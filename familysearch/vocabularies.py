# Python imports

# Magic

class Vocabularies:
    def __init__(self):
        pass

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Vocabularies,)