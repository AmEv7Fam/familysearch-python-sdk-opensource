"""FamilySearch Ordinances submodule"""
# Python imports

# Magic

class Ordinances:
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#ordinances"""
        pass
    
# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Ordinances,)
