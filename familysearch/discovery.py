
# Python imports



from . import FamilySearch

# Magic

class Discovery(object):
    def __init__(self):
        self.root_collection = self.get(self.base + '/.well-known/collection')
        
    def fix_discovery(self):
        self.root_collection = self.get(self.base + '/platform/collection')
    
    
# FamilySearch hookup

FamilySearch.__bases__ += (Discovery,)
