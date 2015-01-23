"""FamilySearch Discovery submodule"""
# Python imports

# FYI: I moved it to top, because I wasn't sure if I needed to import FS class
# before it could run.
from . import FamilySearch

# Magic

class Discovery(object):
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#discovery"""
        self.root_collection = self.get(self.base + '/.well-known/collection')
        self.collections = self.get(self.root_collection['collections'][0]
                                    ['links']['subcollections']['href'])
        for item in self.collections['collections']:
            #https://familysearch.org/developers/docs/api/tree/FamilySearch_Collections_resource
            if item['id'] == 'FSFT':
                #https://familysearch.org/developers/docs/api/tree/FamilySearch_Family_Tree_resource
                self.family_tree = self.get(
                  item['links']['self']['href'])
            elif item['id'] == 'FSHRA':
                #https://familysearch.org/developers/docs/api/records/FamilySearch_Historical_Records_Archive_resource
                self.historical_records = self.get(
                  item['links']['self']['href'])
            elif item['id'] == 'FSUDS':
                #https://familysearch.org/developers/docs/api/sources/FamilySearch_User-Defined_Sources_resource
                self.user_sources = self.get(
                  item['links']['self']['href'])
            elif item['id'] == 'FSMEM':
                #https://familysearch.org/developers/docs/api/memories/FamilySearch_Memories_resource
                self.memories_collection = self.get(
                  item['links']['self']['href'])
            elif item['id'] == 'FSDF':
                #https://familysearch.org/developers/docs/api/discussions/FamilySearch_Discussions_resource
                self.discussions_collection = self.get(
                  item['links']['self']['href'])
            elif item['id'] == 'FSPA':
                #https://familysearch.org/developers/docs/api/places/FamilySearch_Place_Authority_resource
                self.places_authority = self.get(
                  item['links']['self']['href'])
            elif item['id'] == 'FSDA':
                #https://familysearch.org/developers/docs/api/dates/FamilySearch_Date_Authority_resource
                self.dates_authority = self.get(
                  item['links']['self']['href'])
            elif item['id'] == 'FSCV':
                #https://familysearch.org/developers/docs/api/places/FamilySearch_Controlled_Vocabulary_resource
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
