# SNAP_control
scripts and code to configure SNAP-1 boards for DSA-110.

### 1. Description

The good stuff is in SNAP_control, which is based on the dsaX_snap class. This class enables M&C of a single SNAP. It is invoked by the script snap.py, which communicates with the etcd store. The commands of interest are "prog", "arm", "level", and "test", although "level" is not fully tested. The commands do not take any values.

Depends on casperfpga (among other things), which is within the hera_corr_f/control_software dir. 

