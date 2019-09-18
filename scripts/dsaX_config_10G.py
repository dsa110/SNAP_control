import katcp,corr,numpy as np,struct,time,datetime,sys,socket,os,pause
import matplotlib.pyplot as plt
from astropy.time import Time
import snap_util as su

def config10g(SNAP):
    
    if SNAP==1:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.2')
        time.sleep(2)
    if SNAP==2:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.3')
        time.sleep(2)
    if SNAP==3:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.4')
        time.sleep(2)
    if SNAP==4:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.5')
        time.sleep(2)
    if SNAP==5:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.6')
        time.sleep(2)

        
    print 'connected to FPGA ',fpga,', with est clock',fpga.est_brd_clk()
    
    # snap defaults

    # arp table stuff
    mac_base0 = (2<<40) + (2<<32)
    # dest_macff= 255*(2**40) + 255*(2**32) + 255*(2**24) + 255*(2**16) + 255*(2**8) + 255
    dest_macff = su.fpgs_encode_mac('ff:ff:ff:ff:ff:ff')
    arp_table = [dest_macff for i in range(256)]
    arp_table1 = [0 for i in range(256)]
    
    if SNAP==1:
    
        # defaults for snap-side
        src_ip_base = 10*(2**24) + 10*(2**16) + 5*(2**8) + 2
        src_ip_base1 = 10*(2**24) + 10*(2**16) + 3*(2**8) + 2
        src_port = 4002
        src_port1 = 4002

        dest_ip = 10*(2**24) + 10*(2**16) + 5*(2**8) + 1
        dest_ip1 = 10*(2**24) + 10*(2**16) + 3*(2**8) + 1

        dest_mac = 40175247655025 # 24:8a:07:5d:80:71 // ens6d1 on dsamaster
        dest_mac1 = 40175247654465 # ens6d1 on dsa5

        dest_port = 4011
        dest_port1 = 4011
        
        src_mac = mac_base0+src_ip_base
        src_mac1 = mac_base0+src_ip_base1

        arp_table[2] = src_mac
        arp_table[1] = dest_mac
        arp_table1[2] = src_mac1
        arp_table1[1] = dest_mac1

    if SNAP==2:

        # defaults for snap-side
        src_ip_base = 10*(2**24) + 10*(2**16) + 6*(2**8) + 2
        src_ip_base1 = 10*(2**24) + 10*(2**16) + 3*(2**8) + 3
        src_port = 4002
        src_port1 = 4003

        dest_ip = 10*(2**24) + 10*(2**16) + 6*(2**8) + 1
        dest_ip1 = 10*(2**24) + 10*(2**16) + 3*(2**8) + 1

        dest_mac = 40175247654497 # ens6d1 on dsa1 
        dest_mac1 = 40175247654465 # ens6d1 on dsa5

        dest_port = 4011
        dest_port1 = 4012

        src_mac = mac_base0+src_ip_base
        src_mac1 = mac_base0+src_ip_base1

        arp_table[2] = src_mac
        arp_table[1] = dest_mac
        arp_table1[3] = src_mac1
        arp_table1[1] = dest_mac1
        
    if SNAP==3:

        # defaults for snap-side
        src_ip_base = 10*(2**24) + 10*(2**16) + 7*(2**8) + 2
        src_ip_base1 = 10*(2**24) + 10*(2**16) + 3*(2**8) + 4
        src_port = 4002
        src_port1 = 4004

        dest_ip = 10*(2**24) + 10*(2**16) + 7*(2**8) + 1
        dest_ip1 = 10*(2**24) + 10*(2**16) + 3*(2**8) + 1

        dest_mac = 137432781157265 # ens6d1 on dsa2
        dest_mac1 = 40175247654465 # ens6d1 on dsa5

        dest_port = 4011
        dest_port1 = 4013
        
        src_mac = mac_base0+src_ip_base
        src_mac1 = mac_base0+src_ip_base1

        arp_table[2] = src_mac
        arp_table[1] = dest_mac
        arp_table1[4] = src_mac1
        arp_table1[1] = dest_mac1

    if SNAP==4:

        # defaults for snap-side
        src_ip_base = 10*(2**24) + 10*(2**16) + 8*(2**8) + 2
        src_ip_base1 = 10*(2**24) + 10*(2**16) + 3*(2**8) + 5
        src_port = 4002
        src_port1 = 4005

        dest_ip = 10*(2**24) + 10*(2**16) + 8*(2**8) + 1
        dest_ip1 = 10*(2**24) + 10*(2**16) + 3*(2**8) + 1

        dest_mac = 137432781157249 # ens6d1 on dsa3 
        dest_mac1 = 40175247654465 # ens6d1 on dsa5

        dest_port = 4011
        dest_port1 = 4014
        
        src_mac = mac_base0+src_ip_base
        src_mac1 = mac_base0+src_ip_base1

        arp_table[2] = src_mac
        arp_table[1] = dest_mac
        arp_table1[5] = src_mac1
        arp_table1[1] = dest_mac1
        

    if SNAP==5:

        # defaults for snap-side
        src_ip_base = 10*(2**24) + 10*(2**16) + 9*(2**8) + 2
        src_ip_base1 = 10*(2**24) + 10*(2**16) + 3*(2**8) + 6
        src_port = 4002
        src_port1 = 4006

        dest_ip = 10*(2**24) + 10*(2**16) + 9*(2**8) + 1
        dest_ip1 = 10*(2**24) + 10*(2**16) + 3*(2**8) + 1

        dest_mac = 137432781168273 # ens6d1 on dsa4 
        dest_mac1 = 40175247654465 # ens6d1 on dsa5

        dest_port = 4011
        dest_port1 = 4015
        
        src_mac = mac_base0+src_ip_base
        src_mac1 = mac_base0+src_ip_base1

        arp_table[2] = src_mac
        arp_table[1] = dest_mac
        arp_table1[6] = src_mac1
        arp_table1[1] = dest_mac1
        
    

    # raw data flow
    fpga.config_10gbe_core('eth_gbe0',src_mac, src_ip_base, src_port, arp_table)
    time.sleep(3)
    print 'Configured 10gbe core - RAW'
    print fpga.print_10gbe_core_details('eth_gbe0')

    # accum data flow
    fpga.config_10gbe_core('eth1_gbe1',src_mac1, src_ip_base1, src_port1, arp_table1)
    time.sleep(3)
    print 'Configured 10gbe core - ACCUM'
    print fpga.print_10gbe_core_details('eth1_gbe1')

    # write stuff to registers
    fpga.write_int('acc_len',255);
    fpga.write_int('fft_shift',1023);
    fpga.write_int('port',dest_port);
    fpga.write_int('ip',dest_ip);
    fpga.write_int('port1',dest_port1);
    fpga.write_int('ip1',dest_ip1);

    # set reset for 10g
    fpga.write_int('eth_ctrl',1);
    fpga.write_int('eth1_ctrl',1);
    time.sleep(0.1)
    fpga.write_int('eth_ctrl',0);
    fpga.write_int('eth1_ctrl',0);
    time.sleep(0.1)

    print 'All ready to go!'

def adchist(SNAP,cal_adc):

    if SNAP==1:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.2')
        time.sleep(2)
    if SNAP==2:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.3')
        time.sleep(2)
    if SNAP==3:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.4')
        time.sleep(2)
    if SNAP==4:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.5')
        time.sleep(2)
    if SNAP==5:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.6')
        time.sleep(2)
    print 'connected to FPGA ',fpga,', with est clock',fpga.est_brd_clk()

    if cal_adc==1:
        fpga.write_int('scaling',0)
        time.sleep(0.1)
    fpga.write_int('adc_snap_ctrl',3)
    time.sleep(0.1)
    fpga.write_int('adc_snap_ctrl',0)
    time.sleep(0.1)

    ADC = np.asarray(struct.unpack('<8192b',fpga.read('adc_snap_bram',8192)))

    ADC1 = (np.ravel(np.fliplr(ADC.reshape((1024,4,2))[:,0,:]))).astype('float')
    ADC2 = (np.ravel(np.fliplr(ADC.reshape((1024,4,2))[:,1,:]))).astype('float')
    ADC3 = (np.ravel(np.fliplr(ADC.reshape((1024,4,2))[:,2,:]))).astype('float')
    ADC4 = (np.ravel(np.fliplr(ADC.reshape((1024,4,2))[:,3,:]))).astype('float')

    rms1 = np.std(ADC1)
    rms2 = np.std(ADC2)
    rms3 = np.std(ADC3)
    rms4 = np.std(ADC4)
    
    print 'Initial RMS of ADC 1 ',rms1
    print 'Initial RMS of ADC 2 ',rms2
    print 'Initial RMS of ADC 3 ',rms3
    print 'Initial RMS of ADC 4 ',rms4

    if cal_adc==1:
    
        # aim for rms of 10
        sc = np.zeros(4)
        if rms1<10./np.sqrt(2.):
            sc[0] = 1
        if rms2<10./np.sqrt(2.):
            sc[1] = 1
        if rms3<10./np.sqrt(2.):
            sc[2] = 1
        if rms4<10./np.sqrt(2.):
            sc[3] = 1
        scfac = 0
        for i in np.arange(4):
            scfac += sc[i]*2**(i*2*3)
            scfac += sc[i]*2**((i*2+1)*3)
        fpga.write_int('scaling',int(scfac))

        fpga.write_int('adc_snap_ctrl',3)
        time.sleep(0.1)
        fpga.write_int('adc_snap_ctrl',0)
        time.sleep(0.1)

        ADC = np.asarray(struct.unpack('<8192b',fpga.read('adc_snap_bram',8192)))

        ADC1 = (np.ravel(np.fliplr(ADC.reshape((1024,4,2))[:,0,:]))).astype('float')
        ADC2 = (np.ravel(np.fliplr(ADC.reshape((1024,4,2))[:,1,:]))).astype('float')
        ADC3 = (np.ravel(np.fliplr(ADC.reshape((1024,4,2))[:,2,:]))).astype('float')
        ADC4 = (np.ravel(np.fliplr(ADC.reshape((1024,4,2))[:,3,:]))).astype('float')

        rms1 = np.std(ADC1)
        rms2 = np.std(ADC2)
        rms3 = np.std(ADC3)
        rms4 = np.std(ADC4)
    
        print 'RMS of ADC 1 ',rms1
        print 'RMS of ADC 2 ',rms2
        print 'RMS of ADC 3 ',rms3
        print 'RMS of ADC 4 ',rms4


    plt.figure()

    plt.subplot(251)
    plt.title('ADC 1')
    plt.hist(ADC1,bins=13)
    plt.subplot(256)
    plt.plot(ADC1)
    plt.subplot(252)
    plt.title('ADC 2')
    plt.hist(ADC2,bins=13)
    plt.subplot(257)
    plt.plot(ADC2)
    plt.subplot(253)
    plt.title('ADC 3')
    plt.hist(ADC3,bins=13)
    plt.subplot(258)
    plt.plot(ADC3)
    plt.subplot(254)
    plt.title('ADC 4')
    plt.hist(ADC4,bins=13)
    plt.subplot(259)
    plt.plot(ADC4)
    plt.subplot(155)
    plt.title('All')
    plt.hist(np.ravel(ADC),bins=20)
    plt.show()


def initialise(SNAP):
    
    if SNAP==1:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.2')
        time.sleep(2)
    if SNAP==2:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.3')
        time.sleep(2)
    if SNAP==3:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.4')
        time.sleep(2)
    if SNAP==4:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.5')
        time.sleep(2)
    if SNAP==5:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.6')
        time.sleep(2)
    print 'connected to FPGA ',fpga,', with est clock',fpga.est_brd_clk()
    
    # 2^12-1 is the largest shift
    fpga.write_int('fft_shift',1023)
    time.sleep(0.1)
    

    fpga.write_int('snap_index',SNAP-1)
    time.sleep(0.1)

    fpga.write_int('sel1',2)
    time.sleep(0.1)
    # TODO: magic number: what is 18000?
    fpga.write_int('coeff1',18000)
    time.sleep(0.1)
    
    config10g(SNAP)
    

def set_delays():

    # connect to FPGAs
    f1 = corr.katcp_wrapper.FpgaClient('10.10.1.2')
    time.sleep(2)
    print 'connected to FPGA ',f1,', with est clock',f1.est_brd_clk()
    f2 = corr.katcp_wrapper.FpgaClient('10.10.1.3')
    time.sleep(2)
    print 'connected to FPGA ',f2,', with est clock',f2.est_brd_clk()
    f3 = corr.katcp_wrapper.FpgaClient('10.10.1.4')
    time.sleep(2)
    print 'connected to FPGA ',f3,', with est clock',f3.est_brd_clk()
    f4 = corr.katcp_wrapper.FpgaClient('10.10.1.5')
    time.sleep(2)
    print 'connected to FPGA ',f4,', with est clock',f4.est_brd_clk()
    f5 = corr.katcp_wrapper.FpgaClient('10.10.1.6')
    time.sleep(2)
    print 'connected to FPGA ',f5,', with est clock',f5.est_brd_clk()

    # read delays
    dA, dB = np.loadtxt('/mnt/nfs/runtime/delays.dat').transpose()

    sA = ((dA-np.min(dA))/4e-3).astype('int')+5
    sB = ((dB-np.min(dB))/4e-3).astype('int')+5
    
    print 'Read delays (microsec), and converting to (samples):'
    for i in np.arange(10):
        print dA[i],dB[i],sA[i],sB[i]
    
    f1.write_int('del1',sA[0])
    time.sleep(0.05)
    f1.write_int('del2',sA[0])
    time.sleep(0.05)
    f1.write_int('del3',sB[0])
    time.sleep(0.05)
    f1.write_int('del4',sB[0])
    time.sleep(0.05)
    f1.write_int('del5',sA[1])
    time.sleep(0.05)
    f1.write_int('del6',sA[1])
    time.sleep(0.05)
    f1.write_int('del7',sB[1])
    time.sleep(0.05)
    f1.write_int('del8',sB[1])
    time.sleep(0.05)

    f2.write_int('del1',sA[2])
    time.sleep(0.05)
    f2.write_int('del2',sA[2])
    time.sleep(0.05)
    f2.write_int('del3',sB[2])
    time.sleep(0.05)
    f2.write_int('del4',sB[2])
    time.sleep(0.05)
    f2.write_int('del5',sA[3])
    time.sleep(0.05)
    f2.write_int('del6',sA[3])
    time.sleep(0.05)
    f2.write_int('del7',sB[3])
    time.sleep(0.05)
    f2.write_int('del8',sB[3])
    time.sleep(0.05)

    f3.write_int('del1',sA[4])
    time.sleep(0.05)
    f3.write_int('del2',sA[4])
    time.sleep(0.05)
    f3.write_int('del3',sB[4])
    time.sleep(0.05)
    f3.write_int('del4',sB[4])
    time.sleep(0.05)
    f3.write_int('del5',sA[5])
    time.sleep(0.05)
    f3.write_int('del6',sA[5])
    time.sleep(0.05)
    f3.write_int('del7',sB[5])
    time.sleep(0.05)
    f3.write_int('del8',sB[5])
    time.sleep(0.05)

    f4.write_int('del1',sA[6])
    time.sleep(0.05)
    f4.write_int('del2',sA[6])
    time.sleep(0.05)
    f4.write_int('del3',sB[6])
    time.sleep(0.05)
    f4.write_int('del4',sB[6])
    time.sleep(0.05)
    f4.write_int('del5',sA[7])
    time.sleep(0.05)
    f4.write_int('del6',sA[7])
    time.sleep(0.05)
    f4.write_int('del7',sB[7])
    time.sleep(0.05)
    f4.write_int('del8',sB[7])
    time.sleep(0.05)

    f5.write_int('del1',sA[8])
    time.sleep(0.05)
    f5.write_int('del2',sA[8])
    time.sleep(0.05)
    f5.write_int('del3',sB[8])
    time.sleep(0.05)
    f5.write_int('del4',sB[8])
    time.sleep(0.05)
    f5.write_int('del5',sA[9])
    time.sleep(0.05)
    f5.write_int('del6',sA[9])
    time.sleep(0.05)
    f5.write_int('del7',sB[9])
    time.sleep(0.05)
    f5.write_int('del8',sB[9])
    time.sleep(0.05)

    print 'Set all delays'

def reg_arm_single(SNAP):

    if SNAP==1:
        f2 = corr.katcp_wrapper.FpgaClient('10.10.1.2')
        time.sleep(0.1)
        print 'connected to FPGA',f2,', with est clock',f2.est_brd_clk()
    
    if SNAP==2:
        f2 = corr.katcp_wrapper.FpgaClient('10.10.1.3')
        time.sleep(0.1)
        print 'connected to FPGA',f2,', with est clock',f2.est_brd_clk()

    if SNAP==3:
        f2 = corr.katcp_wrapper.FpgaClient('10.10.1.4')
        time.sleep(0.1)
        print 'connected to FPGA',f2,', with est clock',f2.est_brd_clk()

    f2.write_int('reg_arm',0)
    time.sleep(0.1)
    f2.write_int('force_sync',2)
    time.sleep(0.1)
    f2.write_int('force_sync',0)
    time.sleep(0.1)
    f2.write_int('eth_ctrl',1);
    f2.write_int('eth1_ctrl',1);
    time.sleep(0.1)
    f2.write_int('eth_ctrl',0);
    f2.write_int('eth1_ctrl',0);
    time.sleep(0.1)
    f2.write_int('eth_ctrl',2);
    f2.write_int('eth1_ctrl',2);
    time.sleep(0.1)

    # sync to 2-and-a-bit seconds from now
    now = datetime.datetime.now()
    micr = now.microsecond
    delt = datetime.timedelta(seconds=3,microseconds=1000000-micr)
    print 'Pausing until',now+delt
    delt2 = datetime.timedelta(hours=7,seconds=1)
    myt = (now+delt+delt2).isoformat()
    t = Time(myt,format='isot',scale='utc')
    f = open("/mnt/nfs/runtime/UTC_START.txt","w")
    f.write('{0}\n'.format(t.mjd))
    f.write('{0}\n'.format(myt))
    f.close()
    
    pause.until(now+delt)
    time.sleep(0.2)    
    f2.write_int('reg_arm',1)
    time.sleep(0.01)
    print 'Synced to NTP second'
    time.sleep(2)
    f2.write_int('eth_ctrl',1);
    time.sleep(0.1)
    f2.write_int('eth_ctrl',0);
    time.sleep(0.1)
    f2.write_int('eth_ctrl',2);
    
    
def reg_arm():

    f1 = corr.katcp_wrapper.FpgaClient('10.10.1.2')
    f2 = corr.katcp_wrapper.FpgaClient('10.10.1.3')
    f3 = corr.katcp_wrapper.FpgaClient('10.10.1.4')
    f4 = corr.katcp_wrapper.FpgaClient('10.10.1.5')
    f5 = corr.katcp_wrapper.FpgaClient('10.10.1.6')
    time.sleep(0.1)
    print 'connected to FPGA 1',f1,', with est clock',f1.est_brd_clk()
    print 'connected to FPGA 2',f2,', with est clock',f2.est_brd_clk()
    print 'connected to FPGA 3',f3,', with est clock',f3.est_brd_clk()
    print 'connected to FPGA 4',f4,', with est clock',f4.est_brd_clk()
    print 'connected to FPGA 5',f5,', with est clock',f5.est_brd_clk()
    
    f1.write_int('reg_arm',0)
    f2.write_int('reg_arm',0)
    f3.write_int('reg_arm',0)
    f4.write_int('reg_arm',0)
    f5.write_int('reg_arm',0)
    time.sleep(0.1)

    # jonathon edit force_sync
    f1.write_int('force_sync',2)
    f2.write_int('force_sync',2)
    f3.write_int('force_sync',2)
    f4.write_int('force_sync',2)
    f5.write_int('force_sync',2)
    time.sleep(0.1)
    f1.write_int('force_sync',0)
    f2.write_int('force_sync',0)
    f3.write_int('force_sync',0)
    f4.write_int('force_sync',0)
    f5.write_int('force_sync',0)
    time.sleep(0.1)
    
    f1.write_int('eth_ctrl',1);
    f1.write_int('eth1_ctrl',1);
    f2.write_int('eth_ctrl',1);
    f2.write_int('eth1_ctrl',1);
    f3.write_int('eth_ctrl',1);
    f3.write_int('eth1_ctrl',1);
    f4.write_int('eth_ctrl',1);
    f4.write_int('eth1_ctrl',1);
    f5.write_int('eth_ctrl',1);
    f5.write_int('eth1_ctrl',1);
    time.sleep(0.1)
    f1.write_int('eth_ctrl',0);
    f1.write_int('eth1_ctrl',0);
    f2.write_int('eth_ctrl',0);
    f2.write_int('eth1_ctrl',0);
    f3.write_int('eth_ctrl',0);
    f3.write_int('eth1_ctrl',0);
    f4.write_int('eth_ctrl',0);
    f4.write_int('eth1_ctrl',0);
    f5.write_int('eth_ctrl',0);
    f5.write_int('eth1_ctrl',0);
    time.sleep(0.1)
    f1.write_int('eth_ctrl',2);
    f1.write_int('eth1_ctrl',2);
    f2.write_int('eth_ctrl',2);
    f2.write_int('eth1_ctrl',2);
    f3.write_int('eth_ctrl',2);
    f3.write_int('eth1_ctrl',2);
    f4.write_int('eth_ctrl',2);
    f4.write_int('eth1_ctrl',2);
    f5.write_int('eth_ctrl',2);
    f5.write_int('eth1_ctrl',2);
    time.sleep(0.1)
    
    # sync to 2-and-a-bit seconds from now
    now = datetime.datetime.now()
    micr = now.microsecond
    delt = datetime.timedelta(seconds=3,microseconds=1000000-micr)
    print 'Pausing until',now+delt
    delt2 = datetime.timedelta(hours=7,seconds=1)
    myt = (now+delt+delt2).isoformat()
    t = Time(myt,format='isot',scale='utc')
    f = open("/mnt/nfs/runtime/UTC_START.txt","w")
    f.write('{0}\n'.format(t.mjd))
    f.write('{0}\n'.format(myt))
    f.close()
    
    pause.until(now+delt)
    time.sleep(0.2)
    f1.write_int('reg_arm',1)
    time.sleep(0.01)
    f2.write_int('reg_arm',1)
    time.sleep(0.01)
    f3.write_int('reg_arm',1)
    time.sleep(0.01)
    f4.write_int('reg_arm',1)
    time.sleep(0.01)
    f5.write_int('reg_arm',1)
    print 'Synced to NTP second'
    time.sleep(2)
    #
    f1.write_int('eth_ctrl',1);
    f2.write_int('eth_ctrl',1);
    f3.write_int('eth_ctrl',1);
    f4.write_int('eth_ctrl',1);
    f5.write_int('eth_ctrl',1);
    time.sleep(0.1)
    f1.write_int('eth_ctrl',0);
    f2.write_int('eth_ctrl',0);
    f3.write_int('eth_ctrl',0);
    f4.write_int('eth_ctrl',0);
    f5.write_int('eth_ctrl',0);
    time.sleep(0.1)
    f1.write_int('eth_ctrl',2);
    f2.write_int('eth_ctrl',2);
    f3.write_int('eth_ctrl',2);
    f4.write_int('eth_ctrl',2);
    f5.write_int('eth_ctrl',2);

    time.sleep(0.5)
    print 'RAW DATA SW STATUS',bin(f1.read_int('eth_sw_status')),bin(f2.read_int('eth_sw_status')),bin(f3.read_int('eth_sw_status')),bin(f4.read_int('eth_sw_status')),bin(f5.read_int('eth_sw_status'))
    
def help():

    print 'dsaX_config_10g.py <SNAP> -prog -adc <cal/not> -init -arm -scale <sel1> <coeff1> -check_scale -check_spectra <nsnap> -monitor_spectra <nsnap> -rawlevs -delset -cbp'
    sys.exit()

def checkbp(SNAP):
    
    if SNAP==1:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.2')
        time.sleep(2)
    if SNAP==2:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.3')
        time.sleep(2)
    if SNAP==3:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.4')
        time.sleep(2)
    if SNAP==4:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.5')
        time.sleep(2)
    if SNAP==5:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.6')
        time.sleep(2)
    print 'connected to FPGA ',fpga,', with est clock',fpga.est_brd_clk()

    get=1
    
    print 'Getting data'
    if SNAP==1:
        if get:
            os.system('calc_coefficients -ip 10.10.5.1 -port 4011 -server snap1')
            time.sleep(2)
        c1,c2,c3,c4 = np.loadtxt('/mnt/nfs/runtime/snap1_coeffs.dat').transpose()
    if SNAP==2:
        if get:
            os.system('ssh user@dsa1 calc_coefficients -ip 10.10.6.1 -port 4011 -server snap2')
            time.sleep(2)
        c1,c2,c3,c4 = np.loadtxt('/mnt/nfs/runtime/snap2_coeffs.dat').transpose()
    if SNAP==3:
        if get:
            os.system('ssh user@dsa2 calc_coefficients -ip 10.10.7.1 -port 4011 -server snap3')
            time.sleep(2)
        c1,c2,c3,c4 = np.loadtxt('/mnt/nfs/runtime/snap3_coeffs.dat').transpose()
    if SNAP==4:
        if get:
            os.system('ssh user@dsa3 calc_coefficients -ip 10.10.8.1 -port 4011 -server snap4')
            time.sleep(2)
        c1,c2,c3,c4 = np.loadtxt('/mnt/nfs/runtime/snap4_coeffs.dat').transpose()
    if SNAP==5:
        if get:
            os.system('ssh user@dsa4 calc_coefficients -ip 10.10.9.1 -port 4011 -server snap5')
            time.sleep(2)
        c1,c2,c3,c4 = np.loadtxt('/mnt/nfs/runtime/snap5_coeffs.dat').transpose()

    plt.figure()
    plt.subplot(221)
    #plt.plot(np.log10(-c1+coeff))
    plt.plot(np.log10(c1))
    plt.title('Input 4')
    plt.subplot(222)
    #plt.plot(np.log10(-c2+coeff))
    plt.plot(np.log10(c2))
    plt.title('Input 3')
    plt.subplot(223)
    #plt.plot(np.log10(-c3+coeff))
    plt.plot(np.log10(c3))
    plt.title('Input 2')
    plt.subplot(224)
    #plt.plot(np.log10(-c4+coeff))
    plt.plot(np.log10(c4))
    plt.title('Input 1')
    plt.show()
    
def rawlevels(SNAP,get):

    rmsval = 1.
    print 'Setting 4-bit rms to ',rmsval
    
    if SNAP==1:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.2')
        time.sleep(2)
    if SNAP==2:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.3')
        time.sleep(2)
    if SNAP==3:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.4')
        time.sleep(2)
    if SNAP==4:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.5')
        time.sleep(2)
    if SNAP==5:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.6')
        time.sleep(2)
    print 'connected to FPGA ',fpga,', with est clock',fpga.est_brd_clk()

    # write initial coefficients
    coeff = 2**14
    coeffs = np.ones(2048,'I')*coeff
    write_coeffs = struct.pack('>2048I',*coeffs)
    fpga.write('eq_0_coeffs',write_coeffs);
    fpga.write('eq_1_coeffs',write_coeffs);
    fpga.write('eq_2_coeffs',write_coeffs);
    fpga.write('eq_3_coeffs',write_coeffs);

    print 'Getting data'
    if SNAP==1:
        if get:
            os.system('/mnt/nfs/code/calc_coefficients -ip 10.10.5.1 -port 4011 -server snap1')
            time.sleep(2)
        c1,c2,c3,c4 = np.loadtxt('/mnt/nfs/runtime/snap1_coeffs.dat').transpose()
    if SNAP==2:
        if get:
            os.system('ssh user@dsa1 /mnt/nfs/code/calc_coefficients -ip 10.10.6.1 -port 4011 -server snap2')
            time.sleep(2)
        c1,c2,c3,c4 = np.loadtxt('/mnt/nfs/runtime/snap2_coeffs.dat').transpose()
    if SNAP==3:
        if get:
            os.system('ssh user@dsa2 /mnt/nfs/code/calc_coefficients -ip 10.10.7.1 -port 4011 -server snap3')
            time.sleep(2)
        c1,c2,c3,c4 = np.loadtxt('/mnt/nfs/runtime/snap3_coeffs.dat').transpose()
    if SNAP==4:
        if get:
            os.system('ssh user@dsa3 /mnt/nfs/code/calc_coefficients -ip 10.10.8.1 -port 4011 -server snap4')
            time.sleep(2)
        c1,c2,c3,c4 = np.loadtxt('/mnt/nfs/runtime/snap4_coeffs.dat').transpose()
    if SNAP==5:
        if get:
            os.system('ssh user@dsa4 /mnt/nfs/code/calc_coefficients -ip 10.10.9.1 -port 4011 -server snap5')
            time.sleep(2)
        c1,c2,c3,c4 = np.loadtxt('/mnt/nfs/runtime/snap5_coeffs.dat').transpose()

    
    plt.figure()
    plt.subplot(221)
    #plt.plot(np.log10(-c1+coeff))
    plt.plot(np.log10(c1))
    plt.title('Input 4')
    plt.subplot(222)
    #plt.plot(np.log10(-c2+coeff))
    plt.plot(np.log10(c2))
    plt.title('Input 3')
    plt.subplot(223)
    #plt.plot(np.log10(-c3+coeff))
    plt.plot(np.log10(c3))
    plt.title('Input 2')
    plt.subplot(224)
    #plt.plot(np.log10(-c4+coeff))
    plt.plot(np.log10(c4))
    plt.title('Input 1')
    plt.show()

    c4 = (coeff*rmsval/c4).astype('uint32')
    c3 = (coeff*rmsval/c3).astype('uint32')
    c2 = (coeff*rmsval/c2).astype('uint32')
    c1 = (coeff*rmsval/c1).astype('uint32')
    # TODO: magic number 2048. ?? 2*channels_per_sideband ??    
    coeffs = np.ones(2048,'I')*c1
    write_coeffs = struct.pack('>2048I',*coeffs)
    fpga.write('eq_3_coeffs',write_coeffs);
    coeffs = np.ones(2048,'I')*c2
    write_coeffs = struct.pack('>2048I',*coeffs)
    fpga.write('eq_2_coeffs',write_coeffs);
    coeffs = np.ones(2048,'I')*c3
    write_coeffs = struct.pack('>2048I',*coeffs)
    fpga.write('eq_1_coeffs',write_coeffs);
    coeffs = np.ones(2048,'I')*c4
    write_coeffs = struct.pack('>2048I',*coeffs)
    fpga.write('eq_0_coeffs',write_coeffs);
    
# MAIN BIT OF CODE

scale=0
prog=0
adc=0
init=0
delset=0
arm=0
cs=0
ms=0
ncs=1
rawlevs=0
cscale=0
cpb=0
arm1=0
SNAP = int(sys.argv[1])

for i in np.arange(2,len(sys.argv)):
    if sys.argv[i]=='-scale':
        scale=1
        sel1=int(sys.argv[i+1])
        coeff1=int(sys.argv[i+2])
    if sys.argv[i]=='-cbp':
        cpb=1
    if sys.argv[i]=='-check_scale':
        cscale=1
    if sys.argv[i]=='-check_spectra':
        cs=1
        ncs = SNAP
    if sys.argv[i]=='-prog':
        prog=1
    if sys.argv[i]=='-adc':
        adc=1
        cal_adc = int(sys.argv[i+1])
    if sys.argv[i]=='-init':
        init=1
    if sys.argv[i]=='-delset':
        delset=1
    if sys.argv[i]=='-arm':
        arm=1
    if sys.argv[i]=='-arm1':
        arm1=1
    if sys.argv[i]=='-rawlevs':
        rawlevs=1
        get = int(sys.argv[i+1])
    if sys.argv[i]=='-h':
        help()
        
if prog:

    # program FPGA and calibrate ADC
    if SNAP==1:
        os.system("python adc16_init.py 10.10.1.2 dsa_10gv11s.bof -d 2 -g 5")
    if SNAP==2:
        os.system("python adc16_init.py 10.10.1.3 dsa_10gv11s.bof -d 2 -g 5")
    if SNAP==3:
        #os.system("python adc16_init.py 10.10.1.4 dsa_10gv11s.bof -d 2 -g 5")
        os.system("python adc16_init.py 10.10.1.4 dsa_10gv11s.bof -d 2 -g 5")
    if SNAP==4:
        os.system("python adc16_init.py 10.10.1.5 dsa_10gv11s.bof -d 2 -g 5")
    if SNAP==5:
        os.system("python adc16_init.py 10.10.1.6 dsa_10gv11s.bof -d 2 -g 5")

# adc histograms
if adc:
    adchist(SNAP,cal_adc)

# SNAP bandpasses
if cpb:
    checkbp(SNAP)
    
# initialise 
if init:
    initialise(SNAP)

# arm
if arm:
    reg_arm()

# arm 1
if arm1:
    reg_arm_single(SNAP)

# delset
if delset:
    set_delays()

# check scale params
if cscale:
    if SNAP==1:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.2')
        time.sleep(2)
    if SNAP==2:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.3')
        time.sleep(2)
    if SNAP==3:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.4')
        time.sleep(2)
    if SNAP==4:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.5')
        time.sleep(2)
    if SNAP==5:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.6')
        time.sleep(2)
    print 'connected to FPGA ',fpga,', with est clock',fpga.est_brd_clk()
    print 'Have current sel1 ',fpga.read_int('sel1'),' coeff1 ',fpga.read_int('coeff1')
    
    
# scale
if scale:
    
    if SNAP==1:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.2')
        time.sleep(2)
    if SNAP==2:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.3')
        time.sleep(2)
    if SNAP==3:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.4')
        time.sleep(2)
    if SNAP==4:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.5')
        time.sleep(2)
    if SNAP==5:
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient('10.10.1.6')
        time.sleep(2)
    print 'connected to FPGA ',fpga,', with est clock',fpga.est_brd_clk()

    fpga.write_int('sel1',sel1)
    time.sleep(0.5)
    fpga.write_int('coeff1',coeff1)
    time.sleep(0.5)
    print 'written sel1 ',fpga.read_int('sel1'),' coeff1 ',fpga.read_int('coeff1')


if cs==1:
    print 'Checking spectra from SNAP',ncs
    os.system('ssh user@dsa5 check_spectra '+str(ncs))
    os.system('plot_spectra 1')


    
if rawlevs==1:

    rawlevels(SNAP,get)
