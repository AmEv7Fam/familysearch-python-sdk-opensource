# Python imports

# Magic

class ParentsAndChildren:
    def __init__(self):
        self.child_base = self.tree_base + "child-and-parents-relationships/"

    def get_child_relationship(self, crid):
        return self.get(self.child_base + crid)
    
    def delete_child_relationship_parent(self, crid, parent):
        return self.delete(self.child_base + crid + "/" + parent)
    
    def delete_child_relationship_conclusion(self, crid, cid, role):
        return self.delete(self.child_base + crid + "/" + role + "/conclusions/" + cid)
    
    def child_relationship_restore(self, crid):
        return post(self.child_base + crid + "/restore", method="POST", nojson=True)

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (ParentsAndChildren,)