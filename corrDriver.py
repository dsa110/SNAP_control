#!/usr/bin/env python
"""Micro service to handle correlator related commands
Command key: /cmd/corr/<machine_numer>
Monitor Key: /mon/corr/<machine_number>

Commands: {cmd: "start"}
          {cmd: "stop"}

Monitor: {machine_number: int, running: bool, sim: bool, start_time: ISO8601}
"""
import etcd3
import json
from time import sleep
import argparse
import yaml
from os.path import dirname
from os.path import realpath
import sys

ALL_CORRS = 'All'

TOP_OF_TREE = dirname(dirname(realpath(__file__)))
# python3
#sys.path.append(str(Path(TOP_OF_TREE + '/SNAP_control/scripts')))
sys.path.append(TOP_OF_TREE + '/SNAP_control/correlator')
from Correlator import Correlator

DBG = True

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


def process_command(my_corr):
    """Etcd watch callback function. Called when values of watched
       keys are updated.

    :param event: Etcd event containing the key and value.
    :type event: TODO fill in.
    """

    def a(event):
        dprint("corr.py.process_command() process_command() event= {}".format(event), 'INFO', DBG)
        key = event.key.decode('utf-8')
        value = event.value.decode('utf-8')
        dprint("corr.py.process_command() key= {}, value= {}".format(key, value), 'INFO', DBG)
        # parse the JSON command
        cmd = parse_value(value)
        for key, val in cmd.items():
            dprint("corr.py.process_command() cmd key= {}, cmd val= {}".format(key, val), 'INFO', DBG)
        dprint("corr.py.process_command() a: cmd= {}".format(cmd), 'INFO', DBG)
        dprint("corr.py.process_command() sending to my_corr.process", 'INFO', DBG)
        my_corr.process(cmd)
    return a

def process_run(args):
    """Main entry point. Will never return.

    :param args: Input arguments from argparse.
    """

    dprint(args.etcd_file, 'INFO', DBG)
    etcd_params = read_yaml(args.etcd_file)

    dprint(args.corr_config_file, 'INFO', DBG)
    corr_params = read_yaml(args.corr_config_file)

    # dprint(args.corr_num, 'INFO', DBG)

    my_corrs = []
    #for corr_num in corr_params['corrs']:
    print("corr.py.process_run() creatting process to handle corr on: {}".format(args.machine_name))
    my_corr = Correlator(args.machine_name, corr_params['machine'][args.machine_name], corr_params['common'])

    ########
    # my_corr.halt()
    # my_corr.go()
    # my_corrs.append(my_corr)
    # my_corr.process({'cmd': 'go'})
    ########
    
    etcd_host, etcd_port = parse_endpoint(etcd_params['endpoints'])
    dprint("corr.py.corr_run() etcd host={}, etcd port={}".format(etcd_host, etcd_port), 'INFO')
    etcd = etcd3.client(host=etcd_host, port=etcd_port)
    watch_ids = []

    #for idx, my_corr in enumerate(my_corrs, start=1):
    valid_corrs = [ALL_CORRS, args.machine_name]
    for name in valid_corrs:
        cmd = etcd_params['corr_command'] + str(name)
        if my_corr is not None:
            print('corrDriver.py.corr_run() watch cmd= {}'.format(cmd))
            watch_id = etcd.add_watch_callback(cmd, process_command(my_corr))
            watch_ids.append(watch_id)

    while True:
        #for idx, my_corr in enumerate(my_corrs, start=1):
        #key = '/mon/corr/' + str(args.machine_name)
        # print('corrDriver.process_run() mon key= {}'.format(key))
        # md = my_corr.get_monitor_data()
        # print(md)
        # etcd.put(key, md)
        sleep(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-ef', '--etcd_file', type=str,
                        default='etcdConfig.yml',
                        help='etcd parameters')
    parser.add_argument('-sf', '--corr_config_file', type=str,
                        default='corrConfig.yml',
                        help='corr parameters')
    parser.add_argument('-m', '--machine_name', type=str, help='CORR machine name')
    the_args = parser.parse_args()
    dprint(the_args, 'INFO', DBG)
    process_run(the_args)
