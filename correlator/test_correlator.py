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

        self.config = {'machine': {'dsa1': {'nicdb_ip': '10.10.4.2', 'capture': {'ip': '10.10.6.1'}, 'dbnic': [{'ip': '10.10.4.1', 'c': 3, 'k': 'dbda'}, {'ip': '10.10.4.2', 'c': 4, 'k': 'dcda'}, {'ip': '10.10.4.3', 'c': 5, 'k': 'ddda'}, {'ip': '10.10.4.4', 'c': 6, 'k': 'ebda'}, {'ip': '10.10.4.5', 'c': 7, 'k': 'ecda'}], 'nicdb': [{'ip': '10.10.4.2', 'c': 8, 'port': 7016, 'k': 'adbd'}, {'ip': '10.10.4.2', 'c': 9, 'port': 7015, 'k': 'adcd'}, {'ip': '10.10.4.2', 'c': 10, 'port': 7014, 'k': 'addd'}, {'ip': '10.10.4.2', 'c': 11, 'port': 7013, 'k': 'aaaa'}, {'ip': '10.10.4.2', 'c': 12, 'port': 7012, 'k': 'aaba'}], 'dbnic_port': 7015, 'final': {'ip': '10.10.1.7', 'o': 1456.75781, 'filename': '/home/user/data/run1/dsa1'}}, 'dsa2': {'nicdb_ip': '10.10.4.3', 'capture': {'ip': '10.10.7.1'}, 'dbnic': [{'ip': '10.10.4.1', 'c': 3, 'k': 'dbda'}, {'ip': '10.10.4.2', 'c': 4, 'k': 'dcda'}, {'ip': '10.10.4.3', 'c': 5, 'k': 'ddda'}, {'ip': '10.10.4.4', 'c': 6, 'k': 'ebda'}, {'ip': '10.10.4.5', 'c': 7, 'k': 'ecda'}], 'nicdb': [{'ip': '10.10.4.3', 'c': 8, 'port': 7016, 'k': 'adbd'}, {'ip': '10.10.4.3', 'c': 9, 'port': 7015, 'k': 'adcd'}, {'ip': '10.10.4.3', 'c': 10, 'port': 7014, 'k': 'addd'}, {'ip': '10.10.4.3', 'c': 11, 'port': 7013, 'k': 'aaaa'}, {'ip': '10.10.4.3', 'c': 12, 'port': 7012, 'k': 'aaba'}], 'dbnic_port': 7014, 'final': {'ip': '10.10.1.8', 'o': 1426.24023, 'filename': '/home/user/data/run1/dsa2'}}, 'dsa3': {'nicdb_ip': '10.10.4.4', 'capture': {'ip': '10.10.8.1'}, 'dbnic': [{'ip': '10.10.4.1', 'c': 3, 'k': 'dbda'}, {'ip': '10.10.4.2', 'c': 4, 'k': 'dcda'}, {'ip': '10.10.4.3', 'c': 5, 'k': 'ddda'}, {'ip': '10.10.4.4', 'c': 6, 'k': 'ebda'}, {'ip': '10.10.4.5', 'c': 7, 'k': 'ecda'}], 'nicdb': [{'ip': '10.10.4.4', 'c': 8, 'port': 7016, 'k': 'adbd'}, {'ip': '10.10.4.4', 'c': 9, 'port': 7015, 'k': 'adcd'}, {'ip': '10.10.4.4', 'c': 10, 'port': 7014, 'k': 'addd'}, {'ip': '10.10.4.4', 'c': 11, 'port': 7013, 'k': 'aaaa'}, {'ip': '10.10.4.4', 'c': 12, 'port': 7012, 'k': 'aaba'}], 'dbnic_port': 7013, 'final': {'ip': '10.10.1.9', 'o': 1395.72266, 'filename': '/home/user/data/run1/dsa3'}}, 'dsa4': {'nicdb_ip': '10.10.4.5', 'capture': {'ip': '10.10.9.1'}, 'dbnic': [{'ip': '10.10.4.1', 'c': 3, 'k': 'dbda'}, {'ip': '10.10.4.2', 'c': 4, 'k': 'dcda'}, {'ip': '10.10.4.3', 'c': 5, 'k': 'ddda'}, {'ip': '10.10.4.4', 'c': 6, 'k': 'ebda'}, {'ip': '10.10.4.5', 'c': 7, 'k': 'ecda'}], 'nicdb': [{'ip': '10.10.4.5', 'c': 8, 'port': 7016, 'k': 'adbd'}, {'ip': '10.10.4.5', 'c': 9, 'port': 7015, 'k': 'adcd'}, {'ip': '10.10.4.5', 'c': 10, 'port': 7014, 'k': 'addd'}, {'ip': '10.10.4.5', 'c': 11, 'port': 7013, 'k': 'aaaa'}, {'ip': '10.10.4.5', 'c': 12, 'port': 7012, 'k': 'aaba'}], 'dbnic_port': 7012, 'final': {'ip': '10.10.1.10', 'o': 1365.20508, 'filename': '/home/user/data/run1/dsa4'}}, 'dsamaster': {'capture': {'ip': '10.10.5.1'}, 'dbnic': [{'ip': '10.10.4.1', 'c': 3, 'k': 'dbda'}, {'ip': '10.10.4.2', 'c': 4, 'k': 'dcda'}, {'ip': '10.10.4.3', 'c': 5, 'k': 'ddda'}, {'ip': '10.10.4.4', 'c': 6, 'k': 'ebda'}, {'ip': '10.10.4.5', 'c': 7, 'k': 'ecda'}], 'dbnic_port': 7016, 'final': {'ip': '10.10.1.1', 'o': 1487.27539, 'filename': '/home/user/data/run1/dsa0'}, 'nicdb': [{'ip': '10.10.4.1', 'c': 8, 'port': 7016, 'k': 'adbd'}, {'ip': '10.10.4.1', 'c': 9, 'port': 7015, 'k': 'adcd'}, {'ip': '10.10.4.1', 'c': 10, 'port': 7014, 'k': 'addd'}, {'ip': '10.10.4.1', 'c': 11, 'port': 7013, 'k': 'aaaa'}, {'ip': '10.10.4.1', 'c': 12, 'port': 7012, 'k': 'aaba'}]}}, 'common': {'buffer': [{'k': 'caca', 'b': 402653184, 'c': 0, 'n': 8}, {'k': 'dbda', 'b': 49152000, 'c': 0, 'n': 4}, {'k': 'dcda', 'b': 49152000, 'c': 0, 'n': 4}, {'k': 'ddda', 'b': 49152000, 'c': 0, 'n': 4}, {'k': 'ebda', 'b': 49152000, 'c': 0, 'n': 4}, {'k': 'ecda', 'b': 49152000, 'c': 0, 'n': 4}, {'k': 'adbd', 'b': 49152000, 'c': 1, 'n': 4}, {'k': 'adcd', 'b': 49152000, 'c': 1, 'n': 4}, {'k': 'addd', 'b': 49152000, 'c': 1, 'n': 4}, {'k': 'aaaa', 'b': 49152000, 'c': 1, 'n': 4}, {'k': 'aaba', 'b': 49152000, 'c': 1, 'n': 4}, {'k': 'bdad', 'b': 98304000, 'c': 1, 'n': 4}, {'k': 'bdcd', 'b': 98304000, 'c': 1, 'n': 4}, {'k': 'bddd', 'b': 98304000, 'c': 1, 'n': 4}, {'k': 'bbbb', 'b': 98304000, 'c': 1, 'n': 4}, {'k': 'bbab', 'b': 98304000, 'c': 1, 'n': 4}, {'k': 'eada', 'b': 42240000, 'c': 1, 'n': 4}], 'dbnic': {'cmd': '/usr/local/dsaX/bin/dsaX_dbnic'}, 'nsamps': 49152, 'massager': {'c': 14, 'cmd': '/usr/local/dsaX/bin/dsaX_fancy', 'log': '/mnt/nfs/runtime/tmplog/massager_log_'}, 'ar': [{'k': 'adbd', 'c': 24, 'o': 'bdad'}, {'k': 'adcd', 'c': 25, 'o': 'bdcd'}, {'k': 'addd', 'c': 26, 'o': 'bddd'}, {'k': 'aaaa', 'c': 27, 'o': 'bbbb'}, {'k': 'aaba', 'c': 28, 'o': 'bbab'}], 'cpscr': {'cmd': '/usr/local/dsaX/bin/cpscr.bash', 'log': '/mnt/nfs/runtime/tmplog/cpscr_log_'}, 'nbytes_many': 49152000, 'capture': {'k': 'caca', 'cmd': '/usr/local/dsaX/bin/dsaX_correlator_udpdb_thread', 'b': 1, 'port': 4011, 'filename': '/mnt/nfs/code/dsaX/src/correlator_header_dsaX.txt'}, 'nn': 384, 'ar_cmd': '/usr/local/dsaX/bin/dsaX_single', 'big_nbytes': 402653184, 'nwait': 63000, 'fanout': {'c': 2, 'cmd': '/usr/local/dsaX/bin/dsaX_correlator_fanout'}, 'log_dir': '/mnt/nfs/runtime/tmplog', 'nbytes_final': 42240000, 'nicdb': {'cmd': '/usr/local/dsaX/bin/dsaX_nicdb'}, 'nbytes_many2': 943718400, 'final': {'c': 13, 'cmd': '/usr/local/dsaX/bin/dsaX_writevis', 'log': '/mnt/nfs/runtime/tmplog/final_log_'}}}

    def test_read_corr_config(self):
        """ Test reading in corrConfigTest.yml file
        """


        config = su.read_yaml("corrConfigTest.yml")
        #print(config)
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
        cpscr_log_root = config['common']['cpscr']['log']
        fn = corr._cpscr_log_filename(cpscr_log_root)
        # print(fn)
        self.assertEqual(fn, '/mnt/nfs/runtime/tmplog/cpscr_log_dsamaster.log')

        final_log_root = config['common']['final']['log']
        fn = corr._final_log_filename(final_log_root)
        self.assertEqual(fn, '/mnt/nfs/runtime/tmplog/final_log_dsamaster.log')

        massager_log_root = config['common']['massager']['log']
        fn = corr._massager_log_filename(massager_log_root)
        self.assertEqual(fn, '/mnt/nfs/runtime/tmplog/massager_log_dsamaster.log')

        fn = corr._ar_log_filename(log_root, 1)
        self.assertEqual(fn, '/mnt/nfs/runtime/tmplog/ar1_log_dsamaster.log')

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
