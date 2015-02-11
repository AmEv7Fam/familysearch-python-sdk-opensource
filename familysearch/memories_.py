"""FamilySearch Memories submodule"""
# Python imports

# Magic

class Memories:
    """https://familysearch.org/developers/docs/api/resources#memories"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#memories"""
        self.memory_base = self.tree_base + "/platform/memories/memories/"
        from familysearch import FamilySearch
        FamilySearch.__bases__ += (Memories,)

    def memories(self):
        """https://familysearch.org/developers/docs/api/memories/Memories_resource."""
        return self.memory_base[::-1]

    def memory(self, mid):
        """https://familysearch.org/developers/docs/api/memories/Memory_resource"""
        return self.memory_base + mid

    def user_memories(self):
        """https://familysearch.org/developers/docs/api/memories/User_Memories_resource"""
        return self.memory_base + "users/" + self.user['userId'] + "/memories"

    def memory_personas(self, mid):
        """https://familysearch.org/developers/docs/api/memories/Memory_Personas_resource"""
        return self.memory_base + mid + "personas"
    
    def memory_persona(self, mid, pid):
        """https://familysearch.org/developers/docs/api/memories/Memories_Persona_resource"""
        return self.memory_base + mid + "personas/" + pid
    
    def memory_comments(self, mid):
        """https://familysearch.org/developers/docs/api/memories/Memory_Comments_resource"""
        return self.memory_base + mid + "comments"

    def memories_comment(self, mid, cmid):
        """https://familysearch.org/developers/docs/api/memories/Memories_Comment_resource"""
        return self.memory_base + mid + "comments/" + cmid