# -*- coding: utf-8 -*-

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
    # Python 3
    app_key = config["fskey"]["devkey"]
    base = config["fskey"]["base"]
    try:
        user = config["fskey"]["user"]
    except KeyError:
        user = None
    try:
        password = config["fskey"]["password"]
    except KeyError:
        password = None
except AttributeError:
    # Python 2
    app_key = config.get("fskey", "devkey")
    base = config.get("fskey", "base")
    user = config.get("fskey", "user")
    password = config.get("fskey", "password")

# Sign into FamilySearch, and keep on trying until successful.

fs = FamilySearch("FSPySDK/SampleApps", app_key, base=base)
if user and password:
    print("Try user/password from config.ini")
    try:
        fs.login(user, password)
    except HTTPError as e:
        print("HTTPError:", str(e))
        #print("dir(e):", dir(e))
        print("code:", e.code)
        print("hdrs:", str(e.hdrs).replace("\n", "\n\t"))
        print("reason:", e.reason)
        user = password = None

if not fs.logged_in:
    print("Please sign in to FamilySearch.")

while not fs.logged_in:
    try:
        fs.login(input("Username: "), getpass())
    except HTTPError:
        print("Not logged in. Try again.")

me = fs.get_current_user()['response']['users'][0]['displayName']
print("Welcome, " + me + "!")
