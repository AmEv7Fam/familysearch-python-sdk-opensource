# Python imports

# Magic

class SearchAndMatch:
    def __init__(self):
        pass
    
    def person_search(self):
        pass # TODO
    
    def person_matches(self):
        pass # TODO
    
    def person_not_a_match_list(self):
        pass # TODO
    
    def person_matches_query(self):
        pass # TODO

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (SearchAndMatch,)