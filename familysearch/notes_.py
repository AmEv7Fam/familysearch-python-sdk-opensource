# Python imports

# Magic

class Notes:
    def __init__(self):
        pass
    
    def create_person_note(self, pid, data):
        return self.post(person_base + pid + "/notes", data)
    
    def get_list_person_note(self, pid):
        return self.get(person_base + pid + "/notes")
    
    def read_person_note(self, pid, nid):
        return self.get(person_base + pid + "/notes/" + nid)
    
    def update_person_note(self, nid, data):
        return self.post(person_base + pid + "/notes/" + nid, data)
    
    def delete_person_note(self, pid, nid):
        return self.delete(person_base + pid + "/notes/" + nid)
    
    def create_couple_note(self, crid, data):
        return self.post(couple_base + crid + "/notes", data)
    
    def list_couple_note(self, crid):
        return self.get(couple_base + crid + "/notes")
    
    def read_couple_note(self, crid, nid):
        return self.get(couple_base + crid + "/notes/" + nid)
    
    def update_couple_note(self, crid, data):
        response = self.post(urlcouple_base + crid + "/notes/" + nid, data)
    
    def delete_couple_note(self, crid, nid):
        return self.delete(couple_base + crid + "/notes/" + nid)
    
    def create_child_note(self, cprid, data):
        return self.post(child_base + cprid + "/notes", data)
    
    def list_child_note(self, cprid):
        return self.get(couple_base + cprid + "/notes")
    
    def read_child_note(self, cprid, nid):
        return self.get(person_base + cprid + "/notes/" + nid)
    
    def update_child_note(self, cprid, data):
        response = self.post(couple_base + cprid + "/notes/" + nid, data)
    
    def delete_child_note(self, cprid, nid):
        return self.delete(couple_base + cprid + "/notes/" + nid)

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Notes,)