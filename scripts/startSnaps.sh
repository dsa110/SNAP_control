#!/bin/bash

# start snap services
pkill -9 -f snap.py
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.150 -df ../config/beamformer_weights.yaml -n 1 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.243 -df ../config/beamformer_weights.yaml -n 2 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.246 -df ../config/beamformer_weights.yaml -n 3 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.147 -df ../config/beamformer_weights.yaml -n 4 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.137 -df ../config/beamformer_weights.yaml -n 5 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.149 -df ../config/beamformer_weights.yaml -n 6 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.249 -df ../config/beamformer_weights.yaml -n 7 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.148 -df ../config/beamformer_weights.yaml -n 8 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.247 -df ../config/beamformer_weights.yaml -n 9 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.248 -df ../config/beamformer_weights.yaml -n 10 &
