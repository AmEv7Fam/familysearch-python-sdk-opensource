"""FamilySearch Ordinances submodule"""
# Python imports

from . import FamilySearch

# Magic

class Ordinances:
    """https://familysearch.org/developers/docs/api/resources#ordinances"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#ordinances"""
        pass
    
# FamilySearch imports


FamilySearch.__bases__ += (Ordinances,)
