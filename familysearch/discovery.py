
# Python imports



from . import FamilySearch

# Magic

class Discovery(object):
    def __init__(self):
        self.root_collection = self.get(self.base + '/.well-known/collection')
        self.collections = self.get(self.root_collection['collections'][0]
                                    ['links']['subcollections']['href'])
        self.family_tree = self.get(self.collections['collections'][0]['links']
                                    ['self']['href'])
        self.historical_records = self.get(self.collections['collections'][1]
                                           ['links']['self']['href'])
        self.user_sources = self.get(self.collections['collections'][2]['links']
                                     ['self']['href'])
        self.memories_collection = self.get(self.collections['collections'][3]
                                            ['links']['self']['href'])
        self.discussions_collection = self.get(self.collections['collections']
                                               [4]['links']['self']['href'])
        self.places_authority = self.get(self.collections['collections'][5]
                                         ['links']['self']['href'])
        self.dates_authority = self.get(self.collections['collections'][6]
                                        ['links']['self']['href'])
        self.person = ""
        
    def fix_discovery(self):
        try:
            self.user = self.get_current_user()['users'][0]
        except KeyError:
            self.user = ""
    
    
# FamilySearch hookup

FamilySearch.__bases__ += (Discovery,)
