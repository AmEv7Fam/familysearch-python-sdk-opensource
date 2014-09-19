# Python imports

# Magic

class ParentsAndChildren:
    def __init__(self):
        self.child_base = self.tree_base + "child-and-parents-relationships/"

    def create_child_relationship(self, data):
        url = self.tree_base + 'relationships'
        response = self._request(url, data)
        return dict(response.info())
    
    def delete_child_relationship_parent(self, crid, parent):
        url = self.child_base + crid + "/" + parent
        response = self._request(url, method="DELETE")
        return dict(response.info())
    
    def cap_relationship_conclusion(self):
        pass # TODO
    
    def child_relationship_restore(self):
        pass # TODO

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (ParentsAndChildren,)