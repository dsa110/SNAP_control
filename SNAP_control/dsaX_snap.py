""" Handle snap configuration
"""
import pytz
import json
import numpy as np
import struct
import time
import datetime
import sys
import socket
import os
import snap_util as su
from snap_fengine import SnapFengine
from hera_corr import HeraCorrelator
from scipy.signal import savgol_filter

# ---------------------------------------------------------------------------
# level() robustness knobs (2026-08-03)
# ---------------------------------------------------------------------------
# Every step of level() talks to the SNAP over tftp/katcp, which is
# intermittently lossy. Before this, a glitch could:
#   * fail the initial flat-coefficient write -- logged, then the bandpass
#     was measured anyway through whatever coefficients happened to be
#     loaded, so that input got silently mis-levelled;
#   * raise inside get_new_corr() -- which propagated out of level() and
#     abandoned EVERY REMAINING INPUT on the board;
#   * fail the final coefficient write -- caught, but the flat fallback
#     write was itself unprotected and could raise, again taking the rest
#     of the board with it;
#   * return an all-zero spectrum without raising, which drives
#     50*4/sqrt(0) to inf and lands that input on the flat fallback.
# and in all cases level_mjd was still stamped as if it had worked.
# Each stream is now attempted up to LEVEL_MAX_ATTEMPTS times, coefficient
# writes are read back and verified, and whatever is still broken at the
# end is logged and published in the monitor data.

#: Attempts per stream (input) before giving up on it.
LEVEL_MAX_ATTEMPTS = 3
#: Seconds to wait between attempts on the same stream.
LEVEL_RETRY_SLEEP_S = 2.0
#: Spectra averaged when measuring a stream's bandpass.
LEVEL_N_SPEC = 4
#: Post-equalisation target amplitude (the historical value).
LEVEL_TARGET = 50.0
#: Accumulation length used while levelling (the historical value).
LEVEL_ACC_LEN = 50000
#: Coefficient read-back tolerance, in LSBs of the Eq block's binary
#: point. set_coeffs truncates coeffs*2**bp to an integer, so a correct
#: write reads back within 1 LSB; 2 leaves room for the rounding
#: direction without admitting a genuinely corrupt transfer.
LEVEL_VERIFY_LSB = 2.0
#: Channel slice held flat across the HI line (the historical value).
LEVEL_HI_SLICE = slice(410, 490)
#: Number of Eq streams per SNAP (3 antennas x 2 pols).
LEVEL_N_STREAMS = 6

class dsaX_snap:
    """  is a class for handling SNAP configuration
        host is the hostname of the SNAP
        config_file is the config_file for the correlator
        This class handles the prog, level, arm, and get_monitor_data commands
    """
    def __init__(self, host, config_file, number=1, port_offset=0):

        self.host = host
        self.corr = HeraCorrelator(config=config_file)
        self.number = number
        self.port_offset=port_offset
        self.mansync = False
        if self.corr.config['sync']=='manual':
            self.mansync = True
        self.feng = SnapFengine(host,ant_indices=self.corr.config['fengines'][host]['ants'])

        # do some basic checks. 
        if not self.feng.fpga.is_connected():
            self.feng.logger.error("F-Engine is not connected. Is the power off?")
            exit()
        
        # attributes to deal with commands
        self.initialized = False
        self.monon = False
        self.ismon = False
        if self.feng.is_programmed():
            self.programmed = True
            if self.feng.is_initialized():
                self.initialized = True
                self.monon = True
        else:            
            self.programmed = False
        
        self.armed_mjd = 55000.0
        self.level_mjd = 55000.0
        # Outcome of the most recent level() call. level_failed lists the
        # stream indices still broken after all retries (empty == clean);
        # level_attempts maps stream index -> attempts consumed. Both are
        # published in the monitor data so a partial level is visible in
        # etcd instead of only in this process's log.
        self.level_failed = []
        self.level_attempts = {}
        self.known_commands = {}
        self.known_commands['prog'] = self.prog
        self.known_commands['progonly'] = self.progonly
        self.known_commands['prong'] = self.prong
        self.known_commands['arm'] = self.arm
        self.known_commands['level'] = self.level
        self.known_commands['mon'] = self.get_monitor_data
        self.known_commands['test'] = self.test
        self.known_commands['set_delay'] = self.set_delay

    def test(self):
        """ tests reception of command
        """

        self.simplemon()
        self.feng.logger.info("test successful")

    def simplemon(self):
        """ send prog, init, armed_mjd to etcd
        """

        all_mon_data = {}
        cur_time = su.time_to_mjd(time.time())
        mon_data = {}            

        # common stuff
        mon_data['time'] = cur_time
        mon_data['prog'] = self.programmed
        mon_data['init'] = self.initialized
        mon_data['armed_mjd'] = self.armed_mjd
        mon_data['number'] = int(self.number)
        # snap.py publishes simplemon() to /mon/snap/<n> straight after
        # every command, so this is the channel that carries the level
        # outcome out of the process. level_failed == [] means clean.
        self._add_level_mon(mon_data)

        try:
            md_json = json.dumps(mon_data)
            all_mon_data = md_json
        except ValueError:
            su.dprint("get_monitor_data(): JSON encode error. Check JSON. mon_data = {}".format(mon_data), 'ERR')
            return

        return(all_mon_data)

    def _add_level_mon(self, mon_data):
        """Add the most recent level() outcome to a monitor dict.

        level_attempts keys are ints; json.dumps stringifies them, so
        consumers see {"0": 1, "1": 2, ...}.
        """
        mon_data['level_mjd'] = self.level_mjd
        mon_data['level_failed'] = list(self.level_failed)
        mon_data['level_attempts'] = dict(self.level_attempts)
        mon_data['level_ok'] = (len(self.level_failed) == 0)

        
        
    def progonly(self):
        """ Program SNAP, and do basic init. configure freq slots
        """

        # wait for ismon to be False
        while self.ismon:
            self.feng.logger.info("waiting for monitoring to finish...")
            time.sleep(0.5)
        
        # turn off monitoring
        self.monon = False

        # program the boards
        self.programmed = False
        self.initialized = False
        self.armed_mjd = 55000.0
        self.feng.fpga.transport.prog_user_image()        
        self.feng.logger.info("possibly programmed, waiting 40s to check")
        time.sleep(40)
        if self.feng.is_programmed() is False:
            self.programmed = False
            self.feng.logger.error("prog failed")
        else:
            self.programmed = True
            self.feng.logger.info("successfully programmed")
        
        self.monon = True
        return(self.simplemon())

    def set_delay(self,delays=[0,0,0,0,0,0]):
        """ Set delays
            delays: 6-element list of delays to add to SNAP inputs (ADC samples)
        """

        # wait for ismon to be False
        while self.ismon:
            self.feng.logger.info("waiting for monitoring to finish...")
            time.sleep(0.5)
        
        # turn off monitoring
        self.monon = False

        # error check
        if len(delays) != 6:
            self.feng.logger.error("delays list needs to be 6 elements long")
            return()
        delays_int = np.asarray(delays).astype(int)

        # implement delays
        for i in range(6):
            self.feng.delay.set_delay(i,delays_int[i])

        self.feng.logger.info("successfully set delays to "+str(delays_int))

        self.monon = True
        


    def prog(self):
        """ Program SNAP, and do basic init. configure freq slots
        """

        # wait for ismon to be False
        while self.ismon:
            self.feng.logger.info("waiting for monitoring to finish...")
            time.sleep(0.5)
        
        # turn off monitoring
        self.monon = False

        # program the boards
        self.programmed = False
        self.initialized = False
        self.armed_mjd = 55000.0
        self.feng.fpga.transport.prog_user_image()        
        self.feng.logger.info("possibly programmed, waiting 60s to check")
        time.sleep(60)
        if self.feng.is_programmed() is False:
            self.programmed = False
            self.feng.logger.error("prog failed")
        else:
            self.programmed = True

        # do the init
        self.feng.logger.info("programmed - now initializing")
        self.feng.eth.disable_tx()
        self.feng.initialize()
        self.initialized = True
        if self.feng.is_initialized() is False:
            self.initialized = False
            self.feng.logger.error("init failed")

        # set delays to make switch happy
        self.feng.sync.set_delay(self.corr.config['fengines'][self.feng.host]['sync_delay'])
            
        self.feng.logger.info("initialized - configuring freq slots")

        # config freq slots
        n_xengs = self.corr.config.get('n_xengs', 16)
        chans_per_packet = self.corr.config.get('chans_per_packet', 384) # Hardcoded in firmware
        self.feng.logger.info('Configuring frequency slots for %d X-engines, %d channels per packet' % (n_xengs, chans_per_packet))
        dest_port = self.corr.config['fengines'][self.feng.host]['dest_port'] 
        for xn, xparams in self.corr.config['xengines'].items():
            chan_range = xparams.get('chan_range', [xn*384, (xn+1)*384])
            chans = range(chan_range[0], chan_range[1])
            if (xn > n_xengs): 
               self.feng.logger.error("Cannot have more than %d X-engs!!" % n_xengs)
            ip = [int(i) for i in xparams['even']['ip'].split('.')]
            ip_even = (ip[0]<<24) + (ip[1]<<16) + (ip[2]<<8) + ip[3]
            ip = [int(i) for i in xparams['odd']['ip'].split('.')]
            ip_odd = (ip[0]<<24) + (ip[1]<<16) + (ip[2]<<8) + ip[3]

            self.feng.logger.info('%s: Setting Xengine %d: chans %d-%d: %s (even) / %s (odd)' % (self.feng.fpga.host, xn, chans[0], chans[-1], xparams['even']['ip'], xparams['odd']['ip']))
            source_port = self.corr.config['fengines'][self.feng.host].get('source_port', dest_port + 1 + self.port_offset)            
            self.feng.packetizer.assign_slot(xn, chans, [ip_even,ip_odd], self.feng.reorder, self.feng.ant_indices[0])
            self.feng.eth.add_arp_entry(ip_even,xparams['even']['mac'])
            self.feng.eth.add_arp_entry(ip_odd,xparams['odd']['mac'])

        self.feng.eth.set_source_port(source_port)
        self.feng.eth.set_port(dest_port)

        self.feng.logger.info('Configured frequency slots')
        
        self.monon = True
        return(self.simplemon())
        
    def prong(self):
        """ Do basic init. Configure freq slots
        """

        # wait for ismon to be False
        while self.ismon:
            self.feng.logger.info("waiting for monitoring to finish...")
            time.sleep(0.5)
        
        # turn off monitoring
        self.monon = False

        self.initialized = False
        self.programmed = True
        if self.feng.is_programmed() is False:
            self.programmed = False
            self.feng.logger.error("prog failed")

        # do the init
        self.feng.logger.info("programmed - now initializing")
        self.feng.eth.disable_tx()
        self.feng.initialize()
        self.initialized = True
        if self.feng.is_initialized() is False:
            self.initialized = False
            self.feng.logger.error("init failed")

        self.feng.logger.info("initialized - configuring freq slots")

        # set delays to make switch happy
        self.feng.sync.set_delay(self.corr.config['fengines'][self.feng.host]['sync_delay'])
        
        # config freq slots
        n_xengs = self.corr.config.get('n_xengs', 16)
        chans_per_packet = self.corr.config.get('chans_per_packet', 384) # Hardcoded in firmware
        self.feng.logger.info('Configuring frequency slots for %d X-engines, %d channels per packet' % (n_xengs, chans_per_packet))
        dest_port = self.corr.config['fengines'][self.feng.host]['dest_port'] 
        for xn, xparams in self.corr.config['xengines'].items():
            chan_range = xparams.get('chan_range', [xn*384, (xn+1)*384])
            chans = range(chan_range[0], chan_range[1])
            if (xn > n_xengs): 
               self.feng.logger.error("Cannot have more than %d X-engs!!" % n_xengs)
            ip = [int(i) for i in xparams['even']['ip'].split('.')]
            ip_even = (ip[0]<<24) + (ip[1]<<16) + (ip[2]<<8) + ip[3]
            ip = [int(i) for i in xparams['odd']['ip'].split('.')]
            ip_odd = (ip[0]<<24) + (ip[1]<<16) + (ip[2]<<8) + ip[3]

            self.feng.logger.info('%s: Setting Xengine %d: chans %d-%d: %s (even) / %s (odd)' % (self.feng.fpga.host, xn, chans[0], chans[-1], xparams['even']['ip'], xparams['odd']['ip']))
            source_port = self.corr.config['fengines'][self.feng.host].get('source_port', dest_port + 1)            
            self.feng.packetizer.assign_slot(xn, chans, [ip_even,ip_odd], self.feng.reorder, self.feng.ant_indices[0])
            self.feng.eth.add_arp_entry(ip_even,xparams['even']['mac'])
            self.feng.eth.add_arp_entry(ip_odd,xparams['odd']['mac'])

        self.feng.eth.set_source_port(source_port)
        self.feng.eth.set_port(dest_port)

        self.feng.logger.info('Configured frequency slots')
        
        self.monon = True
        return(self.simplemon())
        
    def arm(self):
        """ 
        Arm this board, after configuring freq slots
        """        
        # wait for ismon to be False
        while self.ismon:
            self.feng.logger.info("waiting for monitoring to finish...")
            time.sleep(0.5)
        
        # turn off monitoring
        self.monon = False
        
        # do arming
        self.feng.eth.disable_tx()
        self.feng.sync.change_period(0)
        before_sync = time.time()
        if not self.mansync:
            self.feng.logger.info('Waiting for PPS at time '+(time.asctime(time.gmtime(time.time()))))
            self.feng.sync.wait_for_sync()
            self.feng.logger.info('Syncing passed at time '+(time.asctime(time.gmtime(time.time()))))
        self.feng.sync.arm_sync()
        after_sync = time.time()
        if self.mansync:
            self.feng.logger.warning('Using manual sync trigger')
            for i in range(3): # takes 3 syncs to trigger
                self.feng.sync.sw_sync()
                sync_time = int(time.time()) # roughly
        else:
            sync_time = int(before_sync) + 1 + 3 # Takes 3 PPS pulses to arm
        self.feng.logger.info('Syncing was at '+(time.asctime(time.gmtime(sync_time))))
        self.feng.eth.enable_tx()

        self.armed_mjd = su.time_to_mjd(sync_time)
        time.sleep(3)
        self.monon = True
        return(self.simplemon())
        
    def _stream_label(self, st):
        """Readable label for an Eq stream index, e.g. "stream 2 (ant 76 pol A)".

        The antenna numbers are this SNAP's ``ants`` entries from the corr
        config (dsa.yaml), i.e. 0-based cube/voltage indices -- NOT
        operator-facing antenna numbers. Stream ordering follows the Corr
        block's documented input map [1a, 1b, 2a, 2b, 3a, 3b].
        """
        st = int(st)
        try:
            ant = str(self.feng.ant_indices[st // 2])
        except Exception:
            ant = "?"
        return "stream %d (ant %s pol %s)" % (
            st, ant, "A" if st % 2 == 0 else "B")

    def _sanitize_coeffs(self, coeffs):
        """Coerce a coefficient vector into something Eq.set_coeffs can load.

        set_coeffs packs into unsigned shorts, so a single non-finite or
        negative entry makes struct.pack raise and takes the whole write
        with it -- which is how a dead spectrum used to knock an input onto
        the flat fallback. Non-finite / negative entries are replaced by
        the median of the usable ones (or the flat target if there are
        none) and the result is clipped to the representable range.

        A vector that is already finite and in range comes back unchanged,
        so this cannot alter the coefficients in the healthy case.
        """
        eq = self.feng.eq
        c = np.array(coeffs, dtype=np.float64)
        c_max = (2.0 ** eq.width - 1.0) / (2.0 ** eq.bp)
        # NaN >= 0.0 is False, which is what we want, but numpy warns about
        # it; silence that rather than spamming the log on every repair.
        with np.errstate(invalid='ignore'):
            good = np.isfinite(c) & (c >= 0.0)
        if not np.any(good):
            self.feng.logger.error(
                "level: no usable coefficients at all; falling back to flat")
            c = LEVEL_TARGET + np.zeros(eq.ncoeffs, dtype=np.float64)
        elif not np.all(good):
            fill = float(np.median(c[good]))
            self.feng.logger.error(
                "level: %d/%d coefficients were non-finite or negative; "
                "replaced with median %.4f"
                % (int(np.sum(~good)), c.size, fill))
            c[~good] = fill
        return np.clip(c, 0.0, c_max)

    def _write_coeffs_verified(self, st, coeffs):
        """Load coefficients onto a stream and confirm they actually landed.

        Returns True when the board reads back what we asked for. This is
        the check that catches a silently truncated tftp transfer -- the
        failure mode that leaves one input mis-levelled while everything
        reports success.

        Note set_coeffs multiplies its argument IN PLACE (``coeffs *=
        2**bp``), so it is handed a copy and the comparison uses our own
        untouched values.
        """
        st = int(st)
        eq = self.feng.eq
        intended = self._sanitize_coeffs(coeffs)
        eq.set_coeffs(st, intended.copy())
        read_back = np.array(eq.get_coeffs(st), dtype=np.float64)
        if read_back.size != intended.size:
            self.feng.logger.error(
                "level: %s read back %d coefficients, expected %d"
                % (self._stream_label(st), read_back.size, intended.size))
            return False
        # set_coeffs truncates coeffs*2**bp to an integer, so a good write
        # reads back slightly low; anything beyond a couple of LSBs means
        # the transfer was corrupted.
        atol = LEVEL_VERIFY_LSB / (2.0 ** eq.bp)
        diff = np.abs(read_back - intended)
        n_bad = int(np.sum(diff > atol))
        if n_bad:
            self.feng.logger.error(
                "level: %s coefficient read-back differs in %d/%d channels "
                "(max |diff| %.4f, tolerance %.4f)"
                % (self._stream_label(st), n_bad, intended.size,
                   float(np.max(diff)), atol))
            return False
        return True

    def _measure_bandpass(self, st):
        """Average LEVEL_N_SPEC autocorrelation spectra for one stream.

        Returns ``(summed, last)``: the sum used to derive the
        equalisation, and the final individual spectrum (archived to disk,
        preserving what the original code saved).

        Raises RuntimeError on a spectrum that is the wrong length,
        non-finite, or entirely non-positive. A flaky transfer can return a
        dead spectrum WITHOUT raising, and averaging that in is how an
        input ends up flat-levelled with no error anywhere.
        """
        st = int(st)
        # Size off the Corr block's channel count -- this is a spectrum, not
        # a coefficient vector. They are both 1024 today; level() asserts
        # they agree so the derived coefficients are the right length.
        nchans = self.feng.corr.nchans
        total = np.zeros(nchans, dtype=np.float64)
        last = None
        for _ in range(LEVEL_N_SPEC):
            bp = np.array(
                np.real(self.feng.corr.get_new_corr(st, st)), dtype=np.float64)
            if bp.size != nchans:
                raise RuntimeError(
                    "spectrum had %d channels, expected %d" % (bp.size, nchans))
            if not np.all(np.isfinite(bp)):
                raise RuntimeError("spectrum contained non-finite values")
            if not np.any(bp > 0.0):
                raise RuntimeError("spectrum was entirely non-positive")
            # Historical behaviour: zeroed channels take the spectrum
            # median. np.median is evaluated before the assignment, exactly
            # as in the original.
            bp[bp == 0.0] = np.median(bp)
            total += bp
            last = bp
        return total, last

    def _level_stream(self, st):
        """Measure and load equalisation coefficients for a single stream.

        Numerically identical to the original single-pass procedure -- flat
        coefficients, LEVEL_N_SPEC spectra, savgol smooth, sqrt,
        target*n/rms scaling, HI band held at its median -- but every board
        transaction is checked so the caller can retry this stream rather
        than leave it half-configured. Raises on failure.
        """
        st = int(st)
        ncoeffs = self.feng.eq.ncoeffs

        # 1. Flat coefficients, so what we measure is the raw bandpass.
        if not self._write_coeffs_verified(
                st, LEVEL_TARGET + np.zeros(ncoeffs, dtype=np.float64)):
            raise RuntimeError("could not load initial flat coefficients")

        # 2. Measure.
        data, last_spec = self._measure_bandpass(st)

        # 3. Archive the spectrum for offline inspection. Best effort: a
        #    full /home or a missing dir must not fail the level.
        fl = "/home/ubuntu/data/specs/spec_%s_%s.npy" % (self.number, st)
        try:
            np.save(fl, last_spec, allow_pickle=True)
        except Exception as e:
            self.feng.logger.error(
                "level: %s could not save %s: %r"
                % (self._stream_label(st), fl, e))

        # 4. Derive the equalisation.
        smoothed = savgol_filter(data, 41, 3)
        with np.errstate(divide='ignore', invalid='ignore'):
            rms = np.sqrt(smoothed)
            coeffs = LEVEL_TARGET * float(LEVEL_N_SPEC) / rms
        # Sanitize before the HI median so one non-finite channel cannot
        # poison the whole HI band via np.median.
        coeffs = self._sanitize_coeffs(coeffs)
        coeffs[LEVEL_HI_SLICE] = np.median(coeffs[LEVEL_HI_SLICE])
        self.feng.logger.info(
            "level: %s coefficients min %.4f max %.4f"
            % (self._stream_label(st), float(coeffs.min()), float(coeffs.max())))

        # 5. Load them, and confirm.
        if not self._write_coeffs_verified(st, coeffs):
            raise RuntimeError("could not load computed coefficients")
        self.feng.logger.info(
            "level: %s levelled" % self._stream_label(st))

    def _set_acc_len(self, max_attempts):
        """Set the levelling accumulation length, with retries.

        get_new_corr divides by the locally-cached acc_len, so a failed
        write here mis-scales every spectrum on the board and therefore
        every coefficient. The read-back is advisory only: it is logged if
        it disagrees but does not fail the level, since we should not
        assume the register reads back in the same units it is written.
        """
        last_err = None
        for attempt in range(1, int(max_attempts) + 1):
            try:
                self.feng.corr.set_acc_len(int(LEVEL_ACC_LEN))
                try:
                    got = self.feng.corr.read_uint('acc_len')
                    if int(got) != 1024 * int(LEVEL_ACC_LEN):
                        self.feng.logger.error(
                            "level: acc_len read back %s, expected %s "
                            "(continuing anyway)"
                            % (got, 1024 * int(LEVEL_ACC_LEN)))
                except Exception as e:
                    self.feng.logger.info(
                        "level: could not read acc_len back (%r); continuing"
                        % (e,))
                self.feng.logger.info(
                    "level: acc len set to %d" % LEVEL_ACC_LEN)
                return True
            except Exception as e:
                last_err = e
                self.feng.logger.error(
                    "level: attempt %d/%d to set acc len failed: %r"
                    % (attempt, max_attempts, e))
                if attempt < int(max_attempts):
                    time.sleep(LEVEL_RETRY_SLEEP_S)
        self.feng.logger.error(
            "level: giving up on acc len after %d attempts (last error %r)"
            % (max_attempts, last_err))
        return False

    def level(self, max_attempts=LEVEL_MAX_ATTEMPTS):
        """ Flattens the bandpass using the eq_coeffs.
            Will only work if armed.

            Each of the 6 inputs is attempted up to max_attempts times;
            coefficient writes are read back and verified, so a lossy tftp
            transfer is retried instead of silently leaving that input
            mis-levelled. Any input still failing at the end is logged as a
            summary and published in the monitor data as level_failed /
            level_attempts.
        """

        ### TODO: multithread this

        #try:
        #    a = self.feng.eth.get_status()['tx_ctr']; time.sleep(1); b = feng.eth.get_status()['tx_ctr']
        #except:
        #    self.feng.logger.error("cannot tell if TX is on: "+feng.fpga.host)
        #    return()
        #if (b-a) == 0:
        #    self.feng.logger.error("TX is off: "+self.feng.fpga.host)
        #    return()

        max_attempts = max(1, int(max_attempts))
        self.level_failed = []
        self.level_attempts = {}

        # The coefficients are derived channel-for-channel from the measured
        # spectrum, so the two blocks must agree on the channel count.
        if self.feng.corr.nchans != self.feng.eq.ncoeffs:
            self.feng.logger.error(
                "level: refusing to run -- corr has %d channels but eq takes "
                "%d coefficients"
                % (self.feng.corr.nchans, self.feng.eq.ncoeffs))
            self.level_failed = list(range(LEVEL_N_STREAMS))
            return

        # Stop new monitoring passes from interleaving their own board
        # reads with ours -- concurrent tftp traffic to the same FPGA is
        # itself a plausible source of the flakiness this retries around.
        # Deliberately NOT waiting on self.ismon the way prog()/arm() do:
        # get_monitor_data leaves ismon True if it raises part-way, so that
        # wait can hang forever.
        was_monon = self.monon
        self.monon = False
        try:
            if not self._set_acc_len(max_attempts):
                # Nothing downstream is trustworthy without it.
                self.level_failed = list(range(LEVEL_N_STREAMS))
                self.level_mjd = su.time_to_mjd(time.time())
                self.feng.logger.error(
                    "level: FAILED for %s -- could not set acc len, no "
                    "input was levelled" % self.feng.host)
                return

            for st in range(LEVEL_N_STREAMS):
                for attempt in range(1, max_attempts + 1):
                    self.level_attempts[st] = attempt
                    try:
                        self._level_stream(st)
                        if attempt > 1:
                            self.feng.logger.info(
                                "level: %s succeeded on attempt %d/%d"
                                % (self._stream_label(st), attempt,
                                   max_attempts))
                        break
                    except Exception as e:
                        self.feng.logger.error(
                            "level: %s attempt %d/%d failed: %r"
                            % (self._stream_label(st), attempt, max_attempts, e))
                        if attempt < max_attempts:
                            time.sleep(LEVEL_RETRY_SLEEP_S)
                        else:
                            self.level_failed.append(st)
                            # Leave the input at a known flat level rather
                            # than whatever half-written state it is in.
                            try:
                                self.feng.eq.set_coeffs(
                                    int(st),
                                    LEVEL_TARGET + np.zeros(
                                        self.feng.eq.ncoeffs,
                                        dtype=np.float64))
                                self.feng.logger.error(
                                    "level: %s left at flat %g after %d "
                                    "failed attempts"
                                    % (self._stream_label(st), LEVEL_TARGET,
                                       max_attempts))
                            except Exception as e2:
                                self.feng.logger.error(
                                    "level: %s could not even load the flat "
                                    "fallback: %r"
                                    % (self._stream_label(st), e2))

            self.level_mjd = su.time_to_mjd(time.time())

            # ---- end-of-run report -----------------------------------
            retried = sorted([s for s, n in self.level_attempts.items()
                              if n > 1 and s not in self.level_failed])
            if self.level_failed:
                self.feng.logger.error(
                    "level: INCOMPLETE for %s -- %d/%d inputs still failing "
                    "after %d attempts each: %s"
                    % (self.feng.host, len(self.level_failed),
                       LEVEL_N_STREAMS, max_attempts,
                       ", ".join([self._stream_label(s)
                                  for s in self.level_failed])))
            else:
                self.feng.logger.info(
                    "level: complete for %s -- all %d inputs levelled%s"
                    % (self.feng.host, LEVEL_N_STREAMS,
                       (" (%d needed a retry: %s)"
                        % (len(retried),
                           ", ".join([self._stream_label(s)
                                      for s in retried])))
                       if retried else ""))
        finally:
            self.monon = was_monon

    def process(self, cmd_dict):
        """Convert etcd commands local commands.

        :param cmd: etcd value which is a dictionary 'Cmd' as the key
        :type: Dictionary
        """
        self.feng.logger.info("process: cmd_dict= {}".format(cmd_dict))
        cmd = cmd_dict['cmd']
        self.feng.logger.info("process: cmd= {}".format(cmd))
        cmd in self.known_commands and self.known_commands[cmd]()

    def get_all_monitor_data(self):
        """ Return monitor data in JSON format
            Returns a dictionary of JSON strings, one for each feng. 
            Some information is common to all fengs. 
        """
        
        if self.monon is False:
            return -1

        self.ismon = True

        if self.programmed is False:
            self.ismon = False
            return(self.simplemon())
        if self.initialized is False:
            self.ismon = False
            return(self.simplemon())
        
        
        all_mon_data = {}
        cur_time = su.time_to_mjd(time.time())

        feng = self.feng 
                    
        mon_data = {}            

        # common stuff
        mon_data['time'] = cur_time        
        mon_data['prog'] = self.programmed
        mon_data['init'] = self.initialized
        mon_data['armed_mjd'] = self.armed_mjd
        mon_data['level_mjd'] = self.level_mjd
        mon_data['number'] = int(self.number)
        mon_data['sim'] = False
        self._add_level_mon(mon_data)

        # per-SNAP stuff

        sync_ct = feng.sync.count()
        fpga_stats = feng.get_fpga_stats()
        mns,pows,rmss = feng.input.get_stats(sum_cores=True)
        ant_ids = feng.ant_indices
        pfb_overflow = feng.pfb.is_overflowing()
        cl1 = feng.eq.clip_count(); time.sleep(0.5); cl2 = feng.eq.clip_count()
        clip_rate = 2.*(cl2-cl1)
        #eth_status = feng.eth.get_status()
        host = feng.host
        bp0 = np.real(feng.corr.get_new_corr(0,0)).tolist()
        bp1 = np.real(feng.corr.get_new_corr(1,1)).tolist()
        bp2 = np.real(feng.corr.get_new_corr(2,2)).tolist()
        bp3 = np.real(feng.corr.get_new_corr(3,3)).tolist()
        bp4 = np.real(feng.corr.get_new_corr(4,4)).tolist()
        bp5 = np.real(feng.corr.get_new_corr(5,5)).tolist()
        h0 = feng.input.get_histogram(0)[1].tolist()
        h1 = feng.input.get_histogram(1)[1].tolist()
        h2 = feng.input.get_histogram(2)[1].tolist()
        h3 = feng.input.get_histogram(3)[1].tolist()
        h4 = feng.input.get_histogram(4)[1].tolist()
        h5 = feng.input.get_histogram(5)[1].tolist()

        mon_data['sync_ct'] = sync_ct
        mon_data['uptime'] = fpga_stats['uptime']
        mon_data['fpga_temp'] = fpga_stats['temp']
        mon_data['host'] = host
        mon_data['ant0'] = ant_ids[0]
        mon_data['ant1'] = ant_ids[1]
        mon_data['ant2'] = ant_ids[2]
        mon_data['ant0_A_mn'] = mns[0]
        mon_data['ant0_B_mn'] = mns[1]
        mon_data['ant1_A_mn'] = mns[2]
        mon_data['ant1_B_mn'] = mns[3]
        mon_data['ant2_A_mn'] = mns[4]
        mon_data['ant2_B_mn'] = mns[5] 
        mon_data['ant0_A_rms'] = rmss[0]
        mon_data['ant0_B_rms'] = rmss[1]
        mon_data['ant1_A_rms'] = rmss[2]
        mon_data['ant1_B_rms'] = rmss[3]
        mon_data['ant2_A_rms'] = rmss[4]
        mon_data['ant2_B_rms'] = rmss[5] 
        mon_data['pfb_overflow'] = pfb_overflow
        mon_data['eq_clip_rate'] = clip_rate
        #mon_data['eth_tx_ctr'] = eth_status['tx_ctr']
        #mon_data['eth_tx_err'] = eth_status['tx_err']
        #mon_data['eth_tx_ctr'] = eth_status['tx_ctr']
        #mon_data['eth_tx_of'] = eth_status['tx_of']
        #mon_data['eth_tx_vld'] = eth_status['tx_vld']
        #mon_data['ant0_A_bp'] = bp0
        #mon_data['ant0_B_bp'] = bp1
        #mon_data['ant1_A_bp'] = bp2
        #mon_data['ant1_B_bp'] = bp3
        #mon_data['ant2_A_bp'] = bp4
        #mon_data['ant2_B_bp'] = bp5
        #mon_data['ant0_A_h'] = h0
        #mon_data['ant0_B_h'] = h1
        #mon_data['ant1_A_h'] = h2
        #mon_data['ant1_B_h'] = h3
        #mon_data['ant2_A_h'] = h4
        #mon_data['ant2_B_h'] = h5
        
        self.ismon = False
        
        try:
            md_json = json.dumps(mon_data)
            all_mon_data = md_json
        except ValueError:
            su.dprint("get_monitor_data(): JSON encode error. Check JSON. mon_data = {}".format(mon_data), 'ERR')
            return
        
        return(all_mon_data)
                
    def get_monitor_data(self):
        """ Return monitor data in JSON format
            Returns a dictionary of JSON strings, one for each feng. 
            Some information is common to all fengs. 
        """
        
        if self.monon is False:
            return -1

        self.ismon = True

        if self.programmed is False:
            self.ismon = False
            return(self.simplemon())
        if self.initialized is False:
            self.ismon = False
            return(self.simplemon())
        
        
        all_mon_data = {}
        cur_time = su.time_to_mjd(time.time())

        feng = self.feng 
                    
        mon_data = {}            

        # common stuff
        mon_data['time'] = cur_time        
        mon_data['prog'] = self.programmed
        mon_data['init'] = self.initialized
        mon_data['armed_mjd'] = self.armed_mjd
        mon_data['level_mjd'] = self.level_mjd
        mon_data['number'] = int(self.number)
        mon_data['sim'] = False
        self._add_level_mon(mon_data)

        # per-SNAP stuff

        sync_ct = feng.sync.count()
        fpga_stats = feng.get_fpga_stats()
        mns,pows,rmss = feng.input.get_stats(sum_cores=True)
        ant_ids = feng.ant_indices
        pfb_overflow = feng.pfb.is_overflowing()
        cl1 = feng.eq.clip_count(); time.sleep(0.5); cl2 = feng.eq.clip_count()
        clip_rate = 2.*(cl2-cl1)
        #eth_status = feng.eth.get_status()
        host = feng.host

        mon_data['sync_ct'] = sync_ct
        mon_data['uptime'] = fpga_stats['uptime']
        mon_data['fpga_temp'] = fpga_stats['temp']
        mon_data['host'] = host
        mon_data['ant0'] = ant_ids[0]
        mon_data['ant1'] = ant_ids[1]
        mon_data['ant2'] = ant_ids[2]
        mon_data['ant0_A_mn'] = mns[0]
        mon_data['ant0_B_mn'] = mns[1]
        mon_data['ant1_A_mn'] = mns[2]
        mon_data['ant1_B_mn'] = mns[3]
        mon_data['ant2_A_mn'] = mns[4]
        mon_data['ant2_B_mn'] = mns[5] 
        mon_data['ant0_A_rms'] = rmss[0]
        mon_data['ant0_B_rms'] = rmss[1]
        mon_data['ant1_A_rms'] = rmss[2]
        mon_data['ant1_B_rms'] = rmss[3]
        mon_data['ant2_A_rms'] = rmss[4]
        mon_data['ant2_B_rms'] = rmss[5] 
        mon_data['pfb_overflow'] = pfb_overflow
        mon_data['eq_clip_rate'] = clip_rate
        
        self.ismon = False
        
        try:
            md_json = json.dumps(mon_data)
            all_mon_data = md_json
        except ValueError:
            su.dprint("get_monitor_data(): JSON encode error. Check JSON. mon_data = {}".format(mon_data), 'ERR')
            return
        
        return(all_mon_data)
                
