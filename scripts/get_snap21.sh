#!/bin/bash

while true; do
    
    ./get_spec_tstamp.py -cf ../config/dsa.yaml -hs 10.41.0.185 -f /home/ubuntu/snap22/snap22 -a 100 -b 101 -c 999
    
    sleep 60

done



