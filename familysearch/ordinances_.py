"""FamilySearch Ordinances submodule"""
# Python imports

# Magic

class Ordinances:
    """https://familysearch.org/developers/docs/api/resources#ordinances"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#ordinances"""
        from familysearch import FamilySearch
        FamilySearch.__bases__ += (Ordinances,)
    
# FamilySearch imports



