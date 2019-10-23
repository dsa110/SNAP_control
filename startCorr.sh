#!/bin/bash

# start Correlatore services

./corrDriver.py --machine_name dsamaster > dsamaster.log 2>&1 &
./corrDriver.py --machine_name dsa3 > dsa3.log 2>&1 &
./corrDriver.py --machine_name dsa4 > dsa4.log 2>&1 &
./corrDriver.py --machine_name dsa1 > dsa1.log 2>&1 &
./corrDriver.py --machine_name dsa2 > dsa2.log 2>&1 &

