# Python imports

# Magic

class Vocabularies:
    pass

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Vocabularies,)