# Python imports

# Magic

class Records:
    def __init__(self):
        pass

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Records,)