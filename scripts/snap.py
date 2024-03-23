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
        logger.error("parse_value(): JSON Decode Error. Check JSON. value= {}".format(value))
    return rtn


def process_command(my_snap,etcd,keym,keym2,delays,ants,keym3,keym4):
    """Etcd watch callback function. Called when values of watched
       keys are updated.

    :param event: Etcd event containing the key and value.
    :type event: TODO fill in.
    """

    def a(event):
        logger.info("snap.py.process_command() process_command() event= {}".format(event))
        key = event.events[0].key.decode('utf-8')
        value = event.events[0].value.decode('utf-8')
        logger.info("snap.py.process_command() key= {}, value= {}".format(key, value))
        # parse the JSON command
        cmd = parse_value(value)
        for key, val in cmd.items():
            logger.debug("snap.py.process_command() cmd key= {}, cmd val= {}".format(key, val))
        logger.debug("snap.py.process_command() a: cmd= {}".format(cmd))
        if cmd['cmd']=='prog':
            sleep(my_snap.number*0.4)
        if cmd['cmd']=='mon':
            data = my_snap.get_monitor_data()
            if data!=-1:
                try:
                    etcd.put(keym2, data)
                except:
                    logger.error("Could not place full mon into etcd")
        elif cmd['cmd']=='set_delay':
            my_snap.set_delay(delays=delays)
            try:
                etcd.put(keym3,json.dumps({'delays':delays.tolist()}))
                etcd.put(keym4,json.dumps({'antenna_order':ants.tolist()}))
            except:
                logger.error("Could not place delays / antenna_order into etcd")
            
        else:
            # comment out for arm
            #sleep(my_snap.number*1.)
            my_snap.process(cmd)
            data = my_snap.simplemon()
            try:
                etcd.put(keym2, data)
            except:
                logger.error("Could not place simple mon into etcd")

        if cmd['cmd']=='arm':
            try:
                etcd.put(keym,json.dumps({'armed_mjd':my_snap.armed_mjd}))
            except:
                logger.error("Could not place armed_mjd into etcd")
        if cmd['cmd']=='prog':
            try:
                etcd.put(keym3,json.dumps({'delays':np.zeros(6,dtype='int').tolist()}))
                etcd.put(keym4,json.dumps({'antenna_order':ants.tolist()}))
            except:
                logger.error("Could not place zero_delays into etcd")
        if cmd['cmd']=='prong':
            try:
                etcd.put(keym3,json.dumps({'delays':np.zeros(6,dtype='int').tolist()}))
                etcd.put(keym4,json.dumps({'antenna_order':ants.tolist()}))
            except:
                logger.error("Could not place zero delays into etcd")
        if cmd['cmd']=='progonly':
            try:
                etcd.put(keym3,json.dumps({'delays':np.zeros(6,dtype='int').tolist()}))
                etcd.put(keym4,json.dumps({'antenna_order':ants.tolist()}))
            except:
                logger.error("Could not place zero delays into etcd")

        
        
            
    return a

def snap_run(args):
    """Main entry point. Will never return.

    :param args: Input arguments from argparse.
    """

    ## TODO: link snap num to host name

    logger.debug("ETCD config file: "+args.etcd_config_file)
    etcd_params = read_yaml(args.etcd_config_file)
    logger.debug("CORR config file: "+args.corr_config_file)
    logger.debug("HOST SNAP: "+args.host_snap)
    logger.debug("SNAP NUMBER: "+str(args.snap_num))

    delay_params = read_yaml(args.delay_config_file)
    delays = (np.asarray(delay_params['cal_solutions']['delays']).ravel())[(args.snap_num-1)*6:(args.snap_num)*6]
    ants = np.asarray(delay_params['cal_solutions']['antenna_order'])
    
    logger.info("snap.py.snap_run() creatting process to handle snap: {}".format(args.host_snap))
    my_snap = dsaX_snap.dsaX_snap(args.host_snap,args.corr_config_file,number=args.snap_num,port_offset=args.port_offset)

    etcd_host, etcd_port = parse_endpoint(etcd_params['endpoints'])
    logger.info("snap.py.snap_run() etcd host={}, etcd port={}".format(etcd_host, etcd_port))
    etcd = etcd3.client(host=etcd_host, port=etcd_port)
    watch_ids = []
    keym = '/mon/snap/' + str(args.snap_num) + '/armed_mjd'
    keym3 = '/mon/snap/' + str(args.snap_num) + '/delays'
    keym4 = '/mon/snap/' + str(args.snap_num) + '/antenna_order'
    keym2 = '/mon/snap/' + str(args.snap_num)

    
    # add watch on cmd for snapnum
    cmd = etcd_params['snap_command'] + str(args.snap_num)
    logger.info('snap.py.snap_run() watch cmd= {}'.format(cmd))


    watch_id = etcd.add_watch_callback(cmd, process_command(my_snap,etcd,keym,keym2,delays,ants,keym3,keym4))
    watch_ids.append(watch_id)

    # add watch on cmd for snap 0
    cmd = etcd_params['snap_command'] + str(0)
    logger.info('snap.py.snap_run() watch cmd= {}'.format(cmd))
    watch_id = etcd.add_watch_callback(cmd, process_command(my_snap,etcd,keym,keym2,delays,ants,keym3,keym4))
    watch_ids.append(watch_id)

    
    # main loop
    while True:
        
        #md = my_snap.get_monitor_data()
        #if md!=-1:
        #    etcd.put(key, md)
        sleep(10)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-df', '--delay_config_file', type=str,default='beamformer.yaml')
    parser.add_argument('-ef', '--etcd_config_file', type=str,default='etcdConfig.yaml')
    parser.add_argument('-cf', '--corr_config_file', type=str,
                        default='dsa_single.yml',
                        help='corr parameters')
    parser.add_argument('-hs', '--host_snap', type=str, help='SNAP host name')
    parser.add_argument('-n', '--snap_num', type=int, help='SNAP number in etcd')
    parser.add_argument('-p', '--port_offset', type=int, help='Offset of source port')
    the_args = parser.parse_args()
    snap_run(the_args)
