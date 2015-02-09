"""FamilySearch Authorities submodule"""
# Python imports
 
# Magic

class Authorities():
    def __init__(self):
        """Obsolete."""
        self.authorities_base = self.base + '/authorities'

    def get_dates(self, dateX):
        """Obsolete."""
        return self.get(self.base + '/platform/dates?date=' + dateX)

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Authorities,)