"""FamilySearch Vocabularies submodule"""
# Python imports

# Magic

class Sources:
    """https://familysearch.org/developers/docs/api/resources#sources"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#sources"""
        self.source_base = self.base + "/platform/sources/"

    def source_descriptions(self):
        """https://familysearch.org/developers/docs/api/sources/Source_Descriptions_resource"""
        return self.source_base + "descriptions"

    def source_description(self, sdid):
        """https://familysearch.org/developers/docs/api/sources/Source_Description_resource"""
        return self.source_base + "descriptions/" + sdid

    def source_folders(self):
        """https://familysearch.org/developers/docs/api/sources/Source_Folders_resource"""
        return self.source_base + "collections"

    def source_folder(self, udcid):
        """https://familysearch.org/developers/docs/api/sources/Source_Folder_resource"""
        return self.source_base + "collections/" + udcid

    def source_folder_source_descriptions(self, udcid):
        """https://familysearch.org/developers/docs/api/sources/Source_Folder_Source_Descriptions_resource"""
        return self.source_base + "collections/" + udcid + "/descriptions"

    def user_source_folders(self):
        """https://familysearch.org/developers/docs/api/sources/User_Source_Folders_resource"""
        return self.source_base + self.user['personId'] + "/collections"

    def user_source_descriptions(self):
        """https://familysearch.org/developers/docs/api/sources/User_Source_Descriptions_resource"""
        return self.source_base + self.user['personId'] + "/collections"

    def source_references_query(self):
        """https://familysearch.org/developers/docs/api/tree/Source_References_Query_resource"""
        return self.tree_base + "source_references"

from familysearch import FamilySearch
FamilySearch.__bases__ += (Sources,)