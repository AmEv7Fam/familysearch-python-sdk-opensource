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

def get_config():
    config_path = os.path.dirname(os.path.abspath(sys.argv[0])) + "/config.ini"

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

def use_login(fs, config):
   # keep on trying until successful.
    user = config.get("fskey", "user")
    password = config.get("fskey", "password")
    if user and password:
        print("Try user/password from config.ini")
        try:
            fs.login(user, password)
        except HTTPError as e:
            print("HTTPError:", str(e))
            # print("dir(e):", dir(e))
            print("code:", e.code)
            print("hdrs:", str(e.hdrs).replace("\n", "\n\t"))
            print("reason:", e.reason)
            print("Not logged in.")
        finally:
            user = password = None

    if not fs.logged_in:
        print("Please sign in to FamilySearch.")

    while not fs.logged_in:
        try:
            user = input("Username: ")
            password = getpass()
            fs.login(user, password)
        except HTTPError:
            print("Not logged in. Try again.")
        except EOFError:
            exit(1)
        finally:
            user = password = None

def use_desktop_login(fs):
    ruri = "http://localhost:63342/fspy"
    fs.oauth_desktop_login(ruri)

config = get_config()
app_key = config.get("fskey", "devkey")
base = config.get("fskey", "base")

# Sign into FamilySearch

fs = FamilySearch("FSPySDK/SampleApps", app_key, base=base)

#use_login(fs, config)
use_desktop_login(fs)

me = fs.get_current_user()['response']['users'][0]['displayName']
print("Welcome, " + me + "!")
