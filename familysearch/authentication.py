# Python imports

"""
A module implementing the Identity version 2 API module

Main class: Authentication, meant to be mixed-in to the FamilySearch class
"""

try:
    # Python 3
    from urllib.request import(build_opener, HTTPCookieProcessor)
    from urllib.parse import urlencode
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
        url = self.auth_base + 'authorization'
        url = self._add_query_params(url, {'response_type': 'code',
                                     'client_id': self.key,
                                     'redirect_uri': "http://localhost:63342/login.html"
                                     })
        webbrowser.open(url)
        socketserver.TCPServer(('', 63342), server.SimpleHTTPRequestHandler
                               ).handle_request()

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

from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse

class GetHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        message_parts = [
                'CLIENT VALUES:',
                'client_address=%s (%s)' % (self.client_address,
                                            self.address_string()),
                'command=%s' % self.command,
                'path=%s' % self.path,
                'real path=%s' % parsed_path.path,
                'query=%s' % parsed_path.query,
                'request_version=%s' % self.request_version,
                '',
                'SERVER VALUES:',
                'server_version=%s' % self.server_version,
                'sys_version=%s' % self.sys_version,
                'protocol_version=%s' % self.protocol_version,
                '',
                'HEADERS RECEIVED:',
                ]
        for name, value in sorted(self.headers.items()):
            message_parts.append('%s=%s' % (name, value.rstrip()))
        message_parts.append('')
        message = '\r\n'.join(message_parts)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message)
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Authentication,)