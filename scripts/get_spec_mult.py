#!/usr/bin/env python
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
    s1 = []
    s2 = []
    s3 = []
    s4 = []
    s5 = []
    s6 = []
    
    for i in np.arange(args.num):
        s1.append(d.feng.corr.get_new_corr(0,2))
        s2.append(d.feng.corr.get_new_corr(1,3))
        s3.append(d.feng.corr.get_new_corr(0,4))
        s4.append(d.feng.corr.get_new_corr(1,5))
        s5.append(d.feng.corr.get_new_corr(2,4))
        s6.append(d.feng.corr.get_new_corr(3,5))

    for i in np.arange(args.num-1):
        s1[0] += s1[i]
        s2[0] += s2[i]
        s3[0] += s3[i]
        s4[0] += s4[i]
        s5[0] += s5[i]
        s6[0] += s6[i]
        
    t = time.asctime()

    np.savez(args.fname,a1=args.a1,a2=args.a2,a3=args.a3,specs=(s1[0]/(1.*args.num),s2[0]/(1.*args.num),s3[0]/(1.*args.num),s4[0]/(1.*args.num),s5[0]/(1.*args.num),s6[0]/(1.*args.num)),time=t)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-hs', '--host_snap', type=str, help='SNAP host name')
    parser.add_argument('-cf', '--corr_config_file', type=str, help='config file')
    parser.add_argument('-f', '--fname', type=str, help='file name')
    parser.add_argument('-a', '--a1', type=str, help='first ant')
    parser.add_argument('-b', '--a2', type=str, help='second ant')
    parser.add_argument('-c', '--a3', type=str, help='third ant')
    parser.add_argument('-n', '--num', type=int, help='number of specs to average')
    the_args = parser.parse_args()
    run(the_args)
