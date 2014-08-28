# Python imports

# Magic

class Utilities:
    def __init__(self):
        pass
    
    def pending_modifications(self):
        pass
    
    def redirect(self):
        pass

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Utilities,)