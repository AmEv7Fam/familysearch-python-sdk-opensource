# Python imports

# Magic

class Pedigree:
    def __init__(self):
        pass
        
    def get_ancestry(self, pid, person=False, spouse=None, marriage=False,
                 generations=None):
        url = self.tree_base + 'ancestry?person=' + pid
        if person:
            url = url + "&personDetails="
        if marriage:
            url = url + "&marriageDetails="
        if spouse is not None:
            url = url + '&spouse=' + spouse
        if generations:
         url = url + '&generations' + str(generations)
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def get_descendancy(self, pid, person=False, spouse=None, marriage=False,
                    generations=None):
        url = self.tree_base + 'descendancy?person=' + pid
        if person:
            url = url + "&personDetails="
        if marriage:
            url = url + "&marriageDetails="
        if spouse is not None:
            url = url + '&spouse=' + spouse
        if generations:
         url = url + '&generations' + str(generations)
        response = self._request(url)
        response = self._fs2py(response)
        return response

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Pedigree,)