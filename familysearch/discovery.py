
# Python imports



from . import FamilySearch

# Magic

class Discovery(object):
    def __init__(self):
        self.root_collection = self.get(self.base + '/.well-known/collection')
        self.family_tree = self.get(self.root_collection['collections'][0]\
        ['links']['family-tree']['href'])
        
    def fix_discovery(self):
        self.root_collection = self.get(self.base + '/platform/collection')
        self.family_tree = self.get(self.root_collection['collections'][0]\
        ['links']['family-tree']['href'])
    
    
# FamilySearch hookup

FamilySearch.__bases__ += (Discovery,)
