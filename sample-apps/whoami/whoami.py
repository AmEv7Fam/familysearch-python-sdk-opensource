# Python imports
from __future__ import print_function
import os
import sys
from getpass import getpass

try:
    # Python 3
    import configparser
    from urllib.error import HTTPError
except ImportError:
    # Python 2
    import ConfigParser as configparser
    from urllib2 import HTTPError
    input = raw_input

from familysearch import FamilySearch

# Get app key from config.ini

config_path = os.path.dirname(os.path.abspath(sys.argv[0])) + "/config.ini"

config = configparser.ConfigParser()
config.read(config_path)
try:
    app_key = config["fskey"]["devkey"]
    base = config["fskey"]["base"]
except AttributeError:
    app_key = config.get("fskey", "devkey")
    base = config.get("fskey", "base")

# Sign into FamilySearch, and keep on trying until successful.

fs = FamilySearch("FSPySDK/SampleApps", app_key, base=base)
print("Please sign in to FamilySearch.")
while fs.logged_in is not True:
    try:
        fs.login(input("Username: "), getpass())
    except HTTPError:
        print("Not logged in. Try again.")

me = fs.get_current_user()['response']['users'][0]['displayName']
print("Welcome, " + me + "!")