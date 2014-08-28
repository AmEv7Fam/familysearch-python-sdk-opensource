# Python imports

# Magic

class Records:
    pass

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Records,)