# Python imports

# Magic

class ParentsAndChildren:
    def __init__(self):
        pass

    def create_child_relationship(self, cpid, data):
        url = self.tree_base + 'relationships'
        response = self._request(url, data)
        return dict(response.info())
    
    def cap_relationship_parent(self):
        pass # TODO
    
    def cap_relationship_conclusion(self):
        pass # TODO
    
    def child_relationship_restore(self):
        pass # TODO

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (ParentsAndChildren,)