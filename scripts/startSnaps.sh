#!/bin/bash

# start snap services
pkill -9 -f snap.py
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs snap00.sas.pvt -n 1 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs snap01.sas.pvt -n 2 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs snap02.sas.pvt -n 3 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs snap03.sas.pvt -n 4 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs snap04.sas.pvt -n 5 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs snap05.sas.pvt -n 6 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs snap06.sas.pvt -n 7 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs snap07.sas.pvt -n 8 &
