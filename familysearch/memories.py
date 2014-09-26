# Python imports

# Magic

class Memories:
    def __init__(self):
        self.memories_base = self.base + "/platform/memories/"
    
    def upload_memory(self, filename, title, filetype, data):
        url = memories_base[:-1] + "?title=" + title
        response = self._request(url, data, {"Content-disposition": "attachment",
                                 "filename": filename,
                                 "Content-Type": filetype},
                                 nojson=True)
        return dict(response.info())
    
    def read_memory(self, mid):
        url = self.memories_base + mid
        response = self._request(url)
        response = self._fs2py(response)
        return response
        
    def update_memory_description(self, mid, data):
        url = self.memories_base + mid
        response = self._request(url, data)
        return dict(response.info())
    
    def delete_memory(self, mid):
        url = self.memories_base + mid
        response = self._request(url, method="DELETE")
        return dict(response.info())
    
    def create_memory_persona(self, mid, data):
        url = self.memories_base + mid + "/personas"
        response = self._request(url, data)
        return dict(response.info())
    
    def read_memory_personas(self, mid):
        url = self.memories_base + mid + "/personas"
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def read_memory_persona(self, mid, pid):
        url = self.memories_base + mid + "/personas/"+ pid
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def update_memory_persona(self, mid, pid):
        url = self.memories_base + mid + "/personas/"+ pid
        response = self._request(url)
        return dict(response.info())
    
    def delete_memory_persona(self, mid, pid):
        url = self.memories_base + mid + "/personas/" + pid
        response = self._request(url, method="DELETE")
        return dict(response.info())
    
    def create_user_memories_reference(self, pid, data):
        url = person_base + pid + "/memory-references"
        response = self._request(url, data)
        return dict(response.info())
    
    def read_user_memories_reference(self, pid):
        url = self.person_base + pid + "/memory-references"
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def delete_user_memories_reference(self, pid, erid):
        url = self.person_base + pid + "/memory-references/" + erid
        response = self._request(url, method="DELETE")
        return dict(response.info())
        
    def create_memory_comment(self, mid, data):
        url = self.memories_base + mid + "/comments"
        response = self._request(url, data)
        return dict(response.info())
    
    def read_memory_comments(self, mid):
        url = self.memories_base + mid + "/comments"
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def update_memory_comment(self, mid, data):
        url = self.memories_base + mid + "/comments"
        response = self._request(url, data)
        return dict(response.info())
    
    def delete_memory_comment(self, mid, cmid):
        url = self.memories_base + mid + "/comments/" + cmid
        response = self._request(url, method="DELETE")
        return dict(response.info())

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Memories,)