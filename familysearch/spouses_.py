"""FamilySearch Spouses submodule"""
# Python imports

# Magic

class Spouses:
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#spouses"""
        self.couple_base = self.tree_base + 'couple-relationships/'

    def create_couple_relationship(self, data):
        """"""
        return self.post(self.tree_base + 'relationships', data)

    def get_couple_relationship(self, cpid):
        """"""
        return self.get(self.couple_base + cpid)

    def update_couple_relationship_conclusion(self, cpid, data):
        """"""
        return self.post(self.couple_base + cpid, data)

    def delete_couple_relationship_conclusion(self, cpid, cid, reason=None):
        """"""
        return self.delete(
  self.couple_base + cpid + '/conclusions/' + cid, headers={'X-Reason': reason})

    def delete_couple_relationship(self, cpid, reason=None):
        """"""
        return self.delete(
         self.couple_base + cpid, headers={'X-Reason': reason}, method="DELETE")

    def restore_couple_relationship(self, cpid):
        """"""
        return self.post(self.couple_base + cpid + '/restore', nojson=True)

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Spouses,)
