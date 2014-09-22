# Python imports

# Magic

class Discussions:
    def __init__(self):
        self.discuss_base = self.base + "/platform/discussions/discussions/"
    
    def create_discussion(self, data):
        url = self.discuss_base[:-1]
        response = self._request(url, data)
        return dict(response.info())
    
    def read_discussion(self):
        url = self.discuss_base + did
        response = self._request(url)
        return dict(response.info)
    
    def update_discussion(self, did, data):
        url = self.discuss_base + did
        response = self._request(url, data)
        return dict(response.info())
    
    def delete_discussion(self, did):
        url = self.discuss_base + did
        response = self._request(url, method="DELETE")
        return dict(response.info)
    
    def create_dicussion_comment(self, did, data):
        url = self.disuss_base + did + "/comments"
        response = self._request(url, data)
        return dict(response.info())
    
    def update_discussion_comment(self, did, data):
        url = self.disuss_base + did + "/comments"
        response = self._request(url, data)
        return dict(response.info())
    
    def delete_discussion_comment(self, did, num):
        url = self.disuss_base + did + "/comments/" + num
        response = self._request(url, data)
        return dict(response.info())
    
    def create_discussion_reference(self, pid, data):
        url = self.person_base + pid + "/discussion-references"
        response = self._request(url, data)
        return dict(response.info())
        
    def read_discussion_reference(self, pid):
        url = self.person_base + pid + "/discussion-references"
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def delete_discussion_reference(self, pid, drid):
        url = self.person_base + "/discussion-references/" + drid
        response = self._request(url, method="DELETE")
        return dict(response.info)

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Discussions,)