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
from hera_corr_f import HeraCorrelator

class DsaXConfig:
    """ DsaXConfig is a class for handling SNAP configuration
        config_file is the overall corr config file
    """
    def __init__(self, config_file):

        self.config_file = config_file
        self.corr = HeraCorrelator(redishost=None, config=config_file, use_redis=False)

        # do some basic checks. 
        if len(self.corr.fengs) == 0:
            su.dprint("No F-Engines are connected. Is the power off?","ERROR")
            exit()
        if not self.corr.config_is_valid:
            su.dprint('Currently loaded config is invalid',"ERROR")
            exit()
        
        # attributes to deal with commands
        self.force_program = False
        self.programmed = False
        self.initialized = False
        self.mansync = False
        self.armed = False
        self.armed_mjd = "1970-01-01T12:00:00"
        self.level_mjd = self.armed_mjd
        self.known_commands = {}
        self.known_commands['prog'] = self.prog
        self.known_commands['init'] = self.init
        self.known_commands['arm'] = self.arm
        self.known_commands['level'] = self.level

        # attributes to deal with monitoring
        
    def prog(self):
        """ Program all unprogrammed SNAPs, unless force_program
        """

        if not self.force_program:
            self.programmed = True
            not_programmed = [feng.fpga.host for feng in self.corr.fengs if not feng.is_programmed()]
            if len(not_programmed) > 0:
                self.programmed = False

        su.dprint("Boards not programmed: "+str(not_programmed),"INFO")
        
        self.corr.program(unprogrammed_only=(not self.force_program))        
        self.programmed = True

        not_programmed = [feng.fpga.host for feng in self.corr.fengs if not feng.is_programmed()]
        if len(not_programmed) > 0:
            self.programmed = False
            su.dprint("prog failed. boards not programmed: "+str(not_programmed),"ERROR")
        
        
    def init(self):
        """ Initialize all SNAP blocks, and configure freq slots
        """

        self.corr.disable_output()
        self.corr.initialize(multithread=True, uninitialized_only=False)        
        if not self.corr.configure_freq_slots():
            su.dprint("init failed. freq slots not configured","ERROR")
        else:
            self.initialized = True
        not_initialized = [feng.fpga.host for feng in self.corr.fengs if not feng.is_initialized()]
        if len(not_initialized) > 0:
            self.initialized = False
            su.dprint("init failed. boards not initialized: "+str(not_initialized),"ERROR")


    def arm(self):
        """ Arm all SNAP boards. Manual sync if set
        """

        self.corr.disable_output()
        self.corr.do_for_all_f("change_period", block="sync", args=[0])
        sync_time = self.corr.resync(manual=self.mansync)
        self.corr.enable_output()
        self.armed = True
        su.dprint("Synced on (UTC): "+time.ctime(sync_time),"INFO")
        
        self.armed_mjd = su.time_to_mjd(sync_time)        
        

    def level(self):
        """ Flattens the bandpass using the eq_coeffs. 
            Will only work if armed.
        """

        ### TODO: multithread this

        for feng in self.corr.fengs:

            try:
                a = feng.eth.get_status()['tx_ctr']; time.sleep(1); b = feng.eth.get_status()['tx_ctr']
            except:
                su.dprint("cannot tell if TX is on: "+feng.fpga.host,"ERROR")
                return()
            if (b-a) == 0:
                su.dprint("TX is off: "+feng.fpga.host,"ERROR")
                return()
            
            for st in range(6):
                
                bp = np.real(feng.corr.get_new_corr(int(st),int(st)))
                bp[np.where(bp==0.0)] = np.median(bp)
                try:
                    coeffs = 50.*np.median(bp)/bp                
                    feng.eq.set_coeffs(int(st),coeffs)
                    su.dprint("Set coeffs for stream "+str(st),"INFO")
                except:
                    su.dprint("couldn't set coeffs for stream "+str(st),"ERROR")
                    su.dprint("min "+str(coeffs.min())+" max "+str(coeffs.max()),"ERROR")
                    

        self.level_mjd = su.time_to_mjd(time.time())
                

    def process(self, cmd_dict):
        """Convert etcd commands local commands.

        :param cmd: etcd value which is a dictionary 'Cmd' as the key
        :type: Dictionary
        """
        su.dprint("dsaX_config_10G.process(). cmd_dict= {}".format(cmd_dict),"INFO")
        cmd = cmd_dict['cmd']
        su.dprint("dsaX_config_10G.process(). cmd= {}".format(cmd),"INFO")
        cmd in self.known_commands and self.known_commands[cmd]()

    def get_monitor_data(self):
        """ Return monitor data in JSON format
        """

        utc = pytz.UTC
        mon_data = {}
        cur_time = datetime.datetime.utcnow().replace(tzinfo=utc).isoformat()
        mon_data['time'] = cur_time        
        mon_data['prog'] = self.programmed
        mon_data['init'] = self.initialized
        mon_data['armed'] = self.armed
        mon_data['armed_mjd'] = self.armed_mjd
        mon_data['level_utc'] = self.level_mjd
        mon_data['sim'] = False

        try:
            md_json = json.dumps(mon_data)
        except ValueError:
            su.dprint("get_monitor_data(): JSON encode error. Check JSON. mon_data = {}".format(mon_data), 'ERR')
        return md_json
