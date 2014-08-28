# Python imports
 
# Magic

class Authorities():
    def __init__(self):
        self.authorities_base = self.base + '/authorities'
        
    def dates(self, dateX):
        url = self.base + '/platform/dates?date=' + dateX
        response = self._request(url)
        response = response.fs2py(response)
        return response

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Authorities,)