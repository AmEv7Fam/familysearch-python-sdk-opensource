"""FamilySearch Discovery submodule"""
# Python imports

# Magic

class Discovery(object):
    """https://familysearch.org/developers/docs/api/tree/FamilySearch_Collections_resource"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#discovery"""
        # TODO: Set it up so that it doesn't need to call the sumbodules
        # until absolutely necessary...
        self.root_collection = self.get(self.base + '/.well-known/collection')
        self.subcollections = self.get(self.root_collection['response']
                                    ['collections'][0]['links']
                                    ['subcollections']['href'])
        self.collections = {}
        self.fix_discovery()

    def update_collection(self, collection):
            self.collections[collection] = self.get(collection)

    def fix_discovery(self):
        """The Hypermedia items are semi-permanent. Some things change
        based on who's logged in (or out).
        """
        for item in self.subcollections['response']['collections']:
            if item['id'] == 'LDSO':
                try:
                    self.collections['LDSO'] = self.get(['links']['self']['href'])
                except:
                    self.lds_user = False
                else:
                    self.lds_user = True
            else:
                self.collections[item['id']] = item['links']['self']['href']
        try:
            self.user = self.get_current_user()['response']['users'][0]
        except:
            self.user = ""