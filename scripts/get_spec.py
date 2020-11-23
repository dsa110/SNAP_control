#!/usr/bin/env python
"""mcant is an etcd client for control and monitor of DSA110 antennas
"""

import argparse
import json
from time import sleep
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
import matplotlib.pyplot as plt, pylab

def plot_spec(s1,s2,s3,s4,s5,s6,ants,fname):

    plt.figure(figsize=(15,5))
    x = 1530. - np.arange(1024)*250./1024.

    pylab.subplot(1,3,1)
    plt.plot(x,10.*np.log10(np.abs(s1)),label=ants[0]+'B')
    plt.plot(x,10.*np.log10(np.abs(s2)),label=ants[0]+'A')
    plt.legend()
    plt.ylabel('Power (rel. dB)')

    pylab.subplot(1,3,2)
    plt.plot(x,10.*np.log10(np.abs(s3)),label=ants[1]+'B')
    plt.plot(x,10.*np.log10(np.abs(s4)),label=ants[1]+'A')
    plt.legend()
    plt.xlabel('Frequency (MHz)')

    pylab.subplot(1,3,3)
    plt.plot(x,10.*np.log10(np.abs(s5)),label=ants[2]+'B')
    plt.plot(x,10.*np.log10(np.abs(s6)),label=ants[2]+'A')
    plt.legend()

    plt.close()
    plt.savefig(fname,bbox_inches='tight')    
    

def run(args):

    d = dsaX_snap.dsaX_snap(args.host_snap,args.corr_config_file,number=1)
    s1 = d.feng.corr.get_new_corr(0,0)
    s2 = d.feng.corr.get_new_corr(1,1)
    s3 = d.feng.corr.get_new_corr(1,1)
    s4 = d.feng.corr.get_new_corr(3,3)
    s5 = d.feng.corr.get_new_corr(4,4)
    s6 = d.feng.corr.get_new_corr(5,5)

    plot_spec(s1,s2,s3,s4,s5,s6,[args.a1,args.a2,args.a3],args.fname)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-hs', '--host_snap', type=str, help='SNAP host name')
    parser.add_argument('-cf', '--corr_config_file', type=str, help='config file')
    parser.add_argument('-f', '--fname', type=str, help='file name')
    parser.add_argument('-a', '--a1', type=str, help='first ant')
    parser.add_argument('-b', '--a3', type=str, help='second ant')
    parser.add_argument('-c', '--a2', type=str, help='third ant')
    the_args = parser.parse_args()
    run(the_args)
