#!/bin/bash

# start snap services
pkill -9 -f snap.py
ping -w2  10.41.0.150
ping -w2  snap01.sas.pvt
ping -w2  snap02.sas.pvt
ping -w2  10.41.0.147
ping -w2  snap04.sas.pvt
ping -w2  snap05.sas.pvt
ping -w2  snap06.sas.pvt
ping -w2  snap07.sas.pvt
