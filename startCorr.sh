#!/bin/bash

delay=20
# start Correlatore services.
pkill -9 -f corrDriver.py
src_dir="/home/rh/proj/dsa110-shell/SNAP_control"
$src_dir/corrDriver.py --machine_name dsamaster > dsamaster.log 2>&1 &
#sleep $delay
$src_dir/corrDriver.py --machine_name dsa1 > dsa1.log 2>&1 &
#sleep $delay
$src_dir/corrDriver.py --machine_name dsa2 > dsa2.log 2>&1 &
#sleep $delay
$src_dir/corrDriver.py --machine_name dsa3 > dsa3.log 2>&1 &
#sleep $delay
$src_dir/corrDriver.py --machine_name dsa4 > dsa4.log 2>&1 &

