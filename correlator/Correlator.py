""" Correlator class for controlling DBE.
"""
import pytz
import os
import sys
import datetime
import subprocess
import json
from time import sleep

class Correlator:
    """Correlator is a class for managing the running of the DSA10 Correlator.
    """

    def __init__(self, machine_name, cfg, cmn):
        """ C-tor
        :param machine_name: Machine name
        :param cfg: Configuration for this specific machine
        :param cmn: Common configuration
        :type machine_name: String
        :type cfg: Dictionary
        :type cmn: Dictionary
        """
        self.machine_name = machine_name
        # self.capture_ip = cfg['capture']['ip']
        self.cfg = cfg
        self.cmn = cmn
        self.running = False
        self.started_utc = "1970-01-01T00:00:00+00:00"
        self.known_commands = {}
        self.known_commands['cbuffers'] = self.cbuffers
        self.known_commands['start_rx'] = self.start_rx
        self.known_commands['start_tx'] = self.start_tx
        self.known_commands['halt'] = self.halt

    def _cpscr_log_filename(self, log_root):
        """Private helper to construct cpscr log filename.

        Example: /mnt/nfs/runtime/tmplog/cpscr_log_'+machine+'.log

        :param log_root: Base path for log file
        :type log_root: String
        :return: cpscr log filename
        :rtype: String
        """
        
        # '/mnt/nfs/runtime/tmplog/cpscr_log_'+machine+'.log'
        return '{}{}.log'.format(log_root, self.machine_name)

    def _cpscr(self, cpscr_cmd, log_root):
        """Private helper to run cpscr on remote machine

        :param cpscr_cmd: cpscr command to execute on remote machine
        :param log_root: Base filename for logging
        :type cpscr_cmd: String
        :type log_root: String
        """
        
        # cpscr_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+cpscr+'"', shell = True, stdout=cpscr_log, stderr=cpscr_log)
        with open(self._cpscr_log_filename(log_root), 'w') as log:
            cmd = self._subprocess_cmd(self.machine_name, cpscr_cmd)
            subprocess.Popen(cmd, shell=True, stdout=log, stderr=log)

    def _final_log_filename(self, log_root):
        """Private helper to construct final log filename.

        Example: /mnt/nfs/runtime/tmplog/final_log_'+machine+'.log

        :param log_root: Base path for log file
        :type log_root: String
        :return: final log filename
        :rtype: String
        """

        # '/mnt/nfs/runtime/tmplog/final_log_'+machine+'.log'
        return '{}{}.log'.format(log_root, self.machine_name)

    def _final_cmd(self, cmd, c, filename, o, ip):
        """Private helper to construct final command

        :param cmd: Base command.
        :param c: Option -c for command.
        :param filename: Option -f for command.
        :param o: Option -o for command.
        :param ip: Option -i for command. (i.e. 10.10.1.1)
        :type cmd: String
        :type c: Integer
        :type filename: String
        :type o: Float
        :type ip: String
        :return: final Command.
        :rtype: String
        """
        
        # '/usr/local/dsaX/bin/dsaX_writevis -c 13 -f /home/user/data/run1/dsa4 -o 1365.20508  -i 10.10.1.10'
        return '{} -c {} -f {} -o {} -i {}'.format(cmd, c, filename, o, ip)

    def _final(self, final_log_root):
        """Private helper to run the final command on remote host.

        :param final_log_root: Log file base name.
        :type final_log_root: String
        """
        # final_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+final+'"', shell = True, stdout=final_log, stderr=final_log)
        # final_log = open(self._final_log_filename(final_root), 'w')
        with open(self._final_log_filename(final_log_root), 'w') as log:
            final_cmd = self._final_cmd(self.cmn['final']['cmd'],
                                        self.cmn['final']['c'],
                                        self.cfg['final']['filename'],
                                        self.cfg['final']['o'],
                                        self.cfg['final']['ip'])
            cmd = self._subprocess_cmd(self.machine_name, final_cmd)
            subprocess.Popen(cmd, shell=True, stdout=log, stderr=log)

    def _massager_cmd(self, cmd, c, nbytes):
        """Private helper for return massager command.

        :param cmd: Base command.
        :param c: Option -c for command.
        :param nbytes: Option -n for command.
        :type cmd: String
        :type c: Integer
        :type nbytes: Integer
        :return: massager command
        :rtype: String
        """
        # '/usr/local/dsaX/bin/dsaX_fancy -c 14 -n '+nbytes_final
        return '{} -c {} -n {}'.format(cmd, c, nbytes)

    def _subprocess_cmd(self, machine, cmd):
        """Private helper to prepend ssh syntax to allow running command remotely.

        :param machine: Machine name to run command on.
        :param cmd: Command to run on machine.
        :type machine: String
        :type cmd: String
        :return: Full command to be run by OS.
        :rtype: String
        """

        return 'ssh user@'+machine+' "source ~/.bashrc; '+cmd+'"'

    def _massager_log_filename(self, log_root):
        """Private helper to construct massager log filename.

        Example: /mnt/nfs/runtime/tmplog/massager_log_'+machine+'.log

        :param log_root: Base path for log file
        :type log_root: String
        :return: massager log filename
        :rtype: String
        """

        # '/mnt/nfs/runtime/tmplog/massager_log_'+machine+'.log'
        return '{}{}.log'.format(log_root, self.machine_name)
    
    def _massager(self, log_root):
        """Private helper to run massager command.

        :param log_root: Base log filename for logging.
        :type log_root: String
        """

        #massager_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+massager+'"', shell = True, stdout=massager_log, stderr=massager_log)
        with open(self._massager_log_filename(log_root), 'w') as log:
            massager_cmd = self._massager_cmd(self.cmn['massager']['cmd'],
                                              self.cmn['massager']['c'],
                                              self.cmn['nbytes_final'])
            cmd = self._subprocess_cmd(self.machine_name, massager_cmd)
            subprocess.Popen(cmd, shell=True, stdout=log, stderr=log)

    def _ar_log_filename(self, log_dir, idx):
        """Private helper to construct ar log filename.

        Example: /mnt/nfs/runtime/tmplog/ar1_log_'+machine+'.log

        :param log_root: Base path for log file
        :type log_root: String
        :return: ar log filename
        :rtype: String
        """
        return '{}/ar{}_log_{}.log'.format(log_dir, idx, self.machine_name)

    def _ar_cmd(self, cmd, args):
        """Private helper to return ar command.

        Example: /usr/local/dsaX/bin/dsaX_single -k adbd -o bdad -c 24
        :param cmd: Base command
        :param args: Arguments for command.
        :type cmd: String
        :type args: Dictionary. keys are options, val are option values.
        :return: ar command
        :rtype: String
        """
        
        # '/usr/local/dsaX/bin/dsaX_single -k adbd -o bdad -c 24'
        return '{} -k {} -o {} -c {}'.format(cmd, args['k'], args['o'], args['c'])

    def _ar(self, log_dir, idx):
        """Private helper to run ar command.

        :param log_dir: Base directory for log file
        :param idx: Index for log file
        :type log_dir: String
        :type idx: Integer
        """

        # ar1_log = open('/mnt/nfs/runtime/tmplog/ar1_log_'+machine+'.log','w')
        # ar1 = '/usr/local/dsaX/bin/dsaX_single -k adbd -o bdad -c 24'
        # ar1_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+ar1+'"', shell = True, stdout=ar1_log, stderr=ar1_log)
        log_fn = self._ar_log_filename(log_dir, idx)
        sys.stderr.write("idx= {} ar: {}\n".format(idx, self.cmn['ar']))
        ar_cmd = self._ar_cmd(self.cmn['ar_cmd'], (self.cmn['ar'])[idx-1])
        with open(log_fn, 'w') as log:
            cmd = self._subprocess_cmd(self.machine_name, ar_cmd)
            subprocess.Popen(cmd, shell=True, stdout=log, stderr=log)

    def _ndb_log_filename(self, log_dir, idx):
        """Private helper to construct ndb log filename.

        Example: /mnt/nfs/runtime/tmplog/ndb1_log_'+machine+'.log

        :param log_dir: Directory for log file.
        :param idx: Number in log filename
        :type log_root: String
        :type idx: Integer
        :return: ndb log filename
        :rtype: String
        """

        # /mnt/nfs/runtime/tmplog/ndb1_log_'+machine+'.log'
        return '{}/ndb{}_log_{}.log'.format(log_dir, idx, self.machine_name)

    def _ndb_cmd(self, cmd, args):
        """Private helper to return ndb command.

        Example: /usr/local/dsaX/bin/dsaX_nicdb -k adbd -p 7016 -c 8 -b '+nbytes_many+' -i 10.10.4.5

        :param cmd: Base command.
        :params args: Command arguments.
        :type cmd: String
        :type args: Dictionary
        :return: ndb command
        :rtype: String
        """
        # '/usr/local/dsaX/bin/dsaX_nicdb -k adbd -p 7016 -c 8 -b '+nbytes_many+' -i 10.10.4.5'
        return '{} -k {} -p {} -c {} -b {} -i {}'.format(cmd, args['k'],
                                                         args['port'],
                                                         args['c'],
                                                         self.cmn['nbytes_many'],
                                                         args['ip'])
    def _ndb(self, log_dir, idx, args):
        """Private helper to run ndb command.

        :param log_dir: Directory for log.
        :param idx: Number for log filename
        :param args: Command arguments
        :type log_dir: String
        :type idx: Integer
        :type args: Dictionary
        """

        # ndb1_log = open('/mnt/nfs/runtime/tmplog/ndb1_log_'+machine+'.log','w')
        # ndb1_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+nicdb1+'"', shell = True, stdout=ndb1_log, stderr=ndb1_log)
        log_fn = self._ndb_log_filename(log_dir, idx)
        ndb_cmd = self._ndb_cmd(self.cmn['nicdb']['cmd'], args)
        with open(log_fn, 'w') as log:
            cmd = self._subprocess_cmd(self.machine_name, ndb_cmd)
            subprocess.Popen(cmd, shell=True, stdout=log, stderr=log)

    def _dbn_log_filename(self, log_dir, idx):
        """Private helper to construct dbn log filename.

        Example: /mnt/nfs/runtime/tmplog/db1_log_'+machine+'.log

        :param log_dir: directory for log file
        :param idx: Number used in log name
        :type log_dir: String
        :type idx: Integer
        :return: dbn log filename
        :rtype: String
        """
        """Private helper
        """
        # /mnt/nfs/runtime/tmplog/db1_log_'+machine+'.log'
        return '{}/db{}_log_{}.log'.format(log_dir, idx, self.machine_name)

    def _dbn_cmd(self, cmd, port, args):
        """Private helper to return dbn command

        :param cmd: Base command
        :param port: Option -p for command
        :param args: Other command arguments
        :type cmd: String
        :type port: Integer
        :type args: Dictionary
        :return: dbn command
        :rtype: String
        """
        # '/usr/local/dsaX/bin/dsaX_dbnic -k dbda -i 10.10.4.1 -p 7012 -c 3 -n '+nwait
        return '{} -k {} -i {} -p {} -c {} -n {}'.format(cmd,
                                                         args['k'],
                                                         args['ip'],
                                                         port,
                                                         args['c'],
                                                         self.cmn['nwait'])

    def _dbn(self, log_dir, idx, port, args):
        """Private helper to run dbn command

        :param log_dir: Directory for log
        :param idx: Number for log filename
        :param port: Option -p for command
        :param args: Other arguments for command
        :type log_dir: String
        :type idx: Integer
        :type port: Integer
        :type args: Dictionary
        :return: dbn command
        :rtype: String
        """

        # db1_log = open('/mnt/nfs/runtime/tmplog/db1_log_'+machine+'.log','w')
        # db1_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+dbnic1+'"', shell = True, stdout=db1_log, stderr=db1_log)
        log_fn = self._dbn_log_filename(log_dir, idx)
        dbn_cmd = self._dbn_cmd(self.cmn['dbnic']['cmd'], port, args)
        with open(log_fn, 'w') as log:
            cmd = self._subprocess_cmd(self.machine_name, dbn_cmd)
            subprocess.Popen(cmd, shell=True, stdout=log, stderr=log)

    def _fanout_log_filename(self, log_root):
        """Private helper to construct fanout log filename.

        Example: /mnt/nfs/runtime/tmplog/fanout_log_'+machine+'.log

        :param log_root: Base path for log file
        :type log_root: String
        :return: fanout log filename
        :rtype: String
        """

        return '{}/fanout_log_{}.log'.format(log_root, self.machine_name)

    def _fanout_cmd(self, cmd, c, n):
        """Private helper to return fanout commant.

        Example: '/usr/local/dsaX/bin/dsaX_correlator_fanout -c 2 -n '+nsamps

        :param cmd: Base command
        :param c: Option -c for command.
        :param n: Option -n for command.
        :type cmd: String
        :type c: Integer
        :type n: Integer
        :return: fanout command
        :rtype: String
        """
        # '/usr/local/dsaX/bin/dsaX_correlator_fanout -c 2 -n '+nsamps
        return '{} -c {} -n {}'.format(cmd, c, n)
    
    def _fanout(self, log_root):
        """Private helper ro run fancout command

        :param log_root: Diretory for log
        :type log_root: String
        """

        # fanout_log = open('/mnt/nfs/runtime/tmplog/fanout_log_'+machine+'.log','w')
        log_fn = self._fanout_log_filename(log_root)
        with open(log_fn, 'w') as log:
            fanout_cmd = self._fanout_cmd(self.cmn['fanout']['cmd'],
                                          self.cmn['fanout']['c'],
                                          self.cmn['nsamps'])
            cmd = self._subprocess_cmd(self.machine_name, fanout_cmd)
            # fanout_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+fanout+'"', shell = True, stdout=fanout_log, stderr=fanout_log)
            subprocess.Popen(cmd, shell=True, stdout=log, stderr=log)


    def _capture_cmd(self, cmd, b, f, k, p, ip):
        """Private helper to return capture command.

        Example: /usr/local/dsaX/bin/dsaX_correlator_udpdb_thread -b 1 -f /mnt/nfs/code/dsaX/src/correlator_header_dsaX.txt -k caca -i 10.10.9.1 -p 4011

        :param cmd: Base  command
        :param b: Option -b for command
        :param f: Option -f for command
        :param k: Option -k for command
        :param p: Option -p for command
        :param ip: Option -i for command
        :type cmd: String
        :type b: Integer
        :type f: String
        :type k: String
        :type p: Integer
        :type ip: String
        :return: capture command
        :rtype: String
        """
        # '/usr/local/dsaX/bin/dsaX_correlator_udpdb_thread -b 1 -f /mnt/nfs/code/dsaX/src/correlator_header_dsaX.txt -k caca -i 10.10.9.1 -p 4011'
        return '{} -b {} -f {} -k {} -i {} -p {}'.format(cmd, b, f, k, ip, p)

    def _capture_log_filename(self, log_root):
        """Private helper to construct capture log filename.

        Example: /mnt/nfs/runtime/tmplog/capture_log_'+machine+'.log

        :param log_root: Base path for log file
        :type log_root: String
        :return: capture log filename
        :rtype: String
        """
        # '/mnt/nfs/runtime/tmplog/capture_log_'+machine+'.log'
        return '{}/capture_log_{}.log'.format(log_root, self.machine_name)
        
    def _capture(self, log_root):
        """Private helper to run capture command

        :param log_root: Base log filename.
        :type log_root: String
        """

        # capture_log = open(,'w')
        log_fn = self._capture_log_filename(log_root)
        with open(log_fn, 'w') as log:
            capture_cmd = self._capture_cmd(self.cmn['capture']['cmd'],
                                           self.cmn['capture']['b'],
                                           self.cmn['capture']['filename'],
                                           self.cmn['capture']['k'],
                                           self.cmn['capture']['port'],
                                           self.cfg['capture']['ip'])
            cmd = self._subprocess_cmd(self.machine_name, capture_cmd)
            # capture_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+capture+'"', shell = True, stdout=capture_log, stderr=capture_log)
            subprocess.Popen(cmd, shell=True, stdout=log, stderr=log)

    def _stop_process(self, name):
        """Private helper to stop a process name on remote machine.

        :param name: Process name to stop.
        :type name: String
        """
        
        # 'ssh user@'+machine+' "source ~/.bashrc; killall -q dsaX_correlator_udpdb_thread"'
        cmd = 'ssh user@{} "source ~/.bashrc; killall -q {}"'.format(self.machine_name, name)
        output = subprocess.Popen(cmd, shell=True)
        subprocess.Popen.wait(output)

    def cbuffers(self):
        """Create DADA buffers.
        """
        
        sys.stderr.write('creating dada buffers on {}\n'.format(self.machine_name))
        for buf in self.cmn['buffer']:
            self._create_buffer(buf['k'], buf['b'], buf['c'], buf['n'])

    def _destroy_buffer(self, name):
        """Private helper to destroy dada buffer

        :param name: DADA buffer name
        :type name: String
        """

        # 'ssh user@'+machine+' "source ~/.bashrc; dada_db -k dbda -d"'
        cmd = 'ssh user@{} "source ~/.bashrc; dada_db -k {} -d"'.format(self.machine_name, name)
        os.system(cmd)

    def _create_buffer(self, name, b, c, n):
        """Private helper to create DADA buffer on local machine.

        :param name: DADA buffer name
        :param b: Option -b
        :param c: Option -c
        :param n: Option -n
        """

        # 'ssh user@'+machine+' "source ~/.bashrc; dada_db -k eada -b 42240000 -l -p -c 1 -n 4"')
        cmd = 'ssh user@{} "source ~/.bashrc; dada_db -k {} -b {} -l -p -c {} -n {}"'.format(self.machine_name, name, b, c, n)
        os.system(cmd)

    def process(self, cmd_dict):
        """Run Correlator command.

        :param cmd_dict: Dictionary containing command to run
        :type cmd_dict: Dictionary
        """
        
        sys.stderr.write("Correlator.process() cmd_dict= {}\n".format(cmd_dict))
        cmd =  cmd_dict['cmd']
        cmd in self.known_commands and self.known_commands[cmd]()

    def start_rx(self):
        """Start receivers
        """
        
        sys.stderr.write('Starting cpscr\n')
        self._cpscr(self.cmn['cpscr']['cmd'], self.cmn['cpscr']['log'])
        sleep(0.1)
        
        sys.stderr.write('Starting final\n')
        self._final(self.cmn['final']['log'])
        sleep(0.1)
        
        sys.stderr.write('Starting massager\n')
        self._massager(self.cmn['massager']['log'])
        sleep(0.1)

        sys.stderr.write('Starting expands\n')
        for idx, ar in enumerate(self.cmn['ar'], start=1):
            self._ar(self.cmn['log_dir'], idx)
            sleep(0.1)
            
        sys.stderr.write('Starting nicdbs\n')
        for idx, ndb in enumerate(self.cfg['nicdb'], start=1):
            sys.stderr.write('  nicdb for -k {}\n'.format(ndb['k']))
            self._ndb(self.cmn['log_dir'], idx, ndb)
            sleep(0.1)

    def start_tx(self):
        """Start transmittes.
        """

        sys.stderr.write('Starting dbnics\n')
        for idx, dbn in enumerate(self.cfg['dbnic'], start=1):
            self._dbn(self.cmn['log_dir'],
                      idx,
                      self.cfg['dbnic_port'],
                      dbn)
            sleep(0.1)

        sys.stderr.write('Starting fanout\n')
        self._fanout(self.cmn['log_dir'])
        sleep(0.1)

        sys.stderr.write('Starting capture\n')
        self._capture(self.cmn['log_dir'])
        sleep(0.1)

        
    def stop(self):
        """Stop all processes
        """

        sys.stderr.write('Killing everything\n')
        self._stop_process('dsaX_correlator_udpdb_thread')
        self._stop_process('dsaX_correlator_fanout')
        self._stop_process('dsaX_dbnic')
        self._stop_process('dsaX_nicdb')
        self._stop_process('dsaX_single')
        self._stop_process('dsaX_fancy')
        self._stop_process('dsaX_writevis')
        self._stop_process('cpscr.bash')

    def dbuffers(self):
        """Delete all DADA buffers
        """

        sys.stderr.write('destroying dada buffers on {}\n'.format(self.machine_name))
        for buf in self.cmn['buffer']:
            self._destroy_buffer(buf['k'])

    def halt(self):
        """Stop all processes and destroy DADA buffers.
        """

        self.stop()
        self.dbuffers()

    def get_monitor_data(self):
        """Return monitor data as a JSON string

        :return: JSON encode monitor data.
        :rtype: String
        """
        
        utc = pytz.UTC
        mon_data = {}
        cur_time = datetime.datetime.utcnow(). \
                      replace(tzinfo=utc).isoformat()
        mon_data['time'] = cur_time
        mon_data['name'] = self.machine_name
        mon_data['cap_ip'] = self.cfg['capture']['ip']
        mon_data['running'] = self.running
        mon_data['started_utc'] = self.started_utc
        mon_data['sim'] = False

        try:
            md_json = json.dumps(mon_data)
        except ValueError:
            sys.stderr.write("get_monitor_data(): JSON encode error. Check JSON."
                             "mon_data = {} {}\n".format(mon_data, 'ERR'))
        return md_json
