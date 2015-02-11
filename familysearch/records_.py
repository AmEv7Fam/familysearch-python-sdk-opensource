"""FamilySearch Records submodule"""
# Python imports

# Magic

class Records:
    """https://familysearch.org/developers/docs/api/resources#records"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#records"""
        pass

    # There might be a way to reverse-engineer something from the resource,
    # but with a lack of docuementation as of right now, that's what's going
    # to need to happen... Eventually...

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Records,)