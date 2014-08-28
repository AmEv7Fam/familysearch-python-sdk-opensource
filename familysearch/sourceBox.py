# Python imports

# Magic

class SourceBox:
    def __init__(self):
        pass # TODO
    
    def ud_collections__user(self):
        pass # TODO
    
    def ud_collections(self):
        pass # TODO
    
    def ud_collection(self):
        pass # TODO
    
    def ud_collection_source_descriptions(self):
        pass # TODO
    
    def ud_collections_source_descriptions_user(self):
        pass # TODO

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (SourceBox,)