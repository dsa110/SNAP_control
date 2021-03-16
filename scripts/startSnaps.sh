#!/bin/bash

# start snap services
pkill -9 -f snap.py
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.174 -df ../config/beamformer_weights.yaml -n 1 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.175 -df ../config/beamformer_weights.yaml -n 2 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.178 -df ../config/beamformer_weights.yaml -n 3 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.176 -df ../config/beamformer_weights.yaml -n 4 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.179 -df ../config/beamformer_weights.yaml -n 5 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.149 -df ../config/beamformer_weights.yaml -n 6 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.138 -df ../config/beamformer_weights.yaml -n 7 &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.148 -df ../config/beamformer_weights.yaml -n 8 &
# 00:21:5d:a6:18:01
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.177 -df ../config/beamformer_weights.yaml -n 9 &
# 00:31:48:b7:18:01
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.248 -df ../config/beamformer_weights.yaml -n 10 &
