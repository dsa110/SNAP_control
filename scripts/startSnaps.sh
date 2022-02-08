#!/bin/bash

# start snap services
pkill -9 -f snap.py
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.156 -df ../config/beamformer_weights.yaml -n 1 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.177 -df ../config/beamformer_weights.yaml -n 2 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.195 -df ../config/beamformer_weights.yaml -n 3 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.139 -df ../config/beamformer_weights.yaml -n 4 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.201 -df ../config/beamformer_weights.yaml -n 5 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.163 -df ../config/beamformer_weights.yaml -n 6 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.136 -df ../config/beamformer_weights.yaml -n 7 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.137 -df ../config/beamformer_weights.yaml -n 8 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.244 -df ../config/beamformer_weights.yaml -n 9 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.192 -df ../config/beamformer_weights.yaml -n 10 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.196 -df ../config/beamformer_weights.yaml -n 11 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.147 -df ../config/beamformer_weights.yaml -n 12 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.194 -df ../config/beamformer_weights.yaml -n 13 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.197 -df ../config/beamformer_weights.yaml -n 14 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.135 -df ../config/beamformer_weights.yaml -n 15 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.142 -df ../config/beamformer_weights.yaml -n 16 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.184 -df ../config/beamformer_weights.yaml -n 17 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.200 -df ../config/beamformer_weights.yaml -n 18 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.198 -df ../config/beamformer_weights.yaml -n 19 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.140 -df ../config/beamformer_weights.yaml -n 20 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.202 -df ../config/beamformer_weights.yaml -n 21 &
#./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.244 -df ../config/beamformer_weights.yaml -n 22 &
