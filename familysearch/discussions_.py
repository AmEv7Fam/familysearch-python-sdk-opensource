"""FamilySearch Discussions submodule"""
# Python imports

# Magic

class Discussions:
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#discussions"""
        self.discuss_base = self.base + "/platform/discussions/discussions/"

    def create_discussion(self, data):
        """Obsolete."""
        return self._request(self.discuss_base[:-1], data)

    def get_discussion(self):
        """Obsolete."""
        return self._request(self.discuss_base + did)

    def update_discussion(self, did, data):
        """Obsolete."""
        return self.get(self.discuss_base+did, data)

    def delete_discussion(self, did):
        """Obsolete."""
        return self.delete(self.discuss_base + did)

    def create_dicussion_comment(self, did, data):
        """Obsolete."""
        return self._request(self.disuss_base + did + "/comments", data)

    def update_discussion_comment(self, did, data):
        """Obsolete."""
        return self.post(self.disuss_base + did + "/comments", data)

    def delete_discussion_comment(self, did, num, data):
        """Obsolete."""
        return self.delete(self.disuss_base + did + "/comments/" + num, data)

    def create_discussion_reference(self, pid, data):
        """Obsolete."""
        return self.post(self.person_base+pid+"/discussion-references", data)

    def read_discussion_reference(self, pid):
        """Obsolete."""
        return self.get(self.person_base+pid+"/discussion-references")

    def delete_discussion_reference(self, drid):
        """Obsolete."""
        return self.delete(self.person_base+"/discussion-references/"+drid)

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Discussions,)
