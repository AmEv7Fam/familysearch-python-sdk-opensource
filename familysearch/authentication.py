"""FamilySearch Authentication submodule"""
# Python imports
from __future__ import print_function

try:
    # Python 3
    from urllib.request import(build_opener, HTTPCookieProcessor)
    from urllib.parse import(urlencode, parse_qs)
    from http import server
except ImportError:
    # Python 2
    from urllib import urlencode
    from urlparse import parse_qs
    from urllib2 import(build_opener, HTTPCookieProcessor)
    import BaseHTTPServer as server

import webbrowser
import json

# Magic

class Authentication(object):
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#authentication
        Set up the URLs for authentication.
        """
        self.token = self.root_collection['response']['collections'][0]['links']\
        ['http://oauth.net/core/2.0/endpoint/token']['href']
        cookie_handler = HTTPCookieProcessor()
        self.cookies = cookie_handler.cookiejar
        self.opener = build_opener(cookie_handler)

    def login(self, username, password):
        """Log into FamilySearch using Basic Authentication.
        This mechanism is available only to approved developer keys.
        """
        self.logged_in = False
        self.cookies.clear()
        url = self.token
        credentials = urlencode({'username': username,
                                 'password': password,
                                 'client_id': self.key,
                                 'grant_type': 'password'
                                 })
        credentials = credentials.encode("utf-8")
        headers = {"Content-type": "application/x-www-form-urlencoded",
                                 "Accept": "application/json;charset=ISO-8859-1"}
        def xprint():
            print("url:", url)
            print("credentials:", credentials)
            print("headers:", headers)
        xprint()
        response = self.post(url, credentials, headers)
        self.access_token = response['response']['access_token']
        self.logged_in = True
        self.fix_discovery()

    def oauth_desktop_login(self, ruri=None):
        """
        Log into FamilySearch using OAuth2 Authentication.
        This is primarily a convenience function for destop apps.
        Not normally intended for production apps, but should
        work while waiting for approval for password login.
        Default Redirect URI is "http://localhost:63342/fslogin",
        but you can set your own as a paramater.
        """
        if ruri is None:
            ruri = "http://localhost:63342/fslogin"
        self.logged_in = False
        self.cookies.clear()
        url = self.root_collection['response']['collections'][0]['links']\
        ['http://oauth.net/core/2.0/endpoint/authorize']['href']
        url = self._add_query_params(url, {'response_type': 'code',
                                     'client_id': self.key,
                                     'redirect_uri': ruri
                                     })
        webbrowser.open(url)
        server.HTTPServer(('', 63342), Getter).handle_request()
        # Now that we have the authentication token, grab the access token.
        self.oauth_code_login(qs)

    def oauth_code_login(self, code):
        """
        Convenience function for Web servers to log into FamilySearch
        with the token code FamilySearch hands you.
        """
        url = self.token
        credentials = urlencode({'grant_type': 'authorization_code',
                                 'code': code,
                                 'client_id': self.key
                                  })
        credentials = credentials.encode("utf-8")
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "application/json"}
        response = self.post(url, credentials ,headers, nojson=True)
        response = json.loads()
        self.access_token = response['response']['access_token']
        self.logged_in = True
        self.fix_discovery()

    def unauthenticated_login(self, ip_address):
        """
        Log into FamilySearch without authenticating.
        Has very limited read-only access.
        Not intended for general use.
        """
        self.logged_in = False
        self.cookies.clear()
        url = self.token
        credentials = urlencode({'ip_address': ip_address,
                                 #TODO: make IP address generiation automatic
                                 'client_id': self.key,
                                 'grant_type': 'unauthenticated_session'
                                 })
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "application/json"}
        credentials = credentials.encode("utf-8")
        response = self.post(url, credentials, headers)
        self.access_token = response['response']['access_token']
        self.logged_in = True
        self.fix_discovery()

    def logout(self):
        """
        Log the current session out of FamilySearch.
        """
        self.logged_in = False
        url = self.token + "?access_token=" + self.access_token
        self.delete(url)
        self.access_token = None
        self.cookies.clear()
        self.fix_discovery()

class Getter(server.BaseHTTPRequestHandler):
    """Sample login page, mostly for oauth_desktop_login."""
    def do_GET(self):
        """Sample page to get Oauth code, and log in with."""
        self.send_response(code=200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        path = self.path
        global qs
        qs = parse_qs(path)
        qs = list(qs.values())[0][0]
        sendme = "<html><head><title>FSPySDKLogin</title></head><body>"
        sendme += "<p>This page is intended for log-in purposes only.</p>"
        sendme += "<p>You can safely close this page.</p></body></html>"
        sendme = sendme.encode("UTF-8")
        self.wfile.write(sendme)
