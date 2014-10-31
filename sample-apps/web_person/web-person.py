import webbrowser
import os
import sys

try:
    # Python 3
    import configparser
    from http import server
    from urllib.parse import(urlencode, parse_qs)
except ImportError:
    # Python 2
    import ConfigParser as configparser
    import BaseHTTPServer as server
    from urllib import urlencode
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
        
        top = "<!DOCTYPE html>\n"\
              "<html>\n"\
              "<head>\n"\
              "<title>FSPySDK Sample App</title>\n"
        middle = "</head>\n"\
                 "<body>\n"
        bottom = "</body>\n"\
                 "</html>\n"
        if path.startswith(ruri):
            qs = parse_qs(path)
            qs = list(qs.values())[0][0]
            url = fs.token
            credentials = urlencode({'grant_type': 'authorization_code',
                                     'code': qs,
                                     'client_id': fs.key
                                      })
            credentials = credentials.encode("utf-8")
            response = fs._request(url, credentials,
                                   {"Content-Type": "application/x-www-form-urlencoded",
                                    "Accept": "application/json"}, nojson=True)
            fs.session_id = fs._fs2py(response)['access_token']
            fs.logged_in = True
            fs.fix_discovery()
            fs.own_pid = fs.get_current_user()['users'][0]['personId']
            body = top + middle + '<script>\nwindow.opener.location.reload();\n'\
                                  'window.close()</script>\n' + bottom
        else:
            if fs.logged_in:
                middle = middle + 'Search given FamilySearch PID (default is '\
                                  'your own)\n'\
                                  '<form>\n<input type="text" name="pid" '\
                                  'value='+ fs.own_pid +'><br />\n'\
                                  '<input type="submit" value="Submit\n">'\
                                  '</form>\n'
                print(path)
                if path.startswith("/?pid="):
                    pid = parse_qs(path)["/?pid"][0]
                    person = fs.get_person(pid)
                    middle = middle + \
                             'This is ' + person['persons'][0]['names'][0]\
                             ['nameForms'][0]['fullText'] + '. <br />\n'+ \
                             ('He' if person['persons'][0]['display']['gender']\
                             == "Male" else 'She') + " is " + \
                             ('living' if person['persons'][0]['living']\
                             else 'deceased') + ".<br />\n" + ('His' if \
                             person['persons'][0]['display']['gender'] == "Male"\
                             else "Her") + ' lifespan is "' + person['persons']\
                             [0]['display']['lifespan'] + '".<br />\n'
                                
            else:
                top = top + '<script>function openWin()\n{window.open("' +\
                            fslogin + '","fsWindow","width=320,height=615");'\
                            '}</script>\n'
                
                middle = middle + '<button onclick=openWin()>'\
                                  'Sign in to FamilySearch</button>\n'

            body = top + middle + bottom
        
        self.wfile.write(body.encode("utf-8"))
        
        

webbrowser.open(url)
server.HTTPServer(('', 63342), getter).serve_forever()