from __future__ import print_function
import os
import sys

try:
    # Python 3
    import configparser
    from urllib.error import HTTPError
except ImportError as ex:
    # Python 2
    import ConfigParser as configparser
    from urllib2 import HTTPError

from getpass import getpass

sys.path.append("..")
from familysearch import FamilySearch

config_path = os.path.dirname(os.path.abspath(__file__)) + "/config.ini"

config = configparser.ConfigParser()
config.read(config_path)
app_key = config["fskey"]["devkey"]
base = config["fskey"]["base"]

fs = FamilySearch("FSPySDK/SampleApps", app_key, base=base)
print("Please sign in to FamilySearch.")
while fs.logged_in is not True:
    try:
        fs.login(input("Username: "), getpass())
    except HTTPError:
        print("Not logged in. Try again.")
        raise

print("Welcome, "+ fs.get_current_user()['users'][0]['displayName']+"!")