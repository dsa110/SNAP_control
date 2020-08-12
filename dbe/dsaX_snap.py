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
from hera_corr_f import SnapFengine

class dsaX_snap:
    """ DsaXConfig is a class for handling SNAP configuration
        host is the hostname of the SNAP
        This class handles the prog, forceprog, level, and get_monitor_data commands
    """
    def __init__(self, host):

        self.host = host
        self.feng = SnapFengine(host,redishost=None)

        # do some basic checks. 
        if not self.fpga.is_connected():
            su.dprint("F-Engine is not connected. Is the power off?","ERROR")
            exit()
        
        # attributes to deal with commands
        if self.feng.is_programmed():
            self.programmed = True
        else:            
            self.programmed = False
        self.level_mjd = "1970-01-01T12:00:00"
        self.known_commands = {}
        self.known_commands['prog'] = self.prog
        self.known_commands['forceprog'] = self.forceprog
        self.known_commands['level'] = self.level
        self.known_commands['mon'] = self.get_monitor_data

        
    def prog(self):
        """ Program all unprogrammed SNAPs
        """

        if self.programmed is False:
            self.feng.fpga.transport.prog_user_image()
            self.programmed = True
            
        if self.feng.is_programmed() is False:
            self.programmed = False
            su.dprint("prog failed","ERROR")

    def forceprog(self):
        """ Program all SNAPs
        """

        self.feng.fpga.transport.prog_user_image()
        self.programmed = True
            
        if self.feng.is_programmed() is False:
            self.programmed = False
            su.dprint("forceprog failed","ERROR")                    

    def level(self):
        """ Flattens the bandpass using the eq_coeffs. 
            Will only work if armed.
        """

        ### TODO: multithread this

        try:
            a = self.feng.eth.get_status()['tx_ctr']; time.sleep(1); b = feng.eth.get_status()['tx_ctr']
        except:
            su.dprint("cannot tell if TX is on: "+feng.fpga.host,"ERROR")
            return()
        if (b-a) == 0:
            su.dprint("TX is off: "+self.feng.fpga.host,"ERROR")
            return()
            
        for st in range(6):
                
            bp = np.real(self.feng.corr.get_new_corr(int(st),int(st)))
            bp[np.where(bp==0.0)] = np.median(bp)
            try:
                coeffs = 50.*np.median(bp)/bp                
                self.feng.eq.set_coeffs(int(st),coeffs)
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
            Returns a dictionary of JSON strings, one for each feng. 
            Some information is common to all fengs. 
        """

        all_mon_data = {}
        utc = pytz.UTC
        cur_time = datetime.datetime.utcnow().replace(tzinfo=utc).isoformat()
        snap_ctr = 0

        # TODO: implement lookup table for SNAP hosts to numbers in etcd
        
        feng = self.feng 
                    
        mon_data = {}            

        # common stuff
        mon_data['time'] = cur_time        
        mon_data['prog'] = self.programmed
        mon_data['level_utc'] = self.level_mjd
        mon_data['sim'] = False

        # per-SNAP stuff

        fpga_stats = feng.get_fpga_stats()
        mns,pows,rmss = feng.input.get_stats(sum_cores=True)
        ant_ids = feng.ant_indices
        pfb_overflow = feng.pfb.is_overflowing()
        cl1 = feng.eq.clip_count(); time.sleep(0.5); cl2 = feng.eq.clip_count()
        clip_rate = 2.*(cl2-cl1)
        eth_status = feng.eth.get_status()
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
        mon_data['eth_tx_ctr'] = eth_status['tx_ctr']
        mon_data['eth_tx_err'] = eth_status['tx_err']
        mon_data['eth_tx_ctr'] = eth_status['tx_ctr']
        mon_data['eth_tx_of'] = eth_status['tx_of']
        mon_data['eth_tx_vld'] = eth_status['tx_vld']
        mon_data['ant0_A_bp'] = bp0
        mon_data['ant0_B_bp'] = bp1
        mon_data['ant1_A_bp'] = bp2
        mon_data['ant1_B_bp'] = bp3
        mon_data['ant2_A_bp'] = bp4
        mon_data['ant2_B_bp'] = bp5
        mon_data['ant0_A_h'] = h0
        mon_data['ant0_B_h'] = h1
        mon_data['ant1_A_h'] = h2
        mon_data['ant1_B_h'] = h3
        mon_data['ant2_A_h'] = h4
        mon_data['ant2_B_h'] = h5
        
        
        try:
            md_json = json.dumps(mon_data)
            all_mon_data = md_json
        except ValueError:
            su.dprint("get_monitor_data(): JSON encode error. Check JSON. mon_data = {}".format(mon_data), 'ERR')
            return

        return(all_mon_data)
                
