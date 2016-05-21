# -*- coding: utf-8 -*-

"""FamilySearch Search and Match submodule"""

# Python imports

# Magic


class SearchAndMatch:
    """https://familysearch.org/developers/docs/api/resources#search-and-match"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#search-and-match"""

    def person_search(self, **kwargs):
        """https://familysearch.org/developers/docs/api/tree/Person_Search_resource"""
        return self._add_query_params(self.tree_base + "search", kwargs)

    def person_matches(self, pid, **kwargs):
        """https://familysearch.org/developers/docs/api/tree/Person_Matches_resource"""
        return self._add_query_params(
            self.tree_base + "persons/" + pid + "/matches", kwargs)

    def person_not_a_match_list(self, pid):
        """https://familysearch.org/developers/docs/api/tree/Person_Not_A_Match_List_resource"""
        return self.tree_base + "persons/" + pid + "/not-a-match"

    def person_matches_query(self, **kwargs):
        """https://familysearch.org/developers/docs/api/tree/Person_Matches_Query_resource"""
        return self._add_query_params(self.tree_base + "matches", kwargs)
