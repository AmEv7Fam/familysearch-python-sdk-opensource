# Python imports

"""
A module implementing the Identity version 2 API module

Main class: Authentication, meant to be mixed-in to the FamilySearch class
"""

import random
import time
try:
    # Python 3
    from urllib.request import(build_opener, HTTPCookieProcessor)
    from urllib.parse import urlencode
except ImportError:
    # Python 2
    from urllib import urlencode
    from urllib2 import(build_opener, HTTPCookieProcessor)

import json

# Magic

def parse(input):
    """Parse specified file or string and return an Identity object created from it."""
    if hasattr(input, "read"):
        input = input.read()
        input = input.decode("utf-8")
    data = json.loads(input)
    return Identity(data)

class JSONBase:
    """Base class for all JSON-related objects"""
    def to_json(self):
        return json.dumps(self.to_json_dict())

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.to_json_dict())

    def __str__(self):
        return self.to_json()


class FSDict(dict):
    """Convenience class to access FamilySearch-style property lists as dictionaries

    For example,
        [{"name": "key1", "value": "value1"}, {"name": "key2", "value": "value2"}]
    converts to
        {"key1": "value1", "key2": "value2"}

    """

    def __init__(self, pairs=None):
        if isinstance(pairs, list) and all((isinstance(pair, dict) for pair in pairs)):
            dict.__init__(self)
            for pair in pairs:
                self[pair["name"]] = pair["value"]

    def to_json_array(self):
        return [{"name": key, "value": self[key]} for key in self]

class Identity(JSONBase):
    def __init__(self, o):
        if "statusCode" in o:
            self.statusCode = o["statusCode"]
        if "statusMessage" in o:
            self.statusMessage = o["statusMessage"]
        if "version" in o:
            self.version = o["version"]
        if "properties" in o:
            self.properties = FSDict(o["properties"])
        if "session" in o and o["session"]:
            self.session = Session(o["session"])

    def to_json_dict(self):
        d = {}
        if hasattr(self, "statusCode"):
            d["statusCode"] = self.statusCode
        if hasattr(self, "statusMessage"):
            d["statusMessage"] = self.statusMessage
        if hasattr(self, "version"):
            d["version"] = self.version
        if hasattr(self, "properties"):
            d["properties"] = self.properties.to_json_array()
        if hasattr(self, "session"):
            d["session"] = self.session.to_json_dict()
        return d

class Session(JSONBase):
    def __init__(self, o):
        if "id" in o:
            self.id = o["id"]
        if "type" in o:
            self.type = o["type"]

    def to_json_dict(self):
        d = {}
        if hasattr(self, "id"):
            d["id"] = self.id
        if hasattr(self, "type"):
            d["type"] = self.type
        return d

class Authentication(object):

    """
    A mix-in implementing the Identity version 2 endpoints
    """

    def __init__(self):
        """
        Set up the URLs for this IdentityV2 object.
        """
        self.identity_base = self.base + '/identity/v2/'

        self.oauth_secrets = dict()

        # Assume logged_in if session_id is set
        self.logged_in = bool(self.session_id)

        cookie_handler = HTTPCookieProcessor()
        self.cookies = cookie_handler.cookiejar
        self.opener = build_opener(cookie_handler)

    def login(self, username, password):
        """
        Log into FamilySearch using Basic Authentication.

        Web applications must use OAuth.

        """
        self.logged_in = False
        self.cookies.clear()
        url = self.identity_base + 'login'
        credentials = urlencode({'username': username,
                                 'password': password,
                                 'key': self.key,
                                 'dataFormat': 'application/json'})
        self.session_id = parse(self._request(url, credentials,)).session.id
        self.logged_in = True
        return self.session_id

    def logout(self):
        """
        Log the current session out of FamilySearch.
        """
        self.logged_in = False
        url = self.identity_base + 'logout'
        self._request(url)
        self.session_id = None
        self.cookies.clear()

    def session(self):
        """
        Keep the current session in an active state by sending an empty request.

        Calling this method is an easy way to turn a sessionId query parameter
        into a cookie without doing anything else.

        """
        url = self.identity_base + 'session'
        self.session_id = identity.parse(self._request(url)).session.id
        self.logged_in = True
        return self.session_id

    def request_token(self, callback_url='oob'):
        """
        Get a request token for step 1 of the OAuth login process.

        Returns a dictionary containing the OAuth response and stores the token
        and token secret, which are needed to get an access token (step 3).

        """
        self.logged_in = False
        self.cookies.clear()
        url = self.identity_properties['request.token.url']
        oauth_response = self._oauth_request(url, oauth_callback=callback_url)
        response = dict(urllib.parse.parse_qsl(oauth_response.read()))
        self.session_id = response['oauth_token']
        self.oauth_secrets[response['oauth_token']] = response['oauth_token_secret']
        return response

    def authorize(self, request_token=None, options={}, **kw_options):
        """
        Construct and return the User Authorization URL for step 2 of the OAuth login process.

        This URL should be loaded into the user's browser. It is the
        application's responsibility to receive the OAuth verifier from the
        callback URL (such as by running an HTTP server) or to provide a means
        for the user to enter the verifier into the application.

        """
        if not request_token:
            if self.session_id and self.session_id in self.oauth_secrets:
                # Use current session ID for oauth_token if it is set
                request_token = self.session_id
            else:
                # Otherwise, get a new request token and use it
                request_token = self.request_token()['oauth_token']
        # Add sessionId parameter to authorize.url
        url = self.identity_properties['authorize.url']
        url = self._add_query_params(url, sessionId=request_token)
        if options or kw_options:
            url = self._add_query_params(url, options, **kw_options)
        return url

    def access_token(self, verifier, request_token=None, token_secret=None):
        """
        Get an access token (session ID) to complete step 3 of the OAuth login process.

        Returns a dictionary containing the OAuth response and stores the token
        as the session ID to be used by future requests.

        """
        if not request_token and self.session_id:
            # Use current session ID for oauth_token if it is set
            request_token = self.session_id
        if not token_secret and request_token in self.oauth_secrets:
            # Use saved secret for oauth_token_secret if it is set
            token_secret = self.oauth_secrets[request_token]
        url = self.identity_properties['access.token.url']
        oauth_response = self._oauth_request(url, token_secret,
                                             oauth_token=request_token,
                                             oauth_verifier=verifier)
        response = dict(urllib.parse.parse_qsl(oauth_response.read()))
        if self.session_id in self.oauth_secrets:
            del self.oauth_secrets[self.session_id]
        self.session_id = response['oauth_token']
        self.logged_in = True
        return response

    def _oauth_request(self, url, token_secret='', params={}, **kw_params):
        """
        Make an OAuth request.

        This function only supports the PLAINTEXT signature method.
        Returns a file-like object representing the response.

        Keyword arguments:
        url -- the URL to request
        token_secret (optional) -- the request token secret, if requesting an
                                   access token (defaults to empty)
        params -- a dictionary of parameters to add to the request, such as
                  oauth_callback, oauth_token, or oauth_verifier

        Additional parameters can be passed either as a dictionary or as
        keyword arguments.

        """
        oauth_params = dict(params)
        oauth_params.update(kw_params)
        oauth_params.update({
                             'oauth_consumer_key': self.key,
                             'oauth_nonce': str(random.randint(0, 99999999)),
                             'oauth_signature_method': 'PLAINTEXT',
                             'oauth_signature': '%s&%s' % ('', token_secret),
                             'oauth_timestamp': str(int(time.time())),
                            })
        data = urllib.parse.urlencode(oauth_params, True)
        request = urllib.request.Request(url, data)
        request.add_header('User-Agent', self.agent)
        try:
            return self.opener.open(request)
        except urllib.error.HTTPError as error:
            if error.code == 401:
                self.logged_in = False
            raise


# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Authentication,)