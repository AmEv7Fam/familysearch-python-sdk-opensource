# -*- coding: utf-8 -*-

"""FamilySearch Places submodule"""

# Python imports

# Magic


class Places:
    """https://familysearch.org/developers/docs/api/resources#places"""

    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#places"""

        self.places_base = self.base + "/platform/places/"

    def places_search(self, **kwargs):
        """https://familysearch.org/developers/docs/api/places/Places_Search_resource"""

        return self._add_query_params(self.places_base + "search", kwargs)

    def place_description(self, pdid):
        """https://familysearch.org/developers/docs/api/places/Place_Description_resource"""

        return self.places_base + "description/" + pdid

    def place_group(self, pgid):
        """https://familysearch.org/developers/docs/api/places/Place_Group_resource"""

        return self.places_base + "groups/" + pgid

    def place(self, pid):
        """https://familysearch.org/developers/docs/api/places/Place_resource"""

        return self.places_base + pid

    def place_description_children(self):
        """https://familysearch.org/developers/docs/api/places/Place_Description_Children_resource"""
        return self.places_base + "description/" + pdid + "/children"

    def place_type(self, ptid):
        """https://familysearch.org/developers/docs/api/places/Place_Type_resource"""

        return self.places_base + "types/" + ptid

    def place_type_group(self, ptgid):
        """https://familysearch.org/developers/docs/api/places/Place_Type_Group_resource"""

        return self.places_base + "type-groups/" + ptgid

    def place_types(self):
        """https://familysearch.org/developers/docs/api/places/Place_Types_resource"""

        return self.places_base + "types"

    def place_type_groups(self):
        """https://familysearch.org/developers/docs/api/places/Place_Type_Groups_resource"""

        return self.places_base + "type-groups"
