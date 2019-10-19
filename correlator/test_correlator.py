""" Test correlator class
"""
import unittest
import json
from os.path import dirname
from os.path import realpath
import sys
TOP_OF_TREE = dirname(dirname(realpath(__file__)))
print(TOP_OF_TREE)
sys.path.append(TOP_OF_TREE + '/scripts')
import snap_util as su
from Correlator import Correlator


class TestCorrelator(unittest.TestCase):
    """ This class applies unit tests.
    """

    def __init__(self, *args, **kwargs):
        """ C-tor. Assign variables used in more than one test
        """

        super(TestCorrelator, self).__init__(*args, **kwargs)

        self.config = {'common': {'big_nbytes': 402653184, 'nbytes_many': 49152000, 'nbytes_many2': 943718400, 'nbytes_final': 42240000, 'nsamps': 49152, 'nwait': 63000, 'nn': 384, 'log_dir': '/mnt/nfs/runtime/tmplog', 'capture': {'cmd': '/usr/local/dsaX/bin/dsaX_correlator_udpdb_thread', 'port': 4011, 'filename': '/mnt/nfs/code/dsaX/src/correlator_header_dsaX.txt', 'k': 'caca', 'b': 1}, 'final': {'cmd': '/usr/local/dsaX/bin/dsaX_writevis', 'log': '/mnt/nfs/runtime/tmplog/final_log_', 'c': 13}, 'dbnic': {'cmd': '/usr/local/dsaX/bin/dsaX_dbnic'}, 'nicdb': {'cmd': '/usr/local/dsaX/bin/dsaX_nicdb'}, 'fanout': {'cmd': '/usr/local/dsaX/bin/dsaX_correlator_fanout', 'c': 2}, 'massager': {'cmd': '/usr/local/dsaX/bin/dsaX_fancy', 'c': 14}, 'cpscr': {'cmd': '/usr/local/dsaX/bin/cpscr.bash', 'log': '/mnt/nfs/runtime/tmplog/cpscr_log_'}, 'ar_cmd': '/usr/local/dsaX/bin/dsaX_single', 'ar': [{'k': 'adbd', 'o': 'bdad', 'c': 24}, {'k': 'adcd', 'o': 'bdcd', 'c': 25}, {'k': 'addd', 'o': 'bddd', 'c': 26}, {'k': 'aaaa', 'o': 'bbbb', 'c': 27}, {'k': 'aaba', 'o': 'bbab', 'c': 28}]}, 'machine': {'dsamaster': {'capture': {'ip': '10.10.5.1'}, 'dbnic_port': 7016, 'dbnic': [{'ip': '10.10.4.1', 'c': 3, 'k': 'dbda'}, {'ip': '10.10.4.2', 'c': 4, 'k': 'dcda'}, {'ip': '10.10.4.3', 'c': 5, 'k': 'ddda'}, {'ip': '10.10.4.4', 'c': 6, 'k': 'ebda'}, {'ip': '10.10.5.5', 'c': 7, 'k': 'ecda'}], 'nicdb': [{'ip': '10.10.4.1', 'port': 7016, 'c': 8, 'k': 'adbd'}, {'ip': '10.10.4.1', 'port': 7015, 'c': 9, 'k': 'adcd'}, {'ip': '10.10.4.1', 'port': 7014, 'c': 10, 'k': 'addd'}, {'ip': '10.10.4.1', 'port': 7013, 'c': 11, 'k': 'aaaa'}, {'ip': '10.10.4.1', 'port': 7012, 'c': 12, 'k': 'aaba'}], 'final': {'ip': '10.10.1.1', 'filename': '/home/user/data/run1/dsa0', 'o': 1487.27539}}, 'dsa1': {'capture': {'ip': '10.10.6.1'}, 'dbnic_port': 7015, 'dbnic': [{'ip': '10.10.4.1', 'c': 3, 'k': 'dbda'}, {'ip': '10.10.4.2', 'c': 4, 'k': 'dcda'}, {'ip': '10.10.4.3', 'c': 5, 'k': 'ddda'}, {'ip': '10.10.4.4', 'c': 6, 'k': 'ebda'}, {'ip': '10.10.4.5', 'c': 7, 'k': 'ecda'}], 'nicdb_ip': '10.10.4.2', 'nicdb': [{'port': 7016, 'c': 8, 'k': 'adbd'}, {'port': 7015, 'c': 9, 'k': 'adcd'}, {'port': 7014, 'c': 10, 'k': 'addd'}, {'port': 7013, 'c': 11, 'k': 'aaaa'}, {'port': 7012, 'c': 12, 'k': 'aaba'}], 'final': {'ip': '10.10.1.7', 'filename': '/home/user/data/run1/dsa1', 'o': 1456.75781}}, 'dsa2': {'capture': {'ip': '10.10.7.1'}, 'dbnic_port': 7014, 'dbnic': [{'ip': '10.10.4.1', 'c': 3, 'k': 'dbda'}, {'ip': '10.10.4.2', 'c': 4, 'k': 'dcda'}, {'ip': '10.10.4.3', 'c': 5, 'k': 'ddda'}, {'ip': '10.10.4.4', 'c': 6, 'k': 'ebda'}, {'ip': '10.10.4.5', 'c': 7, 'k': 'ecda'}], 'nicdb_ip': '10.10.4.3', 'nicdb': [{'port': 7016, 'c': 8, 'k': 'adbd'}, {'port': 7015, 'c': 9, 'k': 'adcd'}, {'port': 7014, 'c': 10, 'k': 'addd'}, {'port': 7013, 'c': 11, 'k': 'aaaa'}, {'port': 7012, 'c': 12, 'k': 'aaba'}], 'final': {'ip': '10.10.1.8', 'filename': '/home/user/data/run1/dsa2', 'o': 1426.24023}}, 'dsa3': {'capture': {'ip': '10.10.8.1'}, 'dbnic_port': 7013, 'dbnic': [{'ip': '10.10.4.1', 'c': 3, 'k': 'dbda'}, {'ip': '10.10.4.2', 'c': 4, 'k': 'dcda'}, {'ip': '10.10.4.3', 'c': 5, 'k': 'ddda'}, {'ip': '10.10.4.4', 'c': 6, 'k': 'ebda'}, {'ip': '10.10.4.5', 'c': 7, 'k': 'ecda'}], 'nicdb_ip': '10.10.4.4', 'nicdb': [{'port': 7016, 'c': 8, 'k': 'adbd'}, {'port': 7015, 'c': 9, 'k': 'adcd'}, {'port': 7014, 'c': 10, 'k': 'addd'}, {'port': 7013, 'c': 11, 'k': 'aaaa'}, {'port': 7012, 'c': 12, 'k': 'aaba'}], 'final': {'ip': '10.10.1.9', 'filename': '/home/user/data/run1/dsa3', 'o': 1395.72266}}, 'dsa4': {'capture': {'ip': '10.10.9.1'}, 'dbnic_port': 7012, 'dbnic': [{'ip': '10.10.4.1', 'c': 3, 'k': 'dbda'}, {'ip': '10.10.4.2', 'c': 4, 'k': 'dcda'}, {'ip': '10.10.4.3', 'c': 5, 'k': 'ddda'}, {'ip': '10.10.4.4', 'c': 6, 'k': 'ebda'}, {'ip': '10.10.4.5', 'c': 7, 'k': 'ecda'}], 'nicdb_ip': '10.10.4.4', 'nicdb': [{'port': 7016, 'c': 8, 'k': 'adbd'}, {'port': 7015, 'c': 9, 'k': 'adcd'}, {'port': 7014, 'c': 10, 'k': 'addd'}, {'port': 7013, 'c': 11, 'k': 'aaaa'}, {'port': 7012, 'c': 12, 'k': 'aaba'}], 'final': {'ip': '10.10.1.10', 'filename': '/home/user/data/run1/dsa4', 'o': 1365.20508}}}}

    def test_read_corr_config(self):
        """ Test reading in corrConfigTest.yml file
        """


        config = su.read_yaml("corrConfigTest.yml")
        # print(config)
        self.assertNotEqual(config, None)
        self.assertEqual(config, self.config)
        self.assertEqual(config['common']['big_nbytes'], 402653184)
        self.assertEqual(config['common']['nbytes_many'], 49152000)
        self.assertEqual(config['common']['nbytes_many2'], 943718400)
        self.assertEqual(config['common']['nbytes_many2'], 943718400)
        self.assertEqual(config['common']['nbytes_final'], 42240000)
        self.assertEqual(config['common']['nsamps'], 49152)
        self.assertEqual(config['common']['nwait'], 63000)
        self.assertEqual(config['common']['nn'], 384)
        self.assertEqual(config['common']['log_dir'],
                         '/mnt/nfs/runtime/tmplog')

    def test_corr_ctor(self):
        """ Test constructing Correlator
        """

        config = su.read_yaml("corrConfigTest.yml")
        machines = ['dsamaster', 'dsa1', 'dsa2', 'dsa3', 'dsa4']
        for mach_name in machines:
            corr = Correlator(mach_name,
                              config['machine'][mach_name],
                              config['common'])
            self.assertNotEqual(corr, None)

    def test_get_monitor_data(self):
        """ Test constructing Correlator
        """

        config = su.read_yaml("corrConfigTest.yml")
        machines = ['dsamaster', 'dsa1', 'dsa2', 'dsa3', 'dsa4']
        for idx, mach_name in enumerate(machines, start=5):
            corr = Correlator(mach_name,
                              config['machine'][mach_name],
                              config['common'])
            # get json encoded data
            md_json = corr.get_monitor_data()

            md = {}
            # convert back to dictionary for comparison
            md = json.loads(md_json)
            # print(md)
            self.assertNotEqual(md['time'], "")
            self.assertEqual(md['name'], mach_name)
            self.assertEqual(md['cap_ip'], '10.10.{}.1'.format(idx))
            self.assertEqual(md['running'], False)
            self.assertEqual(md['started_utc'], '1970-01-01T00:00:00+00:00')
            self.assertEqual(md['sim'], False)

    def test_log_filename(self):
        config = su.read_yaml("corrConfigTest.yml")
        mach_name = 'dsamaster'
        corr = Correlator(mach_name,
                          config['machine'][mach_name],
                          config['common'])
        log_root = config['common']['log_dir']
        fn = corr._cpscr_log_filename(log_root)
        # print(fn)
        self.assertEqual(fn, '/mnt/nfs/runtime/tmplog/cpscr_log_dsamaster.log')

        fn = corr._final_log_filename(log_root)
        self.assertEqual(fn, '/mnt/nfs/runtime/tmplog/final_log_dsamaster.log')

        fn = corr._massager_log_filename(log_root)
        self.assertEqual(fn, '/mnt/nfs/runtime/tmplog/massager_log_dsamaster.log')

        fn = corr._ar_log_filename(log_root, 1)
        self.assertEqual(fn, '/mnt/nfs/runtime/tmplog/ar1.log')

        fn = corr._ndb_log_filename(log_root, 1)
        self.assertEqual(fn, '/mnt/nfs/runtime/tmplog/ndb1_log_dsamaster.log')

        fn = corr._dbn_log_filename(log_root, 1)
        self.assertEqual(fn, '/mnt/nfs/runtime/tmplog/db1_log_dsamaster.log')

        fn = corr._fanout_log_filename(log_root)
        self.assertEqual(fn, '/mnt/nfs/runtime/tmplog/fanout_log_dsamaster.log')

        fn = corr._capture_log_filename(log_root)
        self.assertEqual(fn, '/mnt/nfs/runtime/tmplog/capture_log_dsamaster.log')
        
if __name__ == '__main__':
    unittest.main()
