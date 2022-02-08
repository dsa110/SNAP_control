import logging
import os
import time
import socket
import yaml
import json
import helpers
import hashlib
import numpy as np
from casperfpga import utils

LOGGER = helpers.add_default_log_handlers(logging.getLogger(__name__))

class HeraCorrelator(object):
    def __init__(self, config=None, logger=LOGGER):
        """
        Instantiate a HeraCorrelator instance.
        optional inputs:
            config (str): Path to configuration file. If None, config will be grabbed from redis.
            logger (logging.Logger): Logging object this class will use.
        """
        self.logger = logger
        self.get_config(config)
        self.config_is_valid= self._verify_config()

    def get_config(self, config):
        """
        Parse a configuration file.
        inputs:
            config (str): Path to configuration file. If None, a configuration will be pulled from redis.
        """

        with open(config, 'r') as fp:
            self.config_str = fp.read()
            self.config_name = config
            self.config_hash = hashlib.md5(self.config_str).hexdigest()
            self.config_time = time.time()
            self.config_time_str = time.ctime(self.config_time)
        self.config = yaml.load(self.config_str)

    def _verify_config(self):
        """
        Do some basic sanity checking on the currently loaded config.
        Returns:
            Bool : True if tests pass, False otherwise.
        """
        test_passed = True
        # Check that there are only three antennas per board
        for fn,(host,params) in enumerate(self.config['fengines'].items()):
            if 'ants' in params.keys():
                if len(params['ants']) != 3: 
                    self.logger.warning("%s: Number of antennas is not 3!" % host)
                    test_passed = False
        # Check that there are only 48 channels per x-engine.
        for host,params in self.config['xengines'].items():
            if 'chan_range' in params.keys():
                chan_range= params['chan_range']
                chans = np.arange(chan_range[0], chan_range[1])
                if len(chans) > 384:
                    self.logger.warning("%s: Cannot process >384 channels." % host)
                    test_passed = False
        return test_passed

