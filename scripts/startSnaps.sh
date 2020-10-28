#!/bin/bash

# start snap services
pkill -9 -f snap.py
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.150 -df ../config/beamformer_weights.yaml -n 1 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs snap01.sas.pvt -df ../config/beamformer_weights.yaml -n 2 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs snap02.sas.pvt -df ../config/beamformer_weights.yaml -n 3 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.147 -df ../config/beamformer_weights.yaml -n 4 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs snap04.sas.pvt -df ../config/beamformer_weights.yaml -n 5 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs snap05.sas.pvt -df ../config/beamformer_weights.yaml -n 6 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs snap06.sas.pvt -df ../config/beamformer_weights.yaml -n 7 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs snap07.sas.pvt -df ../config/beamformer_weights.yaml -n 8 &
