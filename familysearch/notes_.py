"""FamilySearch Notes submodule"""
# Python imports

# Magic

class Notes:
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#notes"""
        from familysearch import FamilySearch
        FamilySearch.__bases__ += (Notes,)

    def create_person_note(self, pid, data):
        """Obsolete."""
        return self.post(person_base + pid + "/notes", data)

    def get_list_person_note(self, pid):
        """Obsolete."""
        return self.get(person_base + pid + "/notes")

    def read_person_note(self, pid, nid):
        """Obsolete."""
        return self.get(person_base + pid + "/notes/" + nid)

    def update_person_note(self, nid, data):
        """Obsolete."""
        return self.post(person_base + pid + "/notes/" + nid, data)

    def delete_person_note(self, pid, nid):
        """Obsolete."""
        return self.delete(person_base + pid + "/notes/" + nid)

    def create_couple_note(self, crid, data):
        """Obsolete."""
        return self.post(couple_base + crid + "/notes", data)

    def list_couple_note(self, crid):
        """Obsolete."""
        return self.get(couple_base + crid + "/notes")

    def read_couple_note(self, crid, nid):
        """Obsolete."""
        return self.get(couple_base + crid + "/notes/" + nid)

    def update_couple_note(self, crid, data):
        """Obsolete."""
        return self.post(urlcouple_base + crid + "/notes/" + nid, data)

    def delete_couple_note(self, crid, nid):
        """Obsolete."""
        return self.delete(couple_base + crid + "/notes/" + nid)

    def create_child_note(self, cprid, data):
        """Obsolete."""
        return self.post(child_base + cprid + "/notes", data)

    def list_child_note(self, cprid):
        """Obsolete."""
        return self.get(couple_base + cprid + "/notes")

    def read_child_note(self, cprid, nid):
        """Obsolete."""
        return self.get(person_base + cprid + "/notes/" + nid)

    def update_child_note(self, cprid, data):
        """Obsolete."""
        return self.post(couple_base + cprid + "/notes/" + nid, data)

    def delete_child_note(self, cprid, nid):
        """Obsolete."""
        return self.delete(couple_base + cprid + "/notes/" + nid)