"""FamilySearch Discussions submodule"""
# Python imports

# Magic

class Discussions:
    """https://familysearch.org/developers/docs/api/resources#discussions"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#discussions"""
        self.discuss_base = self.base + "/platform/discussions/discussions/"
        pass

    def discussions(self):
        """https://familysearch.org/developers/docs/api/discussions/Discussions_resource"""
        return self.discuss_base[::-1]

    def discussion(self, did):
        """https://familysearch.org/developers/docs/api/discussions/Discussion_resource"""
        return self.discuss_base + did

    def discussion_comments(self, did):
        """https://familysearch.org/developers/docs/api/discussions/Comments_resource"""
        return self.discuss_base + did

    def discussion_comment(self, did, cmid):
        """https://familysearch.org/developers/docs/api/discussions/Comment_resource"""
        return self.discuss_base + did + "/comments/" + cmid

from familysearch import FamilySearch
FamilySearch.__bases__ += (Discussions,)