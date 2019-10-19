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
#python3
#from pathlib import Path
import sys
TOP_OF_TREE = dirname(dirname(realpath(__file__)))
# python3
#sys.path.append(str(Path(TOP_OF_TREE + '/SNAP_control/scripts')))
sys.path.append(TOP_OF_TREE + '/SNAP_control/scripts')
from dsaX_config_10G import DsaXConfig

DBG = True
ALL_SNAPS = 0


def read_yaml(fname):
    """Read a YAML formatted file.

    :param fn: YAML formatted filename"
    :type fn: String
    :return: Dictionary on success. None on error
    :rtype: Dictionary
    """

    with open(fname, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            return None


def dprint(msg, level, dbg=True):
    """Simple print which can be turned off.

    :param msg: String to print.
    :param level: String preceeding msg(typically INFO, WARN etc)
    :param dbg: Boolean to print or not.
    :type msg: String
    :type level: String
    :type dbg: Boolean
    """

    if dbg:
        print("{}: {}".format(level, msg))


def parse_endpoint(endpoint):
    """Parse the endpoint string in the first element of the list.
       Go allows multiple endpoints to be specified
       whereas Python only one and has separate args for host and port.

    :param endpoint: host port string of the form host:port.
    :type endpoint: List
    :return: Tuple (host, port)
    :rtype: Tuple
    """

    host, port = endpoint[0].split(':')
    return host, port


def parse_value(value):
    """Parse the string in JSON format and assumed represent a dictionary.

    :param value: JSON string of the form: {"key":"value"}
                  or {"key":number|bool}
    :type value: String
    :return: Key,value dictionary
    :rtype: Dictionary
    :raise: ValueError
    """

    rtn = {}
    try:
        rtn = json.loads(value)
    except ValueError:
        dprint("parse_value(): JSON Decode Error. Check JSON. value= {}".
               format(value), 'ERR')
    return rtn


def process_command(my_snap):
    """Etcd watch callback function. Called when values of watched
       keys are updated.

    :param event: Etcd event containing the key and value.
    :type event: TODO fill in.
    """

    def a(event):
        dprint("snap.py.process_command() process_command() event= {}".format(event), 'INFO', DBG)
        key = event.key.decode('utf-8')
        value = event.value.decode('utf-8')
        dprint("snap.py.process_command() key= {}, value= {}".format(key, value), 'INFO', DBG)
        # parse the JSON command
        cmd = parse_value(value)
        for key, val in cmd.items():
            dprint("snap.py.process_command() cmd key= {}, cmd val= {}".format(key, val), 'INFO', DBG)
        dprint("snap.py.process_command() a: cmd= {}".format(cmd), 'INFO', DBG)
        my_snap.process(cmd)
    return a

def snap_run(args):
    """Main entry point. Will never return.

    :param args: Input arguments from argparse.
    """

    dprint(args.etcd_file, 'INFO', DBG)
    etcd_params = read_yaml(args.etcd_file)

    dprint(args.snap_config_file, 'INFO', DBG)
    snap_params = read_yaml(args.snap_config_file)

    dprint(args.snap_num, 'INFO', DBG)

    my_snaps = []
    #for snap_num in snap_params['snaps']:
    print("snap.py.snap_run() creatting process to handle snap: {}".format(args.snap_num))
    my_snap = DsaXConfig(args.snap_num, snap_params['snap'][args.snap_num], snap_params['common'], snap_params['adc16'])
    my_snaps.append(my_snap)

    etcd_host, etcd_port = parse_endpoint(etcd_params['endpoints'])
    dprint("snap.py.snap_run() etcd host={}, etcd port={}".format(etcd_host, etcd_port), 'INFO')
    etcd = etcd3.client(host=etcd_host, port=etcd_port)
    watch_ids = []

    #for idx, my_snap in enumerate(my_snaps, start=1):
    valid_snaps = [ALL_SNAPS, args.snap_num]
    for num in valid_snaps:
        cmd = etcd_params['command'] + str(num)
        watch_id = etcd.add_watch_callback(cmd, process_command(my_snap))
        watch_ids.append(watch_id)

    while True:
        #for idx, my_snap in enumerate(my_snaps, start=1):
        key = '/mon/snap/' + str(args.snap_num)
        # print('key= {}'.format(key))
        md = my_snap.get_monitor_data()
        # print(md)
        etcd.put(key, md)
        sleep(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-ef', '--etcd_file', type=str,
                        default='etcdConfig.yml',
                        help='etcd parameters')
    parser.add_argument('-sf', '--snap_config_file', type=str,
                        default='snapConfig.yml',
                        help='snap parameters')
    parser.add_argument('-n', '--snap_num', type=int, help='SNAP number')
    the_args = parser.parse_args()
    dprint(the_args, 'INFO', DBG)
    snap_run(the_args)
