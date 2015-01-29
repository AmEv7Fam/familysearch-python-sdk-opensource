# For PyLint users:
# pylint familysearch disable=no-member, cyclic-import, import-error
# This is so PyLint shuts up about the function import system,
# and dual Python 2/3 compatibility.
r"""This is a WIP, unofficial SDK for accessing
the FamilySearch API. Based heavily on the official
JavaScript SDK
Currently designed to support Python 3 and 2.6-7.

A library to interact with the FamilySearch API

Licensed under the FamilySearch API License Agreement;
see the included LICENSE file for details.

Example usage:

from familysearch import FamilySearch

# Log in with Basic Authentication
fs = FamilySearch('ClientApp/1.0', 'app')
fs.login('username', 'password')

# Resume a previous session
fs = FamilySearch('ClientApp/1.0', app_key, session='session_id')

# Use the production system instead of the sandbox system
fs = FamilySearch('ClientApp/1.0', app_key, base='https://familysearch.org')

# Log out
fs.logout()
"""

# Python imports
try:
    # Python 3
    from urllib.request import Request as BaseRequest
    from urllib.request import(build_opener, urlopen)
    from urllib.error import HTTPError
    from urllib.parse import(urlsplit, urlunsplit, parse_qs, urlencode)
except ImportError:
    # Python 2
    from urllib import urlencode
    from urllib2 import Request as BaseRequest
    from urllib2 import(build_opener, HTTPError, urlopen)
    from urlparse import(urlsplit, urlunsplit, parse_qs)

import json
import time

__version__ = '0.5'

class Request(BaseRequest):
    """Add ability for the Request object to allow it to handle
    additional methods.
    """
    def __init__(self, *args, **kwargs):
        self._method = kwargs.pop('method', None)
        BaseRequest.__init__(self, *args, **kwargs)

    def get_method(self):
        """The Request object has been enhanced to handle PUT, DELETE, OPTIONS,
        and HEAD request methods.
        """
        if self._method:
            return self._method
        else:
            return BaseRequest.get_method(self)

class FSBase(object): pass
class FamilySearch(FSBase):
    """A FamilySearch API proxy
    The constructor must be called with a user-agent string and a developer key.
    A session ID and base URL are optional.
    Public methods:
    ...needs to be re-written...
    """

    def __init__(self, agent, key, session=None,
                 base='https://sandbox.familysearch.org'):
        """Instantiate a FamilySearch proxy object.

        Keyword arguments:
        agent -- User-agent string to use for requests
        key -- FamilySearch developer key
               (optional if reusing an existing session ID)
        session (optional) -- existing session ID to reuse
        base (optional) -- base URL for the API;
                           defaults to 'https://sandbox.familysearch.org'
        """
        self.agent = '%s Python-FS-Stack/%s' % (agent, __version__)
        self.key = key
        self.session_id = session
        self.base = base
        self.user_base = self.base + "/platform/users/"
        self.tree_base = self.base + "/platform/tree/"
        self.opener = build_opener()
        self.logged_in = bool(self.session_id)
        self.cookies = None

        for mixin in self.__class__.__bases__:
            mixin.__init__(self)

    def _request(self, url, data=None, headers=None, method=None, nojson=False):
        """
        Make a request to the FamilySearch API.

        Adds the User-Agent header and sets the response format to JSON.
        If the data argument is supplied, makes a POST request unless specified
        in the Method header.

        Returns a file-like object representing the response.
        """
        if headers is None:
            headers = {}
        if not nojson:
            if data:
                data = json.dumps(data)
                data = data.encode('utf-8')
        request = Request(url, data, headers, method=method)
        if not nojson:
            if data or method:
                request.add_header('Content-Type', 'application/x-fs-v1+json')
            else:
                request.add_header('Accept', 'application/json')
        if self.logged_in and not self.cookies:
            # Add sessionId parameter to url if cookie is not set
            request.add_header('Authorization', 'Bearer ' + self.session_id)
        request.add_header('User-Agent', self.agent)
        try:
            return self.opener.open(request)
        except HTTPError as error:
            eh = dict(error.headers)
            if error.code == 401:
                self.logged_in = False
            if error.code == 429:
                time.sleep(eh['Retry-after']/1000)
                return self._request(url, data, headers, method, nojson)
            raise

    def _add_subpath(self, url, subpath):
        """
        Add a subpath to the path component of the given URL.

        For example, adding sub to http://example.com/path?query
        becomes http://example.com/path/sub?query.

        """
        parts = urlsplit(url)
        path = parts[2] + '/' + subpath
        return urlunsplit((parts[0], parts[1], path, parts[3], parts[4]))

    def _add_query_params(self, url, params=None, **kw_params):
        """Add the specified query parameters to the given URL.
        Parameters can be passed either as a dictionary or as keyword arguments.
        """
        if params is None:
            params = {}
        parts = urlsplit(url)
        query_parts = parse_qs(parts[3])
        query_parts.update(params)
        query_parts.update(kw_params)
        query = urlencode(query_parts, True)
        return urlunsplit((parts[0], parts[1], parts[2], query, parts[4]))

    # Considering integrating directly into _request
    def _fs2py(self, response, nojson=False):
        """
        Take JSON from FamilySearch response, and allow Python to handle it.
        Also, inject headers into response.
        """
        headers = dict(response.info())
        response = response.read()
        response = response.decode("utf-8")
        if not nojson:
            response = json.loads(response)
        response["headers"] = headers
        return response

    # These are really just front-ends for _request,
    # with the name matching the method.
    def get(self, url, data=None, headers=None, nojson=False):
        """HTTP GET request"""
        return self._fs2py(self._request(
    url, data, headers, None, nojson), nojson)

    def post(self, url, data=None, headers=None, nojson=False):
        """HTTP POST request"""
        return self._fs2py(self._request(
    url, data, headers, "POST", nojson), nojson)

    def put(self, url, data=None, headers=None, nojson=False):
        """HTTP PUT request"""
        return self._fs2py(self._request(
    url, data, headers, "PUT", nojson), nojson)

    def head(self, url, data=None, headers=None, nojson=False):
        """HTTP HEAD request"""
        return self._fs2py(self._request(
    url, data, headers, "HEAD", nojson), nojson)

    def options(self, url, data=None, headers=None, nojson=False):
        """HTTP OPTIONS request"""
        return self._fs2py(self._request(
    url, data, headers, "OPTIONS", nojson), nojson)

    def delete(self, url, data=None, headers=None, nojson=False):
        """HTTP DELETE request"""
        return self._fs2py(self._request(
    url, data, headers, "DELETE", nojson), nojson)

# FamilySearch imports

# Sorted alphabetically, except Discovery, which is the Hypermedia class, which
# all other classes depend on.

from . import(discovery_, authentication_, authorities_, changeHistory_,
              discussions_, memories_, notes_, parentsAndChildren_, ordinances_, 
              pedigree_, person_, places_, records_, searchAndMatch_,
              sourceBox_, sources_, spouses_, user_, utilities_, vocabularies_)
