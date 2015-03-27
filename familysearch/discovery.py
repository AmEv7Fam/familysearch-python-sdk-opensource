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
            response = self.get(self.collections[collection]['url'])['response']
            self.collections[collection]['response'] = response

    def fix_discovery(self):
        """The Hypermedia items are semi-permanent. Some things change
        based on who's logged in (or out).
        """
        for item in self.subcollections['response']['collections']:
            self.collections[item['id']] = {}
            self.collections[item['id']]['url'] = item['links']['self']['href']
            if item['id'] == 'LDSO':
                try:
                    self.update_collection("LDSO")
                except:
                    self.lds_user = False
                else:
                    self.lds_user = True
        try:
            self.user = self.get_current_user()['response']['users'][0]
        except:
            self.user = ""