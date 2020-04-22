#!/bin/bash

# start snap services
pkill -9 -f snap.py
./snap.py --snap_num 1 > snap1.log 2>&1 &
./snap.py --snap_num 2 > snap2.log 2>&1 &
./snap.py --snap_num 3 > snap3.log 2>&1 &
./snap.py --snap_num 4 > snap4.log 2>&1 &
./snap.py --snap_num 5 > snap5.log 2>&1 &
