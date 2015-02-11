"""FamilySearch Source Box submodule"""
# Python imports

# Magic

# Source box 

class SourceBox:
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#source-box"""
        self.source_base = self.base + "/platform/sources/"
        from familysearch import FamilySearch
        FamilySearch.__bases__ += (SourceBox,)

    def read_specific_user_collections(self, uid):
        """Obsolete."""
        return self.get(self.source_base+uid+"/collections")

    def post_user_collection(self, data):
        """Obsolete."""
        return self.get(self.source_base+"collections", data, method="POST")

    def post_user_collection(self, udsid, data):
        """Obsolete."""
        return self.get(
          self.source_base+"collections/"+udsid, data, method="POST")

    def delete_user_collection(self, udsid, data):
        """Obsolete."""
        return self.delete(self.source_base + "collections/" + udsid, data)

    def ud_collection_source_descriptions(self):
        """Obsolete."""
        pass # TODO https://familysearch.org/developers/docs/api/sources/User-Defined_Collection_Source_Descriptions_resource

    def ud_collections_source_descriptions_user(self):
        """Obsolete."""
        pass # TODO https://familysearch.org/developers/docs/api/sources/User-Defined_Collections_Source_Descriptions_for_a_User_resource
