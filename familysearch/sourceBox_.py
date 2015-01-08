# pylint: disable=no-member, cyclic-import, import-error
# Python imports

# Magic

class SourceBox:
    def __init__(self):
        """"""
        self.source_base = self.base + "/platform/sources/"

    def read_specific_user_collections(self, uid):
        """"""
        return self.get(self.source_base+uid+"/collections")

    def post_user_collection(self, data):
        """"""
        return self.get(self.source_base+"collections", data, method="POST")

    def post_user_collection(self, udsid, data):
        """"""
        return self.get(
          self.source_base+"collections/"+udsid, data, method="POST")

    def delete_user_collection(self, udsid, data):
        """"""
        return self.delete(self.source_base + "collections/" + udsid, data)

    def ud_collection_source_descriptions(self):
        """"""
        pass # TODO https://familysearch.org/developers/docs/api/sources/User-Defined_Collection_Source_Descriptions_resource

    def ud_collections_source_descriptions_user(self):
        pass # TODO https://familysearch.org/developers/docs/api/sources/User-Defined_Collections_Source_Descriptions_for_a_User_resource

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (SourceBox,)
