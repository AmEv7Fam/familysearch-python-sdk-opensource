# Python imports

# Magic

class Spouses:
    def __init__(self):
        pass # TODO
    
    def create_relaitionship(self):
        pass # TODO
    
    def couple_relationship(self):
        pass # TODO
    
    def couple_relationship_conclusion(self):
        pass # TODO
    
    def couple_relationship_restore(self):
        pass # TODO

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Spouses,)