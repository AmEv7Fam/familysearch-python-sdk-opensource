# pylint: disable=no-member, cyclic-import, import-error
# Python imports

# Magic

class Ordinances:
    def __init__(self):
        """"""
        pass
    
# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Ordinances,)
