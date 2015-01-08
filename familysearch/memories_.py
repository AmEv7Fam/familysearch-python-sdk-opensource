# pylint: disable=no-member, cyclic-import, import-error
# Python imports

# Magic

class Memories:
    def __init__(self):
        self.memories_base = self.base + "/platform/memories/"
    
    def post_memory(self, title, data, headers):
        return self.post(memories_base[:-1] + "?title=" + title, data, headers, nojson=True)
    
    def read_memory(self, mid):
        return self.get(self.memories_base + mid)
        
    def update_memory_description(self, mid, data):
        return self.post(self.memories_base + mid, data)
    
    def delete_memory(self, mid):
        return self.delete(self.memories_base + mid)
    
    def post_memory_persona(self, mid, data):
        return self.post(self.memories_base + mid + "/personas", data)
    
    def get_memory_personas(self, mid):
        return self.get(self.memories_base + mid + "/personas")
    
    def get_memory_persona(self, mid, pid):
        return self.get(self.memories_base + mid + "/personas/"+ pid)
    
    def update_memory_persona(self, mid, pid):
        return self._request(self.memories_base + mid + "/personas/" + pid)
    
    def delete_memory_persona(self, mid, pid):
        return self.delete(self.memories_base + mid + "/personas/" + pid)
    
    def create_user_memories_reference(self, pid, data):
        return self.post(person_base + pid + "/memory-references", data)
    
    def read_user_memories_reference(self, pid):
        return self.get(self.person_base + pid + "/memory-references")
    
    def delete_user_memories_reference(self, pid, erid):
        return self._request(self.person_base + pid + "/memory-references/" + erid)
        
    def create_memory_comment(self, mid, data):
        return self.post(self.memories_base + mid + "/comments", data)
    
    def read_memory_comments(self, mid):
        return self.get(self.memories_base + mid + "/comments")
    
    def update_memory_comment(self, mid, data):
        return self.post(self.memories_base + mid + "/comments", data)
    
    def delete_memory_comment(self, mid, cmid):
        return self.delete(self.memories_base + mid + "/comments/" + cmid)

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Memories,)