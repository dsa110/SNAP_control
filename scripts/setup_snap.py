from SNAP_control import dsaX_snap
import numpy as np

delays = [[229, 229, 440, 439, 0, 0],[178, 178, 196, 196, 149, 149],[497, 1462, 148, 148, 130, 129],[167, 167, 64, 63, 82, 82],[391, 390, 409, 409, 390, 389],[429, 427, 442, 441, 460, 459],[494, 494, 479, 480, 229, 229],[0, 0, 0, 0, 0, 0]]
snaps = ['00', '01', '02', '03', '04', '05', '06', '07']

for sn in np.arange(8):

    print('snap'+snaps[sn]+'.sas.pvt')
    
    d = dsaX_snap.dsaX_snap('snap'+snaps[sn]+'.sas.pvt','/home/ubuntu/proj/dsa110-shell/SNAP_control/config/dsa.yaml')
    d.feng.corr.set_acc_len(50000)
    d.level()
    d.set_delay(delays=delays[sn])
