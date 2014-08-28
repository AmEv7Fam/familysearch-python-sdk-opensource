# Python imports

# Magic

class Places:
    def __init__(self):
        pass
    
    def places_search(self):
        pass # TODO
    
    def place_description(self):
        pass # TODO
    
    def place_group(self):
        pass # TODO
    
    def place(self):
        pass # TODO
    
    def place_description_children(self):
        pass # TODO
    
    def place_type(self):
        pass # TODO
    
    def place_type_group(self):
        pass # TODO
    
    def place_types(self):
        pass # TODO
    
    def place_type_groups(self):
        pass # TODO

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Places,)