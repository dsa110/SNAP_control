#!/bin/bash

# start snap services
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.187 -n 1  -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg&
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.183 -n 2  -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg&
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.190 -n 3  -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg&
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.189 -n 4  -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg&
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.186 -n 5  -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg&
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.240 -n 6  -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg&
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.242 -n 7  -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg&
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.188 -n 8  -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg&
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.179 -n 9  -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg&
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.175 -n 10 -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg &
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.157 -n 11 -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg &
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.178 -n 12 -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg &
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.149 -n 13 -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg &
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.155 -n 14 -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg &
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.148 -n 15 -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg &
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.154 -n 16 -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg &
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.174 -n 17 -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg &
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.152 -n 18 -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg &
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.153 -n 19 -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg &
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.176 -n 20 -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg &
./prog_fpga.py  -cf ../config/dsa.yaml -hs 10.41.0.245 -n 21 -f ../config/snap_fengine_nophase_2022-03-16_1517.fpg &

