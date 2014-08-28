# Python imports

# Magic

class Sources:
    def __init__(self):
        pass # TODO
    
    def source_descriptions(self):
        pass # TODO
    
    def source_description(self):
        pass # TODO
    
    def person_source_query(self):
        pass # TODO
    
    def couple_relationship_sources_query(self):
        pass # TODO
    
    def couple_relationship_source_references(self):
        pass # TODO
    
    def couple_relatiohship_source_reference(self):
        pass # TODO
    
    def cap_relatioship_sources_query(self):
        pass # TODO
    
    def cap_relationship_source_references(self):
        pass # TODO
    
    def cap_relationship_source_reference(self):
        pass # TODO
    
    def source_references_query(self):
        pass # TODO

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Sources,)