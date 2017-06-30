# -*- coding: utf-8 -*-

from __future__ import print_function
from test.test_basefs import TestFamilySearch
from test.test_enhanced_request import TestEnhancedRequest

fs = TestFamilySearch()
fs.runTest()

# Removing until we can get it platform-independent...
er = TestEnhancedRequest()
er.runTest()
