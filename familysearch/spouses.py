# Python imports

# Magic

class Spouses:
    def __init__(self):
        self.couple_base = self.tree_base + 'couple-relationships/'
    
    def create_couple_relationship(self, data):
        url = self.tree_base + 'relationships'
        response = self._request(url, data)
        return dict(response.info())
    
    def get_couple_relationship(self, cpid):
        return self.get(self.couple_base + cpid)
    
    def couple_relationship_conclusion(self, cpid, data):
        url = self.couple_base + cpid
        response = self._request(url, data)
        return dict(response.info())
    
    def delete_couple_relationship_conclusion(self, cpid, cid, reason=None):
        url = self.couple_base + cpid + '/conclusions/' + cid
        response = self._request(url, headers={'X-Reason': reason}, method="DELETE")
        return dict(response.info())
    
    def delete_couple_relationship(self, cpid, reason=None):
        url = self.couple_base + cpid
        response = self._request(url, headers={'X-Reason': reason}, method="DELETE")
        return dict(response.info())
    
    def restore_couple_relationship(self, cpid):
        url = self.couple_base + cpid + '/restore'
        response = self._request(url, method="POST", nojson=True)
        return dict(response.info()) 
# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Spouses,)