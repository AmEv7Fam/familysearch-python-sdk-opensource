# Python imports

# Magic

class Notes:
    def __init__(self):
        pass
    
    def create_person_note(self, pid, data):
        url = person_base + pid + "/notes"
        response = self._request(url, data)
        return dict(response.info())
    
    def get_list_person_note(self, pid):
        return self.get(person_base + pid + "/notes")
    
    def read_person_note(self, pid, nid):
        return self.get(person_base + pid + "/notes/" + nid)
    
    def update_person_note(self, nid, data):
        url = person_base + pid + "/notes/" + nid
        response = self._request(url, data)
        return dict(response.info())
    
    def delete_person_note(self, pid, nid):
        url = person_base + pid + "/notes/" + nid
        response = self._request(url, method="DELETE")
        return dict(response.info())
    
    def create_couple_note(self, crid, data):
        url = couple_base + crid + "/notes"
        response = self._request(url, data)
        return dict(response.info())
    
    def list_couple_note(self, crid):
        return self.get(couple_base + crid + "/notes")
    
    def read_couple_note(self, crid, nid):
        return self.get(couple_base + crid + "/notes/" + nid)
    
    def update_couple_note(self, crid, data):
        url = couple_base + crid + "/notes/" + nid
        response = self._request(url, data)
        return dict(response.info())
    
    def delete_couple_note(self, crid, nid):
        url = couple_base + crid + "/notes/" + nid
        response = self._request(url, method="DELETE")
        return dict(response.info())
    
    def create_child_note(self, cprid, data):
        url = child_base + cprid + "/notes"
        response = self._request(url, data)
        return dict(response.info())
    
    def list_child_note(self, cprid):
        return self.get(couple_base + cprid + "/notes")
    
    def read_child_note(self, cprid, nid):
        return self.get(person_base + cprid + "/notes/" + nid)
    
    def update_child_note(self, cprid, data):
        url = couple_base + cprid + "/notes/" + nid
        response = self._request(url, data)
        return dict(response.info())
    
    def delete_child_note(self, cprid, nid):
        url = couple_base + cprid + "/notes/" + nid
        response = self._request(url, method="DELETE")
        return dict(response.info())

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Notes,)