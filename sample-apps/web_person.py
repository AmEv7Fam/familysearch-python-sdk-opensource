from __future__ import print_function
import os
import sys

try:
    # Python 3
    import configparser
    from urllib.error import HTTPError
    from http import server
except ImportError:
    # Python 2
    import ConfigParser as configparser
    from urllib2 import HTTPError
    input = raw_input
    import BaseHTTPServer as server


from familysearch import FamilySearch

config_path = os.path.dirname(os.path.abspath(sys.argv[0])) + "/config.ini"

config = configparser.ConfigParser()
config.read(config_path)
try:
    app_key = config["fskey"]["devkey"]
    base = config["fskey"]["base"]
except AttributeError:
    app_key = config.get("fskey", "devkey")
    base = config.get("fskey", "base")

fs = FamilySearch("FSPySDK/SampleApps", app_key, base=base)

