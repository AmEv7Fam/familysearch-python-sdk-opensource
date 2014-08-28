# Python imports

# Magic

class Pedigree:
    def __init__(self):
        pass
        
    def ancestry(self, pid, person=False, spouse=None, marriage=False):
        url = self.tree_base + 'ancestry.json?person=' + pid
        if person:
            url = url + "&personDetails="
        if marriage:
            url = url + "&marriageDetails="
        if spouse:
            url = url + '&spouse=' + spouse
        response = self._request(url)
        response = self._fs2py(response, 'persons')
        return response
    
    def descendancy(self, pid):
        pass # TODO

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Pedigree,)