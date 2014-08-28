# Python imports

# Magic

class Notes:
    def __init__(self):
        pass
    
    def person_notes(self):
        pass # TODO
    
    def person_note(self):
        pass # TODO
    
    def couple_relationship_notes(self):
        pass # TODO
    
    def couple_relationship_note(self):
        pass # TODO
    
    def cap_relationship_notes(self):    
        pass # TODO
    
    def cap_relationship_notes(self):
        pass # TODO

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Notes,)