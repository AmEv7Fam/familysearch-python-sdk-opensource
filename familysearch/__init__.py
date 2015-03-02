# For PyLint users:
# I'll get back to you to the recommeneded command.
r"""This is a WIP, unofficial SDK for accessing
the FamilySearch API.
Currently designed to support Python 3.2+ and 2.6+.

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


# FamilySearch imports

from .authentication import Authentication
from .authorities import Authorities
from .changeHistory import ChangeHistory
from .discovery import Discovery
from .discussions import Discussions
from .memories import Memories
from .ordinances import Ordinances
from .parentsAndChildren import ParentsAndChildren
from .pedigree import Pedigree
from .person import Person
from .places import Places
from .records import Records
from .searchAndMatch import SearchAndMatch
from .sources import Sources
from .spouses import Spouses
from .user import User
from .utilities import Utilities
from .vocabularies import Vocabularies

# Magic

__version__ = '0.75'

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

class FamilySearch(Authentication, Authorities, ChangeHistory, Discovery,
                   Discussions, Memories, Ordinances, ParentsAndChildren,
                   Pedigree, Person, Places, Records, SearchAndMatch,
                   Sources, Spouses, User, Utilities, Vocabularies):
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

        Authentication.__init__()
        Authorities.__init__()
        ChangeHistory.__init__()
        Discovery.__init__()
        Discussions.__init__()
        Memories.__init__()
        Ordinances.__init__()
        ParentsAndChildren.__init__()
        Pedigree.__init__()
        Person.__init__()
        Places.__init__()
        Records.__init__()
        SearchAndMatch.__init__()
        Sources.__init__()
        Spouses.__init__()
        User.__init__()
        Utilities.__init__()
        Vocabularies.__init__()

        self.agent = '%s FSPySDK/%s' % (agent, __version__)
        self.key = key
        self.session_id = session
        self.base = base
        self.user_base = self.base + "/platform/users/"
        self.tree_base = self.base + "/platform/tree/"
        self.opener = build_opener()
        self.logged_in = bool(self.session_id)

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
        if data:
            if not nojson:
                data = json.dumps(data)
            data = data.encode('utf-8')
        request = Request(url, data, headers, method=method)
        if not nojson:
            if method is not "GET":
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
        if response and not nojson:
            response = json.loads(response)
        return {"response": response, "headers": headers}

    # These are really just front-ends for _request,
    # with the name matching the method.
    def get(self, url, data=None, headers=None, nojson=False):
        """HTTP GET request"""
        return self._fs2py(self._request(
            url, data, headers, "GET", nojson), nojson)

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