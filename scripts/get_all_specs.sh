#!/bin/bash

while true; do

    ./get_spec.py -cf ../config/dsa.yaml -hs 10.41.0.174 -f /home/ubuntu/data/snap1.npz -a 24 -b 25 -c 26
    ./get_spec.py -cf ../config/dsa.yaml -hs 10.41.0.175 -f /home/ubuntu/data/snap2.npz -a 27 -b 28 -c 29
    ./get_spec.py -cf ../config/dsa.yaml -hs 10.41.0.178 -f /home/ubuntu/data/snap3.npz -a 30 -b 31 -c 32
    ./get_spec.py -cf ../config/dsa.yaml -hs 10.41.0.176 -f /home/ubuntu/data/snap4.npz -a 33 -b 34 -c 35
    ./get_spec.py -cf ../config/dsa.yaml -hs 10.41.0.179 -f /home/ubuntu/data/snap5.npz -a 20 -b 19 -c 18
    ./get_spec.py -cf ../config/dsa.yaml -hs 10.41.0.149 -f /home/ubuntu/data/snap6.npz -a 17 -b 16 -c 15
    ./get_spec.py -cf ../config/dsa.yaml -hs 10.41.0.138 -f /home/ubuntu/data/snap7.npz -a 14 -b 13 -c 100 
    ./get_spec.py -cf ../config/dsa.yaml -hs 10.41.0.148 -f /home/ubuntu/data/snap8.npz -a 101 -b 102 -c 116
    ./get_spec.py -cf ../config/dsa.yaml -hs 10.41.0.177 -f /home/ubuntu/data/snap9.npz -a 103 -b 12 -c 11
    ./get_spec.py -cf ../config/dsa.yaml -hs 10.41.0.248 -f /home/ubuntu/data/snap10.npz -a 10 -b 9 -c 8
    ./get_spec.py -cf ../config/dsa.yaml -hs 10.41.0.183 -f /home/ubuntu/data/snap11.npz -a 7 -b 6 -c 5
    ./get_spec.py -cf ../config/dsa.yaml -hs 10.41.0.245 -f /home/ubuntu/data/snap12.npz -a 4 -b 3 -c 2
    ./get_spec.py -cf ../config/dsa.yaml -hs 10.41.0.240 -f /home/ubuntu/data/snap13.npz -a 1 -b 999 -c 999

    sleep 120

done



