# -*- coding: utf-8 -*-
"""Utilities to assist in testing."""

# import system modules
import inspect
import os
import sys
import unittest

CONFIG = 'config.ini'

# ConfigParser is renamed in Python 3 to configparser
try:
    # Python 3
    import configparser
except ImportError:
    # Python 2
    import ConfigParser as configparser


def get_config():
    """Get the configuration for the test program."""
    config_path = os.path.dirname(os.path.abspath(sys.argv[0])) + CONFIG
    config = configparser.ConfigParser()
    config.read(config_path)
    return config

class FSTemplateTest(unittest.TestCase):
    """FSTemplateTest is the base class for familysearch tests.
    """
    # common setup
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.config = get_config()
        try:
            #Python 2
            self.user = self.config.get('fsTest', 'user')
            self.password = self.config.get('fsTest', 'password')
            self.devkey = self.config.get('fsTest', 'devkey')                
        except AttributeError:
            # Python 3
            self.devkey = self.config["fsTest"]["devkey"]
            self.username = self.config["fsTest"]["username"]
            self.username = self.config["fsTest"]["password"]

    # common teardown
    def tearDown(self):
        unittest.TestCase.tearDown(self)
