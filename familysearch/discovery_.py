# pylint: disable=no-member, cyclic-import, import-error
# Python imports

# FYI: I moved it to top, because I wasn't sure if I needed to import FS class
# before it could run.
from . import FamilySearch

# Magic

class Discovery(object):
    def __init__(self):
        """"""
        self.root_collection = self.get(self.base + '/.well-known/collection')
        self.collections = self.get(self.root_collection['collections'][0]
                                    ['links']['subcollections']['href'])
        for item in self.collections['collections']:
            if item['id'] == 'FSFT':
                self.family_tree = self.get(
                  item['links']['self']['href'])
            elif item['id'] == 'FSHRA':
                self.historical_records = self.get(
                  item['links']['self']['href'])
            elif item['id'] == 'FSUDS':
                self.user_sources = self.get(
                  item['links']['self']['href'])
            elif item['id'] == 'FSMEM':
                self.memories_collection = self.get(
                  item['links']['self']['href'])
            elif item['id'] == 'FSDF':
                self.discussions_collection = self.get(
                  item['links']['self']['href'])
            elif item['id'] == 'FSPA':
                self.places_authority = self.get(
                  item['links']['self']['href'])
            elif item['id'] == 'FSDA':
                self.dates_authority = self.get(
                  item['links']['self']['href'])
            elif item['id'] == 'FSCV':
                self.vocab = self.get(
                  item['links']['self']['href'])
            elif item['id'] == 'LDSO':
                try:
                    self.lds_ordinances = self.get(['links']['self']['href'])
                except:
                    self.lds_user = False
                else:
                    self.lds_user = True
        try:
            self.user = self.get_current_user()['users'][0]
        except:
            self.user = ""

    def fix_discovery(self):
        """The Hypermedia items are semi-permanent. Some things change
        based on who's logged in (or out).
        """
        for item in self.collections['collections']:
            if item['id'] == 'LDSO':
                try:
                    self.lds_ordinances = self.get(
                      item['links']['self']['href'])
                except:
                    self.lds_user = False
                else:
                    self.lds_user = True
        try:
            self.user = self.get_current_user()['users'][0]
        except:
            self.user = ""
    
    
# FamilySearch hookup

FamilySearch.__bases__ += (Discovery,)
