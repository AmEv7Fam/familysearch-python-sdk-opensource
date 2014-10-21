# Python imports

# Magic

class Utilities:
    def __init__(self):
        pass
    
    def get_pending_modifications(self):
        return self.get(self.root_collection['collections'][0]['links']\
                        ['pending-modifications']['href'])
    
    def redirect(self, params):
        return self._add_query_params(self.base + "platform/redirect", params)


# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Utilities,)