#!/home/ubuntu/anaconda3/envs/py27/bin/python
"""mcant is an etcd client for control and monitor of DSA110 antennas
"""

import argparse
import json
from time import sleep
import time
import yaml
import etcd3
from os.path import dirname
from os.path import realpath
import sys
import syslog
from SNAP_control import dsaX_snap, helpers
import logging
logger = helpers.add_default_log_handlers(logging.getLogger("snapmc"))
import numpy as np

def run(args):

    d = dsaX_snap.dsaX_snap(args.host_snap,args.corr_config_file,number=1)
    s1 = d.feng.corr.get_new_corr(0,2)
    a = d.feng.input.get_adc_snapshot(0)    
    s2 = d.feng.corr.get_new_corr(1,3)
    s3 = d.feng.corr.get_new_corr(0,4)
    b = d.feng.input.get_adc_snapshot(1)    
    s4 = d.feng.corr.get_new_corr(1,5)
    s5 = d.feng.corr.get_new_corr(2,4)
    c = d.feng.input.get_adc_snapshot(2)    
    s6 = d.feng.corr.get_new_corr(3,5)

    t = time.asctime()

    np.savez(args.fname,a1=args.a1,a2=args.a2,a3=args.a3,specs=(s1,s2,s3,s4,s5,s6),time=t,snapshots=(a,b,c))
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-hs', '--host_snap', type=str, help='SNAP host name')
    parser.add_argument('-cf', '--corr_config_file', type=str, help='config file')
    parser.add_argument('-f', '--fname', type=str, help='file name')
    parser.add_argument('-a', '--a1', type=str, help='first ant')
    parser.add_argument('-b', '--a2', type=str, help='second ant')
    parser.add_argument('-c', '--a3', type=str, help='third ant')
    the_args = parser.parse_args()
    run(the_args)
