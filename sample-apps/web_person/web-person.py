import webbrowser
import os
import sys

try:
    # Python 3
    import configparser
    from http import server
    from urllib.parse import parse_qs
except ImportError:
    # Python 2
    import ConfigParser as configparser
    import BaseHTTPServer as server
    from urlparse import parse_qs
    
from familysearch import FamilySearch

config_path = os.path.dirname(os.path.abspath(sys.argv[0])) + "/config.ini"

config = configparser.ConfigParser()
config.read(config_path)
try:
    app_key = config["fskey"]["devkey"]
    base = config["fskey"]["base"]
    port = config["server"]["port"]
    redirect = config["server"]["redirect_uri"]
except AttributeError:
    app_key = config.get("fskey", "devkey")
    base = config.get("fskey", "base")
    port = config.get("server", "port")
    redirect = config.get("server", "redirect_uri")

url = "http://localhost" + (":"+ port) if port is not "80" else ""
ruri = ""
for x in redirect[::-1]:
    ruri = x + ruri
    if x is "/":
        break

fs = FamilySearch("FSPySDK/SampleApps", app_key, base=base)

fslogin = fs.root_collection['collections'][0]['links']\
        ['http://oauth.net/core/2.0/endpoint/authorize']['href']

fslogin = fs._add_query_params(fslogin, {'response_type': 'code',
                             'client_id': fs.key,
                             'redirect_uri': redirect
                             })

class getter(server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(code=200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        path = self.path
        
        top = "<!DOCTYPE html><html><head><title>FSPySDK Sample App</title>"
        middle = "</head><body>"
        bottom = "</body></html>"
        if path.startswith(ruri):
            bottom = self.get_code(path) + bottom
        else:
            if fs.logged_in:
                middle += logged_in()
                if path.startswith("/?pid="):
                    pid = parse_qs(path)["/?pid"][0]
                    person = fs.get_person(pid)
                    middle += has_pid(person)
            else:
                middle = self.not_logged_in() + middle
                middle = self.not_logged_in()

            body = top + middle + bottom
        
        self.wfile.write(body.encode("utf-8"))

    def not_logged_in(self):
        string = '<script>function openWin(){window.open("' + fslogin
        string += '","fsWindow","width=320,height=615");}</script>'
        string += "</head><body>"
        string += "<button onclick=openWin()>Sign in to FamilySearch</button>"
        return string
    def logged_in(self):
        string = 'Search given FamilySearch PID (default is your own)<form>'
        string +='<input type="text" name="pid" value='+ fs.user['personId']
        string +='><br />input type="submit" value="Submit"></form>'
        return string

    def has_pid(self, person):
        name = person['response']['persons'][0]['names'][0]['nameForms'][0]\
            ['fullText']
        string = 'This is ' + name + '. <br />'
        if person['response']['persons'][0]['display']['gender'] == "Male":
            string += 'He' 
        else: 
            string += 'She'
        string += " is "
        if person['persons'][0]['living']:
            string += 'living'
        else:
            string += 'deceased'
        string += ".<br />"
        if person['response']['persons'][0]['display']['gender'] == "Male":
            string += 'His'
        else:
            string +="Her"
        string +=' lifespan is "'
        string += person['persons'][0]['display']['lifespan']
        string += '".<br />'
        return string

    def get_code(self, path):
        qs = parse_qs(path)
        qs = list(qs.values())[0][0]
        fs.oauth_code_login(qs)
        return '<script>window.opener.location.reload();window.close()</script>'

webbrowser.open(url)
server.HTTPServer(('', 63342), getter).serve_forever()