# Python imports

# Magic

class Utilities:
    def __init__(self):
        pass
    
    def pending_modifications(self):
        url = self.base + "/platform/pending-modifications"
        response = self._request(url)
        response = self._fs2py(response, "features")
        return response
    
    def redirect(self, params):
        url = self._add_query_params(self.base + "platform/redirect", params)
        return url

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Utilities,)