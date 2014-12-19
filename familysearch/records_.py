# Python imports

# Magic

class Records:
    def __init__(self):
        pass
    
    # There might be a way to reverse-engineer something from the resource,
    # but with a lack of docuementation as of right now, that's what's going
    # to need to happen... Eventually...
    

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Records,)