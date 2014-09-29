# Python imports

# Magic

class Sources:
    def __init__(self):
        self.source_base = self.base + "/platform/sources/"
    
    def create_source_description(self):
        url = source_base + "/descriptions"
        response = self._request(url, data)
        return dict(response.info())
    
    def create_user_source(self, data):
        url = source_base + "/descriptions"
        response = self._request(url, data)
        return dict(response.info())
    
    def read_source_description(self, sid):
        url = self.source_base + "descriptions/" + sid
        response = self._request(url)
        return dict(response.info())
    
    def update_source_description(self, sid, data):
        url = self.source_base + "descriptions/" + sid
        response = self._request(url, data)
        return dict(response.info())
    
    def delete_source_description(self, sid, reason):
        url = self.source_base + "descriptions/" + sid
        response = self._request(url, headers={"X-Reason": reason}, method="DELETE")
        return dict(response.info())
    
    def read_spouse_relatioship_sources(self, crid):
        url = self.tree_base + 'couple-relationships/' + crid
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def create_person_source_reference(self, pid, data):
        url = self.person_base + pid + "/source-references"
        response = self._request(url, data)
        return dict(response.info())
    
    def read_person_source_reference(self, pid, srid):
        url = self.person_base + pid + "/source-references/" + srid
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def delete_person_source_reference(self, pid, srid, reason=""):
        url = self.person_base + pid + "/source-references/" + srid
        response = self._request(url, headers={"X-Reason": reason}, method="DELETE")
        return dict(response.info())
    
    def read_person_sources(self, pid):
        url = self.person_base + pid + "/sources"
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def read_spouse_relatioship_sources(self, crid):
        url = self.tree_base + 'couple-relationships/' + crid
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def create_spouse_relationship_source_reference(self, crid, data):
        url = self.tree_base + 'ccouple-relationships/' + crid\
              + "/source-references/"
        response = self._request(url, data)
        return dict(response.info())
    
    def read_spouse_relationship_source_reference(self, crid, srid):
        url = self.tree_base + 'couple-relationships/' + crid\
              + "/source-references/" + srid
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def delete_spouse_relationship_source_reference(self, crid, srid, reason=""):
        url = self.tree_base + 'couple-relationships/' + crid\
              + "/source-references/" + srid
        response = self._request(url, headers={"X-Reason": reason}, method="DELETE")
        return dict(response.info())
    
    def read_child_relatioship_sources(self, crid):
        url = self.tree_base + 'child-and-parents-relationships/' + crid
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def create_child_relationship_source_reference(self, crid, data):
        url = self.tree_base + 'child-and-parents-relationships/' + crid\
              + "/source-references/"
        response = self._request(url, data)
        return dict(response.info())
    
    def read_child_relationship_source_reference(self, crid, srid):
        url = self.tree_base + 'child-and-parents-relationships/' + crid\
              + "/source-references/" + srid
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def delete_child_relationship_source_reference(self, crid, srid, reason=""):
        url = self.tree_base + 'child-and-parents-relationships/' + crid\
              + "/source-references/" + srid
        response = self._request(url, headers={"X-Reason": reason}, method="DELETE")
        return dict(response.info())
    
    def read_source_references(self, srid):
        url = self.tree_base + "source-references?source=" + srid
        response = self._request(url)
        response = self._fs2py(response)
        return response

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Sources,)