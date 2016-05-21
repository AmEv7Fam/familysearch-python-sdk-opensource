# -*- coding: utf-8 -*-

"""
Test the EnhancedRequest object contained in __init__.py
"""

# import system modules
from __future__ import print_function, unicode_literals
import json
import pprint
# Python imports
try:
    # Python 3
    from urllib.request import(build_opener, urlopen)
    from urllib.error import HTTPError
    from urllib.parse import(urlsplit, urlunsplit, parse_qs, urlencode)
except ImportError:
    # Python 2
    from urllib import urlencode
    from urllib2 import(build_opener, HTTPError, urlopen)
    from urlparse import(urlsplit, urlunsplit, parse_qs)

# import util module to enable easier testing
from test import util

# import familysearch module
from familysearch import Request

BASE_TEST_URL = "http://httpbin.org"


class TestEnhancedRequest(util.FSTemplateTest):
    """Test the EnhancedRequest object contained in __init__.py"""

    def runTest(self):
        self.setUp()
        self.test_delete()
        self.test_get()
        self.test_head()
        self.test_options()
        self.test_post()
        self.test_put()
        self.tearDown()

    # setup
    def setUp(self):
        util.FSTemplateTest.setUp(self)
        self.base_url = BASE_TEST_URL

    # teardown
    def tearDown(self):
        util.FSTemplateTest.tearDown(self)

    @staticmethod
    def _hr():
        print("="*80)

    def _show_in_out(self, actual, expected, msg_actual, msg_expected):

        pp = pprint.PrettyPrinter(indent=2, width=120)

        if isinstance(expected, dict):
            print(msg_actual, type(actual), "...")
            pp.pprint(actual)
            print(msg_expected, type(expected), "...")
            pp.pprint(expected)

        elif isinstance(expected, list):
            print(msg_actual, type(actual), "...")
            pp.pprint(actual)
            print(msg_expected, type(expected), "...")
            pp.pprint(expected)
        else:
            print("actual:", type(actual), "expected:", type(expected))
            raise TypeError

        self._hr()

    def test_delete(self):
        expected = {
            'args': {},
            'form': {},
            'origin': '192.168.1.70',
            'headers': {
                # 'X-Request-Id': 'e4f0cb78-afc7-4617-aac1-a0c13fa746cc',
                'Accept-Encoding': 'identity',
                'User-Agent': 'Python-urllib/3.5',
                'Host': 'httpbin.org',
                # 'Connection': 'close',
            },
            'data': '',
            'files': {},
            'url': 'http://httpbin.org/delete',
            'json': None,
        }
        url = self.base_url + '/delete'
        request = Request(url, method='DELETE')
        response = urlopen(request)
        actual = json.loads(response.read().decode('utf-8'))
        self.assertTrue(actual)
        actual_keys = list(actual.keys())
        actual_keys.sort()
        expected_keys = list(expected.keys())
        expected_keys.sort()
        # self._hr()
        # self._show_in_out(actual_keys, expected_keys, "actual keys", "expected keys")
        self.assertTrue(actual_keys == expected_keys)
        # self._hr()
        # self._show_in_out(actual.get('headers', {}).keys(), expected['headers'].keys(), "actual[headers]", "expected[headers]")
        self.assertTrue(actual.get('headers', {}).keys() ==
                        expected['headers'].keys())

    def test_get(self):
        expected = {
            'args': {},
            'origin': '192.168.1.70',
            'headers': {
                # 'X-Request-Id': 'e4f0cb78-afc7-4617-aac1-a0c13fa746cc',
                'Accept-Encoding': 'identity',
                'User-Agent': 'Python-urllib/3.5',
                'Host': 'httpbin.org',
                # 'Connection': 'close',
            },
            'url': 'http://httpbin.org/get',
        }
        url = self.base_url + '/get'
        request = Request(url)
        response = urlopen(request)
        actual = json.loads(response.read().decode('utf-8'))
        self.assertTrue(actual)
        self.assertTrue(actual.keys() == expected.keys())
        self.assertTrue(actual.get('headers', {}).keys() ==
                        expected['headers'].keys())

    def test_head(self):
        expected = [
            ('access-control-allow-credentials', 'true'),
            ('access-control-allow-origin', '*'),
            ('content-length', '294'),
            ('content-type', 'application/json'),
            ('date', 'Thu, 18 Sep 2014 00:29:57 GMT'),
            ('server', 'gunicorn/18.0'),
            ('connection', 'Close')
        ]
        url = self.base_url + '/get'
        request = Request(url, method='HEAD')
        response = urlopen(request)
        # print("dir(response):", dir(response))
        # print("headers:", type(response.headers), response.headers.__class__)
        # print(response.headers.__class__, dir(response.headers))
        actual = response.headers
        self.assertTrue(actual)
        expected_keys = [k for k, v in expected]
        actual_keys = [k.lower() for k in actual.keys()]
        expected_keys.sort()
        actual_keys.sort()
        # self._hr()
        # self._show_in_out(actual_keys, expected_keys, "actual keys", "expected keys")
        self.assertTrue(actual_keys == expected_keys)

    def test_options(self):
        expected = [
            ('access-control-allow-credentials', 'true'),
            ('access-control-allow-methods', 'GET, POST, PUT, DELETE, PATCH, OPTIONS'),
            ('access-control-allow-origin', '*'),
            ('access-control-max-age', '3600'),
            ('allow', 'GET, HEAD, OPTIONS'),
            ('content-type', 'text/html; charset=utf-8'),
            ('date', 'Thu, 18 Sep 2014 00:29:57 GMT'),
            ('server', 'gunicorn/18.0'),
            ('content-length', '0'),
            ('connection', 'Close')
        ]
        url = self.base_url
        request = Request(url, method='OPTIONS')
        response = urlopen(request)
        actual = response.headers
        self.assertTrue(actual)
        expected_keys = [k for k, v in expected]
        actual_keys = [k.lower() for k in actual.keys()]
        expected_keys.sort()
        actual_keys.sort()
        # self._hr()
        # self._show_in_out(actual_keys, expected_keys, "actual keys", "expected keys")
        self.assertTrue(actual_keys == expected_keys)

    def test_post(self):
        expected = {
            'args': {},
            'form': {'spam': '1', 'eggs': '2', 'bacon': '3'},
            'origin': '192.168.1.70',
            'headers': {
                'Content-Length': '21',
                # 'X-Request-Id': 'e4f0cb78-afc7-4617-aac1-a0c13fa746cc',
                'Accept-Encoding': 'identity',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Python-urllib/3.5',
                'Host': 'httpbin.org',
                # 'Connection': 'close',
            },
            'data': '',
            'files': {},
            'url': 'http://httpbin.org/delete',
            'json': None,
        }
        url = self.base_url + '/post'
        data_dict = {'spam': 1, 'eggs': 2, 'bacon': 3}
        data = urlencode(data_dict)
        data = data.encode('utf-8')
        request = Request(url, data)
        response = urlopen(request)
        actual = json.loads(response.read().decode('utf-8'))
        self.assertTrue(actual)
        actual_keys = list(actual.keys())
        expected_keys = list(expected.keys())
        actual_keys.sort()
        expected_keys.sort()
        # self._hr()
        # self._show_in_out(actual_keys, expected_keys, "actual keys", "expected keys")
        self.assertTrue(actual_keys == expected_keys)
        akeys = list(actual.get('headers', {}).keys())
        ekeys = list(expected['headers'].keys())
        akeys.sort()
        ekeys.sort()
        # self._hr()
        # self._show_in_out(akeys, ekeys, "actual head keys", "expected head keys")
        self.assertTrue(akeys == ekeys)
        self.assertTrue(actual.get('form', None) == expected['form'])

    def test_put(self):
        expected = {
            'args': {},
            'form': {},
            'origin': '192.168.1.70',
            'headers': {
                'Content-Length': '0',
                # 'X-Request-Id': 'e4f0cb78-afc7-4617-aac1-a0c13fa746cc',
                'Accept-Encoding': 'identity',
                'User-Agent': 'Python-urllib/3.5',
                'Host': 'httpbin.org',
                # 'Connection': 'close'
            },
            'data': '',
            'files': {},
            'url': 'http://httpbin.org/delete',
            'json': None
        }
        url = self.base_url + '/put'
        request = Request(url, method='PUT')
        response = urlopen(request)
        actual = json.loads(response.read().decode('utf-8'))
        self.assertTrue(actual)
        akeys = list(actual.keys())
        ekeys = list(expected.keys())
        akeys.sort()
        ekeys.sort()
        self._hr()
        self._show_in_out(akeys, ekeys, "actual keys", "expected keys")
        self.assertTrue(akeys == ekeys)
        akeys = list(actual["headers"].keys())
        ekeys = list(expected["headers"].keys())
        akeys.sort()
        ekeys.sort()
        self._hr()
        self._show_in_out(akeys, ekeys, "actual head keys", "expected head keys")
        self.assertTrue(akeys == ekeys)
