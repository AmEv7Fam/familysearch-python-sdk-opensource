from test.test_basefs import TestFamilySearch
#from test.test_enhanced_request import TestEnhancedRequest

fs = TestFamilySearch()
fs.setUp()
fs.test_base_fs_creation()
fs.tearDown()

# Removing until we can get it platform-independent...
#er = TestEnhancedRequest()
#er.setUp()
#er.test_delete()
#er.test_head()
#er.test_options()
#er.test_post()
#er.test_put()
#er.tearDown()
