# Python imports

# Magic

class Memories:
    def __init__(self):
        self.memories_base = self.base + "/platform/memories/"
    
    def create_memory(self):
        pass # TODO
    
    def memory(self):
        pass # TODO
    
    def memory_persona(self):
        pass # TODO
    
    def memory_artifact_reference(self):
        pass # TODO
    
    def user_memories_query(self):
        pass # TODO
    
    def person_memory_references(self):
        pass # TODO
    
    def person_memory_reference(self):
        pass # TODO
    
    def memory_comments(self):
        pass # TODO
    
    def memories_comment(self):
        pass # TODO

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Memories,)