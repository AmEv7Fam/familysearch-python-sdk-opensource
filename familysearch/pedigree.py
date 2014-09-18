# Python imports

# Magic

class Pedigree:
    def __init__(self):
        pass
        
    def ancestry(self, pid, person=False, spouse=None, marriage=False,
                 generations=None):
        url = self.tree_base + 'ancestry.json?person=' + pid
        if person:
            url = url + "&personDetails="
        if marriage:
            url = url + "&marriageDetails="
        if spouse:
            url = url + '&spouse=' + spouse
        if generations:
         url = url + '&generations' + str(generations)
        response = self._request(url)
        response = self._fs2py(response, 'persons')
        return response
    
    def descendancy(self, pid):
        pass # TODO

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Pedigree,)