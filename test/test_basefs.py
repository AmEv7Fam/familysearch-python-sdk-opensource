# -*- coding: utf-8 -*-
"""
Test the base familysearch module contained in __init__.py
"""
# import system modules
import json
import urllib

# import util module to enable easier testing
from test import util

# import familysearch module
import familysearch

class TestFamilySearch(util.FSTemplateTest):
    """Test the base familysearch module contained in __init__.py"""
    # setup
    def setUp(self):
        util.FSTemplateTest.setUp(self)
        self.agent = 'ClientApp/1.0'

    # teardown
    def tearDown(self):
        util.FSTemplateTest.tearDown(self)

    def test_base_fs_creation(self):
        fs = familysearch.FamilySearch(self.agent, self.devkey)
        self.assertTrue(fs.agent == 'ClientApp/1.0 Python-FS-Stack/0.3pre')
        self.assertTrue(fs.base == 'sandbox.familysearch.org')
        self.assertTrue(fs.key == self.devkey)
        self.assertTrue(isinstance(fs.opener, urllib.request.OpenerDirector))
        self.assertTrue(fs.session_id == None)
        self.assertTrue(fs.tree_base == 'sandbox.familysearch.org/platform/tree/')
        self.assertTrue(fs.user_base == 'sandbox.familysearch.org/platform/users/')

