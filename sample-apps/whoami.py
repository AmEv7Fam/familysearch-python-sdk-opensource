from __future__ import print_function
import os

# ConfigParser is renamed in Python 3 to configparser
try:
    # Python 3
    import configparser
except ImportError as ex:
    # Python 2
    import ConfigParser as configparser
from getpass import getpass

from familysearch import FamilySearch

config_path = os.path.dirname(os.path.abspath(__file__)) + "config.ini"

config = configparser.ConfigParser()
config.read(config_path)
app_key = config["fskey"]

fs = FamilySearch("FSPySDK/SampleApps", app_key)
while fs.logged_in is False:
    try:
        fs.login(input("Username"), getpass())
    except Exception:
        print("")

print("Welcome, "+ fs.get_current_user()['users'][0]['displayName']+"!")