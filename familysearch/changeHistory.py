# Python imports

# Magic

class ChangeHistory:
    def __init__(self):
        pass
        
    def get_person_change_history(self, pid):
        url = self.tree_base + "persons/" + pid + "/changes"
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def get_child_change_history(self, caprid):
        url = self.tree_base + "child-and-parents-relationships/"\
              + caprid + "/changes"
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def get_read_couple_change_history(self, crid):
        url = self.tree_base + "couple-relationships/" + crid + "/changes"
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def restore_change(self, chid):
        url = self.tree_base + "changes/" + chid + "/restore"
        response = self._request(url, method="POST")
        return dict(response.info())

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (ChangeHistory,)