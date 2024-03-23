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


def snap_run(args):
    """Main entry point. Will never return.

    :param args: Input arguments from argparse.
    """
    my_snap = dsaX_snap.dsaX_snap(args.host_snap,args.corr_config_file,number=args.snap_num)
    my_snap.feng.fpga.upload_to_ram_and_program(args.fpg)
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-cf', '--corr_config_file', type=str,
                        default='dsa_single.yml',
                        help='corr parameters')
    parser.add_argument('-hs', '--host_snap', type=str, help='SNAP host name')
    parser.add_argument('-n', '--snap_num', type=int, help='SNAP number in etcd')
    parser.add_argument('-f', '--fpg', type=str, help='fpg file')
    the_args = parser.parse_args()
    snap_run(the_args)
