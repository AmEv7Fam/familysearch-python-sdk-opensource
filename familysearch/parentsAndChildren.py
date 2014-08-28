# Python imports

# Magic

class ParentsAndChildren:
    def __init__(self):
        pass
        
    def relationships(self):
        pass # TODO
    
    def cap_relationship(self):
        pass # TODO
    
    def cap_relationship_parent(self):
        pass # TODO
    
    def cap_relationship_conclusion(self):
        pass # TODO
    
    def cap_relationship_restore(self):
        pass # TODO

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (ParentsAndChildren,)