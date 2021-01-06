#!/bin/bash

# start snap services
pkill -9 -f snap.py
ping -w2  10.41.0.150
ping -w2  snap01.sas.pvt
ping -w2  snap02.sas.pvt
ping -w2  10.41.0.147
ping -w2  10.41.0.137
ping -w2  10.41.0.149
ping -w2  10.41.0.249
ping -w2  10.41.0.148
