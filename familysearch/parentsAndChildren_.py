# Python imports

# Magic

class ParentsAndChildren:
    def __init__(self):
        self.child_base = self.tree_base + "child-and-parents-relationships/"

    def get_child_relationship(self, crid):
        return self.get(self.child_base + crid)
    
    def delete_child_relationship_parent(self, crid, parent):
        url = self.child_base + crid + "/" + parent
        response = self._request(url, method="DELETE")
        return dict(response.info())
    
    def delete_child_relationship_conclusion(self, crid, cid, role):
        url = self.child_base + crid + "/" + role + "/conclusions/" + cid
        response = self._request(url, method="DELETE")
        return dict(response.info())
    
    def child_relationship_restore(self, crid):
        url = self.child_base + crid + "/restore"
        response = self._request(url, method="POST", nojson=True)
        return dict(response.info())

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (ParentsAndChildren,)