"""FamilySearch Discovery submodule"""
# Python imports

# Magic

class Discovery(object):
    """https://familysearch.org/developers/docs/api/tree/FamilySearch_Collections_resource"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#discovery"""
        # TODO: Set it up so that it doesn't need to call the sumbodules
        # until absolutely necessary...
        from familysearch import FamilySearch
        FamilySearch.__bases__ += (Discovery,)
        self.root_collection = self.get(self.base + '/.well-known/collection')
        self.collections = self.get(self.root_collection['collections'][0]
                                    ['links']['subcollections']['href'])
        self.fix_discovery()

    def update_collection(self, collection):
            self.collections[collection] = self.get(collection)

    def fix_discovery(self):
        """The Hypermedia items are semi-permanent. Some things change
        based on who's logged in (or out).
        """
        for item in self.collections['collections']:
            if item['id'] == 'LDSO':
                try:
                    self.collections['LDSO'] = ['links']['self']['href']
                except:
                    self.lds_user = False
                else:
                    self.lds_user = True
            else:
                self.collections[item['id']] = item['links']['self']['href']
        try:
            self.user = self.get_current_user()['users'][0]
        except:
            self.user = ""