# Python imports

# Magic

class ChangeHistory:
    def __init__(self):
        pass
        
    def person_change_history(self, pid):
        url = self.tree_base + "persons/" + pid + "/changes"
        response = self._request(url)
        response = self._fs2py(response, 'users')
        return response
    
    def capr_change_history(self, caprid):
        url = self.tree_base + "child-and-parents-relationships/"\
              + caprid + "/changes"
        response = self._request(url)
        response = self._fs2py(response, 'users')
        return response
    
    def cr_change_history(self, crid):
        url = self.tree_base + "couple-relationships/" + crid + "/changes"
        response = self._request(url)
        response = self._fs2py(response, 'users')
        return response
    
    def restore_change(self, chid):
        pass # TODO

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (ChangeHistory,)