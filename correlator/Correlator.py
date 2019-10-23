""" Correlator class
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
        self.known_commands['go'] = self.go
        self.known_commands['halt'] = self.halt

    def _cpscr_log_filename(self, log_root):
        """Private helper
        """
        # '/mnt/nfs/runtime/tmplog/cpscr_log_'+machine+'.log'
        return '{}{}.log'.format(log_root, self.machine_name)

    def _cpscr(self, cpscr_cmd, log_root):
        """Private helper
        """
        # cpscr_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+cpscr+'"', shell = True, stdout=cpscr_log, stderr=cpscr_log)
        with open(self._cpscr_log_filename(log_root), 'w') as log:
            cmd = self._subprocess_cmd(self.machine_name, cpscr_cmd)
            subprocess.Popen(cmd, shell=True, stdout=log, stderr=log)

    def _final_log_filename(self, log_root):
        """Private helper
        """
        # '/mnt/nfs/runtime/tmplog/final_log_'+machine+'.log'
        return '{}{}.log'.format(log_root, self.machine_name)

    def _final_cmd(self, cmd, c, filename, o, ip):
        """Private helper
        """
        # '/usr/local/dsaX/bin/dsaX_writevis -c 13 -f /home/user/data/run1/dsa4 -o 1365.20508  -i 10.10.1.10'
        return '{} -c {} -f {} -o {} -i {}'.format(cmd, c, filename, o, ip)

    def _final(self, final_log_root):
        """Private helper
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
        """Private helper
        """
        # '/usr/local/dsaX/bin/dsaX_fancy -c 14 -n '+nbytes_final
        return '{} -c {} -n {}'.format(cmd, c, nbytes)

    def _subprocess_cmd(self, machine, cmd):
        """Private helper
        """
        return 'ssh user@'+machine+' "source ~/.bashrc; '+cmd+'"'

    def _massager_log_filename(self, log_root):
        # '/mnt/nfs/runtime/tmplog/massager_log_'+machine+'.log'
        return '{}{}.log'.format(log_root, self.machine_name)
    
    def _massager(self, log_root):
        """Private helper
        """
        #massager_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+massager+'"', shell = True, stdout=massager_log, stderr=massager_log)
        with open(self._massager_log_filename(log_root), 'w') as log:
            massager_cmd = self._massager_cmd(self.cmn['massager']['cmd'],
                                              self.cmn['massager']['c'],
                                              self.cmn['nbytes_final'])
            cmd = self._subprocess_cmd(self.machine_name, massager_cmd)
            subprocess.Popen(cmd, shell=True, stdout=log, stderr=log)

    def _ar_log_filename(self, log_dir, idx):
        """Private helper
        """
        return '{}/ar{}_log_{}.log'.format(log_dir, idx, self.machine_name)

    def _ar_cmd(self, cmd, args):
        """Private helper
        """
        # '/usr/local/dsaX/bin/dsaX_single -k adbd -o bdad -c 24'
        return '{} -k {} -o {} -c {}'.format(cmd, args['k'], args['o'], args['c'])

    def _ar(self, log_dir, idx):
        """Private helper
        """
        # ar1_log = open('/mnt/nfs/runtime/tmplog/ar1_log_'+machine+'.log','w')
        # ar1 = '/usr/local/dsaX/bin/dsaX_single -k adbd -o bdad -c 24'
        # ar1_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+ar1+'"', shell = True, stdout=ar1_log, stderr=ar1_log)
        log_fn = self._ar_log_filename(log_dir, idx)
        print("idx= ", idx, "ar: ", self.cmn['ar'])
        ar_cmd = self._ar_cmd(self.cmn['ar_cmd'], (self.cmn['ar'])[idx-1])
        with open(log_fn, 'w') as log:
            cmd = self._subprocess_cmd(self.machine_name, ar_cmd)
            subprocess.Popen(cmd, shell=True, stdout=log, stderr=log)

    def _ndb_log_filename(self, log_dir, idx):
        """Private helper
        """
        # /mnt/nfs/runtime/tmplog/ndb1_log_'+machine+'.log'
        return '{}/ndb{}_log_{}.log'.format(log_dir, idx, self.machine_name)

    def _ndb_cmd(self, cmd, args):
        """Private helper
        """
        # '/usr/local/dsaX/bin/dsaX_nicdb -k adbd -p 7016 -c 8 -b '+nbytes_many+' -i 10.10.4.5'
        return '{} -k {} -p {} -c {} -b {} -i {}'.format(cmd, args['k'],
                                                         args['port'],
                                                         args['c'],
                                                         self.cmn['nbytes_many'],
                                                         args['ip'])
    def _ndb(self, log_dir, idx, args):
        """Private helper
        """
        # ndb1_log = open('/mnt/nfs/runtime/tmplog/ndb1_log_'+machine+'.log','w')
        # ndb1_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+nicdb1+'"', shell = True, stdout=ndb1_log, stderr=ndb1_log)
        log_fn = self._ndb_log_filename(log_dir, idx)
        ndb_cmd = self._ndb_cmd(self.cmn['nicdb']['cmd'], args)
        with open(log_fn, 'w') as log:
            cmd = self._subprocess_cmd(self.machine_name, ndb_cmd)
            subprocess.Popen(cmd, shell=True, stdout=log, stderr=log)

    def _dbn_log_filename(self, log_dir, idx):
        """Private helper
        """
        # /mnt/nfs/runtime/tmplog/db1_log_'+machine+'.log'
        return '{}/db{}_log_{}.log'.format(log_dir, idx, self.machine_name)

    def _dbn_cmd(self, cmd, port, args):
        """Private helper
        """
        # '/usr/local/dsaX/bin/dsaX_dbnic -k dbda -i 10.10.4.1 -p 7012 -c 3 -n '+nwait
        return '{} -k {} -i {} -p {} -c {} -n {}'.format(cmd,
                                                         args['k'],
                                                         args['ip'],
                                                         port,
                                                         args['c'],
                                                         self.cmn['nwait'])

    def _dbn(self, log_dir, idx, port, args):
        """Private helper
        """
        # db1_log = open('/mnt/nfs/runtime/tmplog/db1_log_'+machine+'.log','w')
        # db1_proc = subprocess.Popen('ssh user@'+machine+' "source ~/.bashrc; '+dbnic1+'"', shell = True, stdout=db1_log, stderr=db1_log)
        log_fn = self._dbn_log_filename(log_dir, idx)
        dbn_cmd = self._dbn_cmd(self.cmn['dbnic']['cmd'], port, args)
        with open(log_fn, 'w') as log:
            cmd = self._subprocess_cmd(self.machine_name, dbn_cmd)
            subprocess.Popen(cmd, shell=True, stdout=log, stderr=log)

    def _fanout_log_filename(self, log_root):
        """Private helper
        """
        return '{}/fanout_log_{}.log'.format(log_root, self.machine_name)

    def _fanout_cmd(self, cmd, c, n):
        """Private helper
        """
        # '/usr/local/dsaX/bin/dsaX_correlator_fanout -c 2 -n '+nsamps
        return '{} -c {} -n {}'.format(cmd, c, n)
    
    def _fanout(self, log_root):
        """Private helper
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
        """Private helper
        """
        # '/usr/local/dsaX/bin/dsaX_correlator_udpdb_thread -b 1 -f /mnt/nfs/code/dsaX/src/correlator_header_dsaX.txt -k caca -i 10.10.9.1 -p 4011'
        return '{} -b {} -f {} -k {} -i {} -p {}'.format(cmd, b, f, k, ip, p)

    def _capture_log_filename(self, log_root):
        # '/mnt/nfs/runtime/tmplog/capture_log_'+machine+'.log'
        return '{}/capture_log_{}.log'.format(log_root, self.machine_name)
        
    def _capture(self, log_root):
        """Private helper
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
        """Private helper
        """
        
        # 'ssh user@'+machine+' "source ~/.bashrc; killall -q dsaX_correlator_udpdb_thread"'
        cmd = 'ssh user@{} "source ~/.bashrc; killall -q {}"'.format(self.machine_name, name)
        output = subprocess.Popen(cmd, shell=True)
        subprocess.Popen.wait(output)

    def _cbuffers(self):
        print('creating dada buffers on ', self.machine_name)
        for buf in self.cmn['buffer']:
            self._create_buffer(buf['k'], buf['b'], buf['c'], buf['n'])

    def _destroy_buffer(self, name):
        """Private helper
        """
        # 'ssh user@'+machine+' "source ~/.bashrc; dada_db -k dbda -d"'
        cmd = 'ssh user@{} "source ~/.bashrc; dada_db -k {} -d"'.format(self.machine_name, name)
        os.system(cmd)

    def _create_buffer(self, name, b, c, n):
        """Private helper
        """
        # 'ssh user@'+machine+' "source ~/.bashrc; dada_db -k eada -b 42240000 -l -p -c 1 -n 4"')
        cmd = 'ssh user@{} "source ~/.bashrc; dada_db -k {} -b {} -l -p -c {} -n {}"'.format(self.machine_name, name, b, c, n)
        os.system(cmd)

    def process(self, cmd_dict):
        print("Correlator.process() cmd_dict= ".format(cmd_dict))
        if cmd_dict['cmd'] == "go":
            print("Correlator.process() running go")
            self.go()
        elif cmd_dict['cmd'] == "stop":
            print("Correlator.process() running stop()")
            stop()
        else:
            print("Unknown cmd: {}".format(cmd))

    def start_rx(self):
        """Start receivers
        """
        
        print('Starting cpscr')
        self._cpscr(self.cmn['cpscr']['cmd'], self.cmn['cpscr']['log'])
        sleep(0.1)
        
        print('Starting final')
        self._final(self.cmn['final']['log'])
        sleep(0.1)
        
        print('Starting massager')
        #self._massager(self.cmn['massager']['log'])
        self._massager("/mnt/nfs/runtime/tmplog/massager_log_")
        sleep(0.1)

        print('Starting expands')
        for idx, ar in enumerate(self.cmn['ar'], start=1):
            self._ar(self.cmn['log_dir'], idx)
            sleep(0.1)
            
        print('Starting nicdbs')
        for idx, ndb in enumerate(self.cfg['nicdb'], start=1):
            self._ndb(self.cmn['log_dir'], idx, ndb)
            sleep(0.1)

    def start_tx(self):
        print('Starting dbnics')
        for idx, dbn in enumerate(self.cfg['dbnic'], start=1):
            self._dbn(self.cmn['log_dir'],
                      idx,
                      self.cfg['dbnic_port'],
                      dbn)
            sleep(0.1)

        print('Starting fanout')
        self._fanout(self.cmn['log_dir'])
        sleep(0.1)

        print('Starting capture')
        self._capture(self.cmn['log_dir'])
        sleep(0.1)

        
    def stop(self):
        print('Killing everything')
        self._stop_process('dsaX_correlator_udpdb_thread')
        self._stop_process('dsaX_correlator_fanout')
        self._stop_process('dsaX_dbnic')
        self._stop_process('dsaX_nicdb')
        self._stop_process('dsaX_single')
        self._stop_process('dsaX_fancy')
        self._stop_process('dsaX_writevis')
        self._stop_process('cpscr.bash')

    def dbuffers(self):
        print('destroying dada buffers on ', self.machine_name)
        self._destroy_buffer('dbda')
        self._destroy_buffer('dcda')
        self._destroy_buffer('ddda')
        self._destroy_buffer('ebda')
        self._destroy_buffer('ecda')
        self._destroy_buffer('adbd')
        self._destroy_buffer('adcd')
        self._destroy_buffer('addd')
        self._destroy_buffer('aaaa')
        self._destroy_buffer('aaba')
        self._destroy_buffer('bdad')
        self._destroy_buffer('bdcd')
        self._destroy_buffer('bddd')
        self._destroy_buffer('bbbb')
        self._destroy_buffer('bbab')
        self._destroy_buffer('eada')
        self._destroy_buffer('caca')

    def halt(self):
        self.stop()
        self.dbuffers()

    def go(self):
        self._cbuffers()
        self.start_rx()
        self.start_tx()

    def get_monitor_data(self):
        """Return monitor data as a tupe of JSON string and dictionary

        rtype: Tuple(String, Dictionary)
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
            print("get_monitor_data(): JSON encode error. Check JSON."
                  "mon_data = {}".format(mon_data), 'ERR')
        return md_json
