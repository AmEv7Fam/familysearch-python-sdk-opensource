# -*- coding: utf-8 -*-
"""
Test the EnhancedRequest object contained in __init__.py
"""
# import system modules
import json
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
    # setup
    def setUp(self):
        util.FSTemplateTest.setUp(self)
        self.base_url = BASE_TEST_URL


    # teardown
    def tearDown(self):
        util.FSTemplateTest.tearDown(self)


    def test_delete(self):
        expected = {
            'args': {},
            'form': {},
            'origin': '192.168.1.1',
            'headers': {
                'X-Request-Id': 'e4f0cb78-afc7-4617-aac1-a0c13fa746cc',
                'Accept-Encoding': 'identity',
                'User-Agent': 'Python-urllib/3.4',
                'Host': 'httpbin.org',
                'Connection': 'close'
            },
            'data': '',
            'files': {},
            'url': 'http://httpbin.org/delete',
            'json': None
        }
        url = self.base_url + '/delete'
        request = Request(url, method='DELETE')
        response = urlopen(request)
        actual = json.loads(response.read().decode('utf-8'))
        self.assertTrue(actual)
        self.assertTrue(actual.keys() == expected.keys())
        self.assertTrue(actual.get('headers', {}).keys() ==
            expected['headers'].keys())


    def test_get(self):
        expected = {
            'args': {},
            'origin': '192.168.1.1',
            'headers': {
                'X-Request-Id': 'e4f0cb78-afc7-4617-aac1-a0c13fa746cc',
                'Accept-Encoding': 'identity',
                'User-Agent': 'Python-urllib/3.4',
                'Host': 'httpbin.org',
                'Connection': 'close'
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
            ('Access-Control-Allow-Credentials', 'true'),
            ('Access-Control-Allow-Origin', '*'),
            ('Content-length', '294'),
            ('Content-Type', 'application/json'),
            ('Date', 'Thu, 18 Sep 2014 00:29:57 GMT'),
            ('Server', 'gunicorn/18.0'),
            ('Connection', 'Close')
        ]
        url = self.base_url + '/get'
        request = Request(url, method='HEAD')
        response = urlopen(request)
        actual = response.getheaders()
        expected_fields = [value[0] for value in expected]
        actual_fields = [value[0] for value in actual]
        self.assertTrue(actual)
        self.assertTrue(actual_fields == expected_fields)


    def test_options(self):
        expected = [
            ('Access-Control-Allow-Credentials', 'true'),
            ('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, PATCH, OPTIONS'),
            ('Access-Control-Allow-Origin', '*'),
            ('Access-Control-Max-Age', '3600'),
            ('Allow', 'GET, HEAD, OPTIONS'),
            ('Content-Type', 'text/html; charset=utf-8'),
            ('Date', 'Thu, 18 Sep 2014 00:29:57 GMT'),
            ('Server', 'gunicorn/18.0'),
            ('Content-Length', '0'),
            ('Connection', 'Close')
        ]
        url = self.base_url
        request = Request(url, method='OPTIONS')
        response = urlopen(request)
        actual = response.getheaders()
        expected_fields = [value[0] for value in expected]
        actual_fields = [value[0] for value in actual]
        self.assertTrue(actual)
        self.assertTrue(actual_fields == expected_fields)


    def test_post(self):
        expected = {
            'args': {},
            'form': {'spam': '1', 'eggs': '2', 'bacon': '3'},
            'origin': '192.168.1.1',
            'headers': {
                'Content-Length': '21',
                'X-Request-Id': 'e4f0cb78-afc7-4617-aac1-a0c13fa746cc',
                'Accept-Encoding': 'identity',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Python-urllib/3.4',
                'Host': 'httpbin.org',
                'Connection': 'close'
            },
            'data': '',
            'files': {},
            'url': 'http://httpbin.org/delete',
            'json': None
        }
        url = self.base_url + '/post'
        data_dict = {'spam': 1, 'eggs': 2, 'bacon': 3}
        data = urlencode(data_dict)
        data = data.encode('utf-8')
        request = Request(url, data)
        response = urlopen(request)
        actual = json.loads(response.read().decode('utf-8'))
        self.assertTrue(actual)
        self.assertTrue(actual.keys() == expected.keys())
        self.assertTrue(actual.get('headers', {}).keys() ==
            expected['headers'].keys())
        self.assertTrue(actual.get('form', None) == expected['form'])


    def test_put(self):
        expected = {
            'args': {},
            'form': {},
            'origin': '192.168.1.1',
            'headers': {
                'Content-Length': '0',
                'X-Request-Id': 'e4f0cb78-afc7-4617-aac1-a0c13fa746cc',
                'Accept-Encoding': 'identity',
                'User-Agent': 'Python-urllib/3.4',
                'Host': 'httpbin.org',
                'Connection': 'close'
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
        self.assertTrue(actual.keys() == expected.keys())
        self.assertTrue(actual.get('headers', {}).keys() ==
            expected['headers'].keys())

