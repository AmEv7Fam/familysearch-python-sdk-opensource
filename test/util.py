# -*- coding: utf-8 -*-
"""Utilities to assist in testing."""

# import system modules
import inspect
import os
import sys
import unittest

MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.split(MODULE_PATH)[0]
CONFIG = 'config.ini'
sys.path.append(BASE_PATH)

# ConfigParser is renamed in Python 3 to configparser
try:
    # Python 3
    import configparser
except ImportError as ex:
    # Python 2
    import ConfigParser as configparser


def get_config(section='fsTest'):
    """Get the configuration for the test program."""
    config_path = os.path.join(MODULE_PATH, CONFIG)
    print(config_path)
    config = configparser.ConfigParser()
    config.read(config_path)
    return dict(config[section])


class FSTemplateTest(unittest.TestCase):
    """FSTemplateTest is the base class for familysearch tests.
    """
    # common setup
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.config = get_config()
        self.user = self.config.get('user', '')
        self.password = self.config.get('password', '')
        self.devkey = self.config.get('devkey', '')

    # common teardown
    def tearDown(self):
        unittest.TestCase.tearDown(self)
