# Python imports

# Magic

class Sources:
    def __init__(self):
        self.source_base = self.base + "/platform/sources/"
    
    # OK, these next two functions hit the same endpoint... do we need both?
    def create_source_description(self, data):
        return self.post(source_base + "/descriptions", data)
    
    def create_user_source(self, data):
        return self.post(source_base + "/descriptions", data)
    
    def read_source_description(self, sid):
        return self.get(self.source_base + "descriptions/" + sid)
    
    def update_source_description(self, sid, data):
        return self._request(self.source_base + "descriptions/" + sid, data)
    
    def delete_source_description(self, sid, reason):
        return self.delete(self.source_base + "descriptions/" + sid, headers={"X-Reason": reason})
    
    def get_spouse_relatioship_sources(self, crid):
        return self.get(self.tree_base + 'couple-relationships/' + crid)
    
    def create_person_source_reference(self, pid, data):
        return self.post(self.person_base + pid + "/source-references", data)
    
    def get_person_source_reference(self, pid, srid):
        return self.get(self.person_base + pid + "/source-references/" + srid)
    
    def delete_person_source_reference(self, pid, srid, reason=""):
        return self.delete(self.person_base + pid + "/source-references/" + srid, headers={"X-Reason": reason})
    
    def get_person_sources(self, pid):
        return self.get(self.person_base + pid + "/sources")
    
    def get_spouse_relatioship_sources(self, crid):
        return fs.get(self.tree_base + 'couple-relationships/' + crid)
    
    def create_spouse_relationship_source_reference(self, crid, data):
        return self._request(self.tree_base + 'ccouple-relationships/' + crid\
              + "/source-references/", data)
    
    def get_spouse_relationship_source_reference(self, crid, srid):
        return self.get(self.tree_base + 'couple-relationships/' + crid\
              + "/source-references/" + srid)
    
    def delete_spouse_relationship_source_reference(self, crid, srid, reason=""):
        return self.delete(self.tree_base + 'couple-relationships/' + crid\
              + "/source-references/" + srid, headers={"X-Reason": reason})
    
    def get_child_relatioship_sources(self, crid):
        return self.get(self.tree_base + 'child-and-parents-relationships/' + crid)
    
    def create_child_relationship_source_reference(self, crid, data):
        return self.post(self.tree_base + 'child-and-parents-relationships/' + crid\
              + "/source-references/", data)
    
    def get_child_relationship_source_reference(self, crid, srid):
        return self.get(self.tree_base + 'child-and-parents-relationships/' + crid\
              + "/source-references/" + srid)
    
    def delete_child_relationship_source_reference(self, crid, srid, reason=""):
        return self.delete(self.tree_base + 'child-and-parents-relationships/' + crid\
              + "/source-references/" + srid, headers={"X-Reason": reason})
    
    def get_source_references(self, srid):
        return self.get(self.tree_base + "source-references?source=" + srid)

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Sources,)