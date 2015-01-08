# pylint: disable=no-member, cyclic-import, import-error
# Python imports
 
# Magic

class Authorities():
    def __init__(self):
        """"""
        self.authorities_base = self.base + '/authorities'

    def get_dates(self, dateX):
        """"""
        return self.get(self.base + '/platform/dates?date=' + dateX)

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Authorities,)