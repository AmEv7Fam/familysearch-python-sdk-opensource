# Python imports

# Magic

class ChangeHistory:
    def __init__(self):
        pass
        
    def get_person_change_history(self, pid):
        return self.get(self.tree_base + "persons/" + pid + "/changes")
    
    def get_child_change_history(self, caprid):
        return self.get(self.tree_base + "child-and-parents-relationships/"\
              + caprid + "/changes")
    
    def get_read_couple_change_history(self, crid):
        return self.get(self.tree_base + "couple-relationships/" + crid + "/changes")
    
    def restore_change(self, chid):
        url = self.tree_base + "changes/" + chid + "/restore"
        response = self._request(url, method="POST")
        return dict(response.info())

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (ChangeHistory,)