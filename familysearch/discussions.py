# Python imports

# Magic

class Discussions:
    def __init__(self):
        pass
    
    def create_discussion(self):
        pass # TODO
    
    def discussion(self):
        pass # TODO
    
    def comments(self):
        pass # TODO
    
    def comment(self):
        pass # TODO
    
    def discussion_references(self):
        pass # TODO
        
    def discussion_reference(self):
        pass # TODO

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Discussions,)