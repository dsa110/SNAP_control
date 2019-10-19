#!/bin/bash

# start Correlatore services

./corr.py --machine_name dsamaster &
./corr.py --machine_name dsa1 &
./corr.py --machine_name dsa2 &
./corr.py --mahcine_name dsa3 &
./corr.py --mahcine_name dsa4 &

