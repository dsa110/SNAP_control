#!/bin/bash

# start snap services
pkill -9 -f snap.py
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.187 -df ../config/beamformer_weights.yaml -n 1 -p 0  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.183 -df ../config/beamformer_weights.yaml -n 2 -p 0  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.190 -df ../config/beamformer_weights.yaml -n 3 -p 0  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.189 -df ../config/beamformer_weights.yaml -n 4 -p 0  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.186 -df ../config/beamformer_weights.yaml -n 5 -p 0  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.240 -df ../config/beamformer_weights.yaml -n 6 -p 0  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.242 -df ../config/beamformer_weights.yaml -n 7 -p 0  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.188 -df ../config/beamformer_weights.yaml -n 8 -p 0  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.179 -df ../config/beamformer_weights.yaml -n 9 -p 0  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.185 -df ../config/beamformer_weights.yaml -n 10 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.157 -df ../config/beamformer_weights.yaml -n 11 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.178 -df ../config/beamformer_weights.yaml -n 12 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.247 -df ../config/beamformer_weights.yaml -n 13 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.155 -df ../config/beamformer_weights.yaml -n 14 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.148 -df ../config/beamformer_weights.yaml -n 15 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.154 -df ../config/beamformer_weights.yaml -n 16 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.174 -df ../config/beamformer_weights.yaml -n 17 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.152 -df ../config/beamformer_weights.yaml -n 18 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.153 -df ../config/beamformer_weights.yaml -n 19 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.197 -df ../config/beamformer_weights.yaml -n 20 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.245 -df ../config/beamformer_weights.yaml -n 21 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.195 -df ../config/beamformer_weights.yaml -n 22 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.194 -df ../config/beamformer_weights.yaml -n 23 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.249 -df ../config/beamformer_weights.yaml -n 24 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.160 -df ../config/beamformer_weights.yaml -n 25 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.161 -df ../config/beamformer_weights.yaml -n 26 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.158 -df ../config/beamformer_weights.yaml -n 27 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.244 -df ../config/beamformer_weights.yaml -n 28 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.159 -df ../config/beamformer_weights.yaml -n 29 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.162 -df ../config/beamformer_weights.yaml -n 30 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.166 -df ../config/beamformer_weights.yaml -n 31 -p 1  &
./snap.py -ef ../config/etcdConfig.yml -cf ../config/dsa.yaml -hs 10.41.0.164 -df ../config/beamformer_weights.yaml -n 32 -p 1  &
