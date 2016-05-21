# -*- coding: utf-8 -*-
"""
Test the base familysearch module contained in __init__.py
"""
# import system modules
from __future__ import print_function
import json
try:
    from urllib import request
except ImportError:
    import urllib2 as request

# import util module to enable easier testing
from test import util

# import familysearch module
import familysearch

class TestFamilySearch(util.FSTemplateTest):
    """Test the base familysearch module contained in __init__.py"""

    def runTest(self):
        self.setUp()
        self.test_base_fs_creation()
        self.tearDown()

    # setup
    def setUp(self):
        util.FSTemplateTest.setUp(self)
        self.agent = 'ClientApp/1.0'

    # teardown
    def tearDown(self):
        util.FSTemplateTest.tearDown(self)

    def test_base_fs_creation(self):
        fs = familysearch.FamilySearch(self.agent, self.devkey)
        self.assertTrue(fs.base == 'https://sandbox.familysearch.org')
        print("Base is correct.")
        self.assertTrue(fs.key == self.devkey)
        print("Key is correct.")
        self.assertTrue(isinstance(fs.opener, request.OpenerDirector))
        print("HTTP opener works.")
        self.assertTrue(fs.access_token == None)
        print("Access token works.")
