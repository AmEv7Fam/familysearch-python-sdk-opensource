# Python imports

# Magic

class Places:
    def __init__(self):
        self.places_base = self.base + "/platform/places/"
    
    def places_search(self, q):
        url = self.places_base + "search?q=name:" + q
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def place_description(self, pdid, children=None):
        url = self.places_base + "description/" + pdid
        if children:
            url = url + "/chilrdren"
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def place_group(self, pgid):
        url = self.places_base + "gropus/" + pgid
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def place(self, pid):
        url = self.places_base + str(pid)
        response = self._request(url)
        response = self._fs2py(response)
        return response
     
    def place_type(self, ptid):
        url = self.places_base + "types/" + ptid
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def place_type_group(self, ptgid):
        url = self.places_base + "type-gropus/" + ptgid
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def place_types(self):
        url = self.places_base + "types"
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def place_type_groups(self):
        url = self.places_base + "type-groups"
        response = self._request(url)
        response = self._fs2py(response)
        return response

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Places,)