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

class dsaX_snap:
    """  is a class for handling SNAP configuration
        host is the hostname of the SNAP
        config_file is the config_file for the correlator
        This class handles the prog, level, arm, and get_monitor_data commands
    """
    def __init__(self, host, config_file, number=1):

        self.host = host
        self.corr = HeraCorrelator(config=config_file)
        self.number = number
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

        try:
            md_json = json.dumps(mon_data)
            all_mon_data = md_json
        except ValueError:
            su.dprint("get_monitor_data(): JSON encode error. Check JSON. mon_data = {}".format(mon_data), 'ERR')
            return
        
        return(all_mon_data)

        
        
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
        self.feng.logger.info("possibly programmed, waiting 60s to check")
        time.sleep(60)
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
        dest_port = self.corr.config['dest_port'] 
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
        dest_port = self.corr.config['dest_port'] 
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
        
    def level(self):
        """ Flattens the bandpass using the eq_coeffs. 
            Will only work if armed.
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

        self.feng.corr.set_acc_len(50000)
        self.feng.logger.info("Set acc len to 50k")
        
        for st in range(6):

            data = np.zeros(1024)
            coeffs = 2.5 + data
            try:
                self.feng.eq.set_coeffs(int(st),coeffs)
                self.feng.logger.info("Set initial coeffs for stream "+str(st))
            except:
                self.feng.logger.error("couldn't set initial coeffs for stream "+str(st))
                
            for i in range(4):
                bp = np.real(self.feng.corr.get_new_corr(int(st),int(st)))
                bp[np.where(bp==0.0)] = np.median(bp)
                data += bp                
            try:
                data = savgol_filter(data,41,3)
                data = np.sqrt(data)
                #for i in range(1024):
                #    self.feng.logger.info("coeff "+str(data[i]))
                coeffs = 2.5*4./data
                coeffs[410:490] = np.median(coeffs[410:490]) # for HI
                self.feng.eq.set_coeffs(int(st),coeffs)
                self.feng.logger.info("Set coeffs for stream "+str(st))
            except:
                self.feng.logger.error("couldn't set coeffs for stream "+str(st))
                self.feng.logger.error("min "+str(coeffs.min())+" max "+str(coeffs.max()))
                    

        self.level_mjd = su.time_to_mjd(time.time())
                
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
                
