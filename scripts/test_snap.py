""" Test reading snapConfig file
"""
import unittest
import snap_util as su


class TestSnap(unittest.TestCase):
    """ This class applies unit tests.
    """

    def __init__(self, *args, **kwargs):
        """ C-tor. Assign variables used in more than one test
        """

        super(TestSnap, self).__init__(*args, **kwargs)

        self.snap_config = {'fft_shift_noise': 1023, 'fpga_bof': 'dsa_10gv11s.bof', 'adc_samples_per_spectra': 8192, 'utc_start_filename': '/mnt/nfs/runtime/UTC_START.txt', 'snap': {1: {'dest': [{'ip': '10.10.5.1', 'mac': '24:8a:07:5d:80:71', 'port': 4011}, {'ip': '10.10.3.1', 'mac': '24:8a:07:5d:7e:41', 'port': 4011}], 'src': [{'ip_base': '10.10.5.2', 'port': 4002}, {'ip_base': '10.10.3.2', 'port': 4002}], 'adc_gain': 5, 'ip': '10.10.1.2', 'adc_demux': 2, 'coeff_filename': '/mnt/nfs/runtime/snap1_coeffs.dat'}, 2: {'dest': [{'ip': '10.10.6.1', 'mac': '24:8a:07:5d:7e:61', 'port': 4011}, {'ip': '10.10.3.1', 'mac': '24:8a:07:5d:7e:41', 'port': 4012}], 'src': [{'ip_base': '10.10.6.2', 'port': 4002}, {'ip_base': '10.10.3.3', 'port': 4003}], 'adc_gain': 5, 'ip': '10.10.1.3', 'adc_demux': 2, 'coeff_filename': '/mnt/nfs/runtime/snap2_coeffs.dat'}, 3: {'dest': [{'ip': '10.10.7.1', 'mac': '7c:fe:90:19:f3:91', 'port': 4011}, {'ip': '10.10.3.1', 'mac': '24:8a:07:5d:7e:41', 'port': 4013}], 'src': [{'ip_base': '10.10.7.2', 'port': 4002}, {'ip_base': '10.10.3.4', 'port': 4004}], 'adc_gain': 5, 'ip': '10.10.1.4', 'adc_demux': 2, 'coeff_filename': '/mnt/nfs/runtime/snap3_coeffs.dat'}, 4: {'dest': [{'ip': '10.10.8.1', 'mac': '7c:fe:90:19:f3:81', 'port': 4011}, {'ip': '10.10.3.1', 'mac': '24:8a:07:5d:7e:41', 'port': 4014}], 'src': [{'ip_base': '10.10.8.2', 'port': 4002}, {'ip_base': '10.10.3.5', 'port': 4005}], 'adc_gain': 5, 'ip': '10.10.1.5', 'adc_demux': 2, 'coeff_filename': '/mnt/nfs/runtime/snap4_coeffs.dat'}, 5: {'dest': [{'ip': '10.10.9.1', 'mac': '7c:fe:90:1a:1e:91', 'port': 4011}, {'ip': '10.10.3.1', 'mac': '24:8a:07:5d:7e:41', 'port': 4015}], 'src': [{'ip_base': '10.10.9.2', 'port': 4002}, {'ip_base': '10.10.3.6', 'port': 4006}], 'adc_gain': 5, 'ip': '10.10.1.6', 'adc_demux': 2, 'coeff_filename': '/mnt/nfs/runtime/snap5_coeffs.dat'}}, 'delay_filename': '/mnt/nfs/runtime/delays.dat', 'channels_per_sideband': 1024}

        self.src_ip_base0 = ['0.0.0.0',
                             '10.10.5.2',
                             '10.10.6.2',
                             '10.10.7.2',
                             '10.10.8.2',
                             '10.10.9.2',
                             '0.0.0.1',  # for additional test cases
                             '0.0.1.0',
                             '0.1.0.0',
                             '1.0.0.0']
        self.src_ip_base0_bin = [0,
                                 168428802,
                                 168429058,
                                 168429314,
                                 168429570,
                                 168429826,
                                 1,
                                 256,
                                 65536,
                                 16777216]
        self.src_port_base0 = 4002
        self.src_ip_base1 = ['',
                             '10.10.3.2',
                             '10.10.3.3',
                             '10.10.3.4',
                             '10.10.3.5',
                             '10.10.3.6']
        self.src_port_base1 = [0,
                               4002,
                               4003,
                               4004,
                               4005,
                               4006]
        self.dest_mac_dsa = ['00:00:00:00:00:00',
                             '24:8a:07:5d:80:71',
                             '24:8a:07:5d:7e:61',
                             '7c:fe:90:19:f3:91',
                             '7c:fe:90:19:f3:81',
                             '7c:fe:90:1a:1e:91']
        self.dest_mac_dsa_bin = [0,
                                 40175247655025,
                                 40175247654497,
                                 137432781157265,
                                 137432781157249,
                                 137432781168273]

    def test_read_snap_config(self):
        """ Test reading in snapConfigTest.yml file
        """

        adc_gain = 5
        adc_demux = 2

        # index refers to SNAP number.
        ip_snap = ['',
                   '10.10.1.2',
                   '10.10.1.3',
                   '10.10.1.4',
                   '10.10.1.5',
                   '10.10.1.6']
        # IP_DSA = ['',
        #          '10.10.1.7',
        #          '10.10.1.8',
        #          '10.10.1.9',
        #          '10.10.1.10',
        #          '10.10.1.11']
        # MAC_DSA = ['',
        #           '0c:c4:7a:ab:94:c3',
        #           '0c:c4:7a:ab:94:cd',
        #           '0c:c4:7a:ab:94:c9',
        #           '0c:c4:7a:ab:94:c5',
        #           '0c:c4:7a:ab:94:c7']
        dest_ip_dsa = ['',
                       '10.10.5.1',  # dsamaser
                       '10.10.6.1',  # on dsa1
                       '10.10.7.1',  # on dsa2
                       '10.10.8.1',  # on dsa3
                       '10.10.9.1']  # on dsa4

        # destination common to all SNAPS
        dest_ip_dsa5 = '10.10.3.1'
        dest_mac_dsa5 = '24:8a:07:5d:7e:41'
        dest_port = 4011
        dest_port_dsa5 = ['',
                          4011,
                          4012,
                          4013,
                          4014,
                          4015]

        snap_config = su.read_yaml("snapConfigTest.yml")
        self.assertNotEqual(snap_config, None)
        self.assertEqual(snap_config, self.snap_config)
        self.assertEqual(snap_config['fft_shift_noise'], 1023)
        self.assertEqual(snap_config['fpga_bof'], 'dsa_10gv11s.bof')
        self.assertEqual(snap_config['adc_samples_per_spectra'], 8192)
        for snap_no, _ in snap_config['snap'].items():
            snap = snap_config['snap'][snap_no]
            self.assertEqual(snap['adc_gain'], adc_gain)
            self.assertEqual(snap['ip'], ip_snap[snap_no])
            self.assertEqual(snap['adc_demux'], adc_demux)
            self.assertEqual(snap['coeff_filename'],
                             '/mnt/nfs/runtime/snap{}_coeffs.dat'
                             .format(snap_no))
            for idx, dest in enumerate(snap['dest'], start=0):
                if idx == 0:
                    self.assertEqual(dest['ip'], dest_ip_dsa[snap_no])
                    self.assertEqual(dest['mac'], self.dest_mac_dsa[snap_no])
                    self.assertEqual(dest['port'], dest_port)
                elif idx == 1:
                    self.assertEqual(dest['ip'], dest_ip_dsa5)
                    self.assertEqual(dest['mac'], dest_mac_dsa5)
                    self.assertEqual(dest['port'], dest_port_dsa5[snap_no])
                else:
                    # catch when config is extended and no test case for it.
                    self.assertEqual(idx, 1)

            for idx, src in enumerate(snap['src'], start=0):
                if idx == 0:
                    self.assertEqual(src['ip_base'], self.src_ip_base0[snap_no])
                    self.assertEqual(src['port'], self.src_port_base0)
                elif idx == 1:
                    self.assertEqual(src['ip_base'], self.src_ip_base1[snap_no])
                    self.assertEqual(src['port'], self.src_port_base1[snap_no])
                else:
                    # catch when config is extended and no test case for it.
                    self.assertEqual(idx, 1)

    def test_fpga_encode_mac(self):
        """ test converting human readable MAC into binary
        """

        for idx, mac in enumerate(self.dest_mac_dsa, start=0):
            self.assertEqual(su.fpga_encode_mac(mac),
                             self.dest_mac_dsa_bin[idx])

    def test_fpga_encode_ip(self):
        """ test converting human readable IP into binary
        """

        for idx, ip_addr in enumerate(self.src_ip_base0, start=0):
            self.assertEqual(su.fpga_encode_ip(ip_addr),
                             self.src_ip_base0_bin[idx])


if __name__ == '__main__':
    unittest.main()
