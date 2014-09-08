# Python imports

"""
A module implementing the Identity version 2 API module

Main class: Authentication, meant to be mixed-in to the FamilySearch class
"""

try:
    # Python 3
    from urllib.request import(build_opener, HTTPCookieProcessor)
    from urllib.parse import(urlencode, parse_qs)
    import socketserver
    from http import server
except ImportError:
    # Python 2
    from urllib import urlencode
    from urllib2 import(build_opener, HTTPCookieProcessor)
    import SocketServer as socketserver
    import SimpleHTTPServer as server
    
import webbrowser

# Magic

class Authentication(object):

    """
    A mix-in implementing the Identity version 2 endpoints
    """

    def __init__(self):
        """
        Set up the URLs for authentication.
        """
        if self.base == "https://familysearch.org":
            self.auth_base = "https://ident.familysearch.org/cis-web/oauth2/v3/"
        elif self.base == "https://sandbox.familysearch.org":
            self.auth_base = self.base + "/cis-web/oauth2/v3/"
        else:
            self.auth_base = "https://identbeta.familysearch.org/cis-web/oauth2/v3/"

        # Assume logged_in if session_id is set
        self.logged_in = bool(self.session_id)
        

        cookie_handler = HTTPCookieProcessor()
        self.cookies = cookie_handler.cookiejar
        self.opener = build_opener(cookie_handler)

    def login(self, username, password):
        """
        Log into FamilySearch using Basic Authentication.

        This mechanism is available only to approved developer keys.
        """
        self.logged_in = False
        self.cookies.clear()
        url = self.auth_base + '/token'
        credentials = urlencode({'username': username,
                                 'password': password,
                                 'client_id': self.key,
                                 'grant_type': 'password'
                                 })
        response = self._request(url, credentials)
        self.session_id = self._fs2py(response)['access_token']
        self.logged_in = True
        
    def oauth_login(self):
        """
        Log into FamilySearch using OAuth2 Authentication.
        
        This mechanism is required for browser-based applications.
        """
        self.logged_in = False
        self.cookies.clear()
        url = self.auth_base + 'authorization'
        url = self._add_query_params(url, {'response_type': 'code',
                                     'client_id': self.key,
                                     'redirect_uri': "http://localhost:63342"
                                     })
        webbrowser.open(url)
        server.HTTPServer(('', 63342), getter).handle_request()
        
        # Now that we have the authentication token, grab the access token.
        
        url = self.auth_base + '/token'
        credentials = urlencode({'grant_type': 'authorization_code',
                                 'code': qs,
                                 'client_id': self.key
                                  })
        print(credentials)
        response = self._request(url, credentials)
        self.sesion_id = self._fs2py(response)['access_token']
        self.logged_in = True
        

    def logout(self):
        """
        Log the current session out of FamilySearch.
        """
        self.logged_in = False
        # TODO: Change to Delete Access Token
        self.session_id = None
        self.cookies.clear()

    def session(self):
        """
        Keep the current session in an active state by sending an empty request.

        Calling this method is an easy way to turn a sessionId query parameter
        into a cookie without doing anything else.

        """
        # TODO: What is the new equivalent?
        #url = self.identity_base + 'session'
        #self.session_id = identity.parse(self._request(url)).session.id
        #self.logged_in = True
        #return self.session_id
        pass
    
class getter(server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(code=200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        path = self.path
        global qs
        qs = parse_qs(path)
        qs = list(qs.values())[0][0]
        server.wfile("<html>")
        server.wfile("<head>")
        server.wfile("<title>FSPySDKLogin</title>")
        server.wfile("</head")
        server.wfile("<body>")
        server.wfile("<p>This page is intended for log-in purposes only.</p>")
        server.wfile("<p>You can safely close this page.</p>")
        server.wfile("</body")
        server.wfile("</html>")
        
        

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Authentication,)
