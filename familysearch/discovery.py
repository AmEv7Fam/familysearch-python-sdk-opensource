
# Python imports

# Magic

class Discovery(object):
    pass

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Discovery,)
