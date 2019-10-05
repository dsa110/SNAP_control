""" Handle snap configuration
"""
import pytz
import json
import katcp,corr,numpy as np,struct,time,datetime,sys,socket,os,pause
import matplotlib.pyplot as plt
from astropy.time import Time
import snap_util as su
from adc16 import ADC16

class DsaXConfig:
    """ DsaXConfig is a class for handling SNAP configuration
    """
    def __init__(self, snap_number, snap_ip):
        self.snap_number = snap_number
        self.snap_index = snap_number - 1
        self.snap_ip = snap_ip
        self.wait_for_connect_time_in_seconds = 2.0
        self.src_ip_base = [None, None]
        self.src_port = None
        self.dest_ip = [None, None]
        self.dest_mac = [None, None]
        self.dest_port = [None, None]
        self.mac_broadcast = 'ff:ff:ff:ff:ff:ff'
        self.mac_base0 = '02:02:00:00:00:00'
        self.mac_size = 256
        self.min_ip_idx = 0
        self.max_ip_idx = len(snap_ip)
        self.min_mac_idx = 0
        self.max_mac_idx = len(self.mac_base0)
        # snap has not been programmed, initialized.
        self.programmed = False
        self.initialized = False
        self.adc16 = {}

    def init_commands(self):
        # COMMANDS
        self.known_commands = {}
        known_commands['prog'] = self.prog()
        known_commands['init'] = self.initialize()

    def adc16(self, adc16):
        """ Set the adc16 dictionary which contains parameters
        specifically for the adc16 class.

        :param adc16: Dictionary with parameter for the adc16 class
        :type adc16: Dictionary
        """
        self.adc16 = adc16
        
    def bof(self, bof):
        """ Set the FPGA bof file.

        :param bof: FPGA firmware filename
        :type bof: String
        """

        self.fpga_bof = bof
        
    def adc_gain(self, gain):
        """ Set the ADC gain

        :param gain: ADC gain
        :type gain: float
        """

        # TODO: gain gain validity
        self.adc_gain = gain
        

    def adc_demux(self, adc_demux):
        """ Set ADC demux

        :param adc_demux: ADC demux parameter
        :type adc_demux: float
        """
        
        # TODO: check validity
        slef.adc_demux = adc_demux

    def coeff_filename(self, coeff_fn):
        """ Set the filename containing the SNAP coeff.

        :param coeff_fn: SNAP coefficient filename
        :type coeff_fn: String
        """

        # TODO: check validity
        self.coeff_filename = coeff_fn

    def _dest_ip(self, idx, dest_ip):
        """Set the destination IP

        :param idx: Index for this ip.
        :param dest_ip: IP address in dot notation. AA.BB.CC.DD
        :type idx: Integer
        :type dest_ip: String
        """

        if idx < self.min_ip_idx or idx > self.max_ip_idx:
            raise InvalidNumberException()
        
        # TODO: check IP validity
        self.dest_ip[idx] = dest_ip

    def _src_ip(self, idx, src_ip):
        """Set the source IP

        :param idx: Index for this ip.
        :param dest_ip: IP address in dot notation. AA.BB.CC.DD
        :type idx: Integer
        :type dest_ip: String
        """

        if idx < self.min_ip_idx or idx > self.max_ip_idx:
            raise InvalidNumberException()
        
        # TODO: check IP validity
        self.src_ip[idx] = src_ip

    def _dest_mac(self, idx, dest_mac):
        """Set the destination MAC

        :param idx: Index for this MAC
        :param dest_mac: MAC address in colon notation. 00:11:22:AA:BB:CC:DD
        :type idx: Integer
        :type dest_mac: String
        """

        if idx < self.min_mac_idx or idx > self.max_mac_idx:
            raise InvalidNumberException()
        
        # TODO: check MAC validity
        self.dest_mac[idx] = dest_mac

    def _dest_port(self, idx, dest_port):
        """Set the destination port

        :param idx: Index for this port.
        :param dest_port: Port number
        :type idx: Integer
        :type dest_ip: Integer
        """

        if idx < 0 or idx > 1:
            raise InvalidNumberException()
        
        # TODO: check Port validity
        self.dest_port[idx] = dest_ip

    def _src_port(self, idx, src_port):
        """Set the source port

        :param idx: Index for this port.
        :param src_port: Port number
        :type idx: Integer
        :type src_ip: Integer
        """

        if idx < 0 or idx > 1:
            raise InvalidNumberException()
        
        # TODO: check Port validity
        self.src_port[idx] = src_ip
    
    def dest_ip_mac_port(self, idx, dest_ip, dest_mac, dest_port):
        self._dest_ip(idx, dest_ip)
        self._dest_mac(idx, dest_mac)
        self._dest_port(idx, dest_port)

    def src_ip_port(self, idx, src_ip, src_port):
        self._src_ip(idx, src_ip)
        self._src_port(idx, src_port)
        
    def config10g(self):
        """ config the 10G interface
        """
        
        #TODO: check needed parameters have been set.
        # _check_needed_config_parameters()
        
    
        # snap defaults

        # arp table stuff
        # 2<<40) + (2<<32)
        mac_base0 = su.fpga_encode_mac(self.mac_base0)
        # dest_macff= 255*(2**40) + 255*(2**32) + 255*(2**24) + 255*(2**16) + 255*(2**8) + 255
        dest_macff = su.fpgs_encode_mac(self.mac_broadcast)
        arp_table = [dest_macff for i in range(self.mac_size)]
        arp_table1 = [0 for i in range(self.mac_size)]


        # defaults for snap-side
        # 10*(2**24) + 10*(2**16) + 5*(2**8) + 2
        src_ip_base = su.fpga_encode_ip(self.src_ip_base[0])
        # 10*(2**24) + 10*(2**16) + 3*(2**8) + 2
        src_ip_base1 = su.fpga_encode_ip(self.src_ip_base[1])
        # 4002
        src_port = self.src_port[0]
        # 4002
        src_port1 = self.src_port[1]

        # 10*(2**24) + 10*(2**16) + 5*(2**8) + 1
        dest_ip = su.fpga_encode_ip(self.dest_ip_dsa[0])
        # 10*(2**24) + 10*(2**16) + 3*(2**8) + 1
        dest_ip1 = su.fpga_encode_ip(self.dest_ip_dsa[1])
        # 40175247655025 # 24:8a:07:5d:80:71 // ens6d1 on dsamaster
        dest_mac = su.fpga_encode_mac(self.dest_mac_dsa[0])
        # 40175247654465 # ens6d1 on dsa5
        dest_mac1 = su.fpga_encode_mac(self.dest_mac_dsa[1])

        dest_port = self.dest_port[0]
        dest_port1 = self.dest_port[1]

        src_mac = mac_base0+src_ip_base
        src_mac1 = mac_base0+src_ip_base1

        arp_table[2] = src_mac
        arp_table[1] = dest_mac
        arp_table1[2] = src_mac1
        arp_table1[1] = dest_mac1

        fpga = corr.katcp_wrapper.FpgaClient(self.snap_ip)
        time.sleep(wait_for_connect_time_in_seconds)
        
        print('connected to FPGA ',fpga,', with est clock',fpga.est_brd_clk())

        # raw data flow
        fpga.config_10gbe_core('eth_gbe0', src_mac, src_ip_base,
                               src_port, arp_table)
        time.sleep(self.wait_for_config_in_seconds)  # 3 seconds
        print( 'Configured 10gbe core - RAW')
        print( fpga.print_10gbe_core_details('eth_gbe0'))

        # accum data flow
        fpga.config_10gbe_core('eth1_gbe1',src_mac1, src_ip_base1,
                               src_port1, arp_table1)
        time.sleep(self.wait_for_config_in_seconds)
        print( 'Configured 10gbe core - ACCUM')
        print( fpga.print_10gbe_core_details('eth1_gbe1'))

        # write stuff to registers
        fpga.write_int('acc_len', self.acc_len); # 255
        fpga.write_int('fft_shift', self.fft_shift); # 1023
        fpga.write_int('port',dest_port);
        fpga.write_int('ip',dest_ip);
        fpga.write_int('port1',dest_port1);
        fpga.write_int('ip1',dest_ip1);

        # set reset for 10g
        # TODO: assign magic numbers
        fpga.write_int('eth_ctrl',1);
        fpga.write_int('eth1_ctrl',1);
        # TODO: define 0.1 seconds
        time.sleep(0.1)
        fpga.write_int('eth_ctrl',0);
        fpga.write_int('eth1_ctrl',0);
        time.sleep(0.1)

        print( 'All ready to go!')

    def adchist(self, cal_adc):
        """ Perform an ADC Histogram

        :param cal_adc: ??
        :type cal_adc: ??
        """

        # TODO: Refactor plotting code into snap_plotting.py


        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient(self.snap_ip)
        time.sleep(self.wait_for_connect_time_in_seconds)
        print( 'connected to FPGA ',fpga,', with est clock',fpga.est_brd_clk())

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

        print( 'Initial RMS of ADC 1 ',rms1)
        print( 'Initial RMS of ADC 2 ',rms2)
        print( 'Initial RMS of ADC 3 ',rms3)
        print( 'Initial RMS of ADC 4 ',rms4)

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

            print( 'RMS of ADC 1 ',rms1)
            print( 'RMS of ADC 2 ',rms2)
            print( 'RMS of ADC 3 ',rms3)
            print( 'RMS of ADC 4 ',rms4)


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


    def initialise(self):
        """ Initialize the SNAP
        """

        # TODO: check needed  parameters have been set.
        
        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient(self.snap_ip)
        time.sleep(wait_for_connect_time_in_seconds)
        print( 'connected to FPGA ',fpga,', with est clock',fpga.est_brd_clk())

        # 2^12-1 is the largest shift
        fpga.write_int('fft_shift',self.fft_shift)
        time.sleep(0.1)


        # TODO: What is this used for???
        fpga.write_int('snap_index',self.snap_index) # SNAP-1
        time.sleep(0.1)


        # TODO: magic number
        fpga.write_int('sel1',2)
        time.sleep(0.1)
        # TODO: magic number: what is 18000?
        fpga.write_int('coeff1',18000)
        time.sleep(0.1)

        # TODO: config10g also connects to the fpga. Where should this be done?
        #       should config10g be a private method?
        self.config10g()
        self.initialized = True


    def set_delays(self):

        # connect to FPGAs
        f1 = corr.katcp_wrapper.FpgaClient(self.snap_ip)
        time.sleep(2)
        print( 'connected to FPGA ',f1,', with est clock',f1.est_brd_clk())

        # read delays
        # TODO: move file to config. would be better to move these into
        #       speparate files, one for each snap
        dA, dB = np.loadtxt('/mnt/nfs/runtime/delays.dat').transpose()

        # TODO: magic numbers
        sA = ((dA-np.min(dA))/4e-3).astype('int')+5
        sB = ((dB-np.min(dB))/4e-3).astype('int')+5

        print( 'Read delays (microsec), and converting to (samples):')
        for i in np.arange(10):
            print( dA[i],dB[i],sA[i],sB[i])

        f1.write_int('del1',sA[2*self.snap_index]) # 0
        time.sleep(0.05)
        f1.write_int('del2',sA[2*self.snap_index])
        time.sleep(0.05)
        f1.write_int('del3',sB[2*self.snap_index])
        time.sleep(0.05)
        f1.write_int('del4',sB[2*self.snap_index])
        time.sleep(0.05)
        f1.write_int('del5',sA[2*self.snap_index + 1]) # 1
        time.sleep(0.05)
        f1.write_int('del6',sA[2*self.snap_index + 1])
        time.sleep(0.05)
        f1.write_int('del7',sB[2*self.snap_index + 1])
        time.sleep(0.05)
        f1.write_int('del8',sB[2*self.snap_index + 1])
        time.sleep(0.05)

        print( 'Set all delays')

    def reg_arm_single(self):


        f2 = corr.katcp_wrapper.FpgaClient(self.snap_ip)
        time.sleep(0.1)
        print( 'connected to FPGA',f2,', with est clock',f2.est_brd_clk())

        # TODO: magic numbers
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
        print( 'Pausing until',now+delt)
        delt2 = datetime.timedelta(hours=7,seconds=1)
        myt = (now+delt+delt2).isoformat()
        t = Time(myt,format='isot',scale='utc')
        # TODO: move filename to config file
        f = open("/mnt/nfs/runtime/UTC_START.txt","w")
        f.write('{0}\n'.format(t.mjd))
        f.write('{0}\n'.format(myt))
        f.close()

        pause.until(now+delt)
        time.sleep(0.2)    
        f2.write_int('reg_arm',1)
        time.sleep(0.01)
        print( 'Synced to NTP second')
        time.sleep(2)
        f2.write_int('eth_ctrl',1);
        time.sleep(0.1)
        f2.write_int('eth_ctrl',0);
        time.sleep(0.1)
        f2.write_int('eth_ctrl',2);


    def reg_arm(self):

        f1 = corr.katcp_wrapper.FpgaClient(self.snap_ip)
        # TODO: not waiting 2 seconds here. Why?
        time.sleep(0.1)
        print( 'connected to FPGA 1',f1,', with est clock',f1.est_brd_clk())

        f1.write_int('reg_arm',0)
        # time.sleep(0.1)

        # jonathon edit force_sync
        f1.write_int('force_sync',2)
        # time.sleep(0.1)
        f1.write_int('force_sync',0)
        # time.sleep(0.1)

        f1.write_int('eth_ctrl',1);
        # time.sleep(0.1)
        f1.write_int('eth_ctrl',0);
        f1.write_int('eth1_ctrl',0);
        # time.sleep(0.1)
        f1.write_int('eth_ctrl',2);
        f1.write_int('eth1_ctrl',2);
        # time.sleep(0.1)

        # sync to 2-and-a-bit seconds from now
        now = datetime.datetime.now()
        micr = now.microsecond
        delt = datetime.timedelta(seconds=3,microseconds=1000000-micr)
        print( 'Pausing until',now+delt)
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
        print( 'Synced to NTP second')
        time.sleep(2)
        #
        f1.write_int('eth_ctrl',1);
        time.sleep(0.1)
        f1.write_int('eth_ctrl',0);
        time.sleep(0.1)
        f1.write_int('eth_ctrl',2);

        time.sleep(0.5)
        print( 'RAW DATA SW STATUS',bin(f1.read_int('eth_sw_status')))

    def help(self):

        print( 'dsaX_config_10g.py <SNAP> -prog -adc <cal/not> -init -arm -scale <sel1> <coeff1> -check_scale -check_spectra <nsnap> -monitor_spectra <nsnap> -rawlevs -delset -cbp')
        sys.exit()

    def checkbp(self):


        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient(self.snap_ip)
        time.sleep(wait_for_connect_time_in_seconds)
        print( 'connected to FPGA ',fpga,', with est clock',fpga.est_brd_clk())

        get=1

        print( 'Getting data')

        if get:
            # os.system('calc_coefficients -ip 10.10.5.1 -port 4011 -server snap1')
            # TODO: what is snap1 used for
            cmd = 'calc_coefficients -ip {} -port {} -server snap{}'. \
            format(self.dest_ip_dsa[0], self.dest_port, self.snap_index + 1)
            os.system(cmd)
            time.sleep(2)
        # TODO: move filename to config
        #c1,c2,c3,c4 = np.loadtxt('/mnt/nfs/runtime/snap1_coeffs.dat').transpose()
        c1,c2,c3,c4 = np.loadtxt(self.snap_coeffs_fn).transpose()

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

    def rawlevels(self,get):

        rmsval = 1.
        print( 'Setting 4-bit rms to ',rmsval)


        # connect to FPGA
        fpga = corr.katcp_wrapper.FpgaClient(self.snap_ip)
        time.sleep(wait_for_connect_time_in_seconds)
        print( 'connected to FPGA ',fpga,', with est clock',fpga.est_brd_clk())

        # write initial coefficients
        coeff = 2**14
        coeffs = np.ones(2048,'I')*coeff
        write_coeffs = struct.pack('>2048I',*coeffs)
        fpga.write('eq_0_coeffs',write_coeffs);
        fpga.write('eq_1_coeffs',write_coeffs);
        fpga.write('eq_2_coeffs',write_coeffs);
        fpga.write('eq_3_coeffs',write_coeffs);

        print( 'Getting data')

        if get:
            #os.system('/mnt/nfs/code/calc_coefficients -ip 10.10.5.1 -port 4011 -server snap1')
            cmd = '/mnt/nfs/code/calc_coefficients -ip {} -port {} -server snap{}'.\
            format(self.dest_ip[0], self.dest_port, self.snap_index+1)
            if self.calc_coeff_host != 'local':
                cmd = "ssh user@{} {}".format(self.calc_coeff_host, cmd)
            os.system(cmd)
            time.sleep(2)
        # TODO: move filename to config
        #c1,c2,c3,c4 = np.loadtxt('/mnt/nfs/runtime/snap1_coeffs.dat').transpose()
        c1,c2,c3,c4 = np.loadtxt(self.snap_coeffs_fn).transpose()

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

    def prog(self):
        self.adc16['host'] = self.snap_ip
        my_adc16 = ADC16(**self.adc16)
        my_adc16.calibrate()
        self.programmed = True

    # adc histograms
    def adc(self, cal_adc):
        #adchist(SNAP,cal_adc)
        adchist(cal_adc)

    def process(self, cmd):
        """Convert etcd commands local commands.

        :param cmd: etcd value which is a dictionary 'Cmd' as the key
        :type: Dictionary
        """

        command = cmd['Cmd']
        command in self.known_commands and self.known_commands[command]

    def get_monitor_data(self):
        """ Return monitor data in JSON format
        """

        utc = pytz.UTC
        mon_data = {}
        time = datetime.datetime.utcnow(). \
        replace(tzinfo=utc).isoformat()
        mon_data['time'] = time
        mon_data['snap_num'] = self.snap_number
        mon_data['ip'] = self.snap_ip
        mon_data['programmed'] = self.programmed
        mon_data['initialized'] = self.initialized

        try:
            md_json = json.dumps(mon_data)
        except ValueError:
            print("get_monitor_data(): JSON encode error. Check JSON."
                  "mon_data = {}".format(mon_data), 'ERR')
        return md_json
