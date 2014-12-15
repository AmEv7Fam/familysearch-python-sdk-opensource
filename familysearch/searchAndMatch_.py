# Python imports

# Magic

class SearchAndMatch:
    def __init__(self):
        pass
    
    def get_person_search(self, query, **kwargs):
        return self.get(self._add_query_params(
            self.tree_base + "search", query, **kwargs))
    
    def get_person_matches(self, pid, query, **kwargs):
        return self.get(self._add_query_params(
            self.person_base + pid + "/matches" + "matches", query, **kwargs))
    
    def get_person_matches_query(self, query, **kwargs):
        return self.get(self._add_query_params(
            self.tree_base + "matches", query, **kwargs))
    
    def get_person_not_a_match(self, pid):
        return self.get(self.person_base + pid + "/not-a-match")
    
    def update_person_not_a_match(self, pid, dpid, reason=None):
        url = person_base + pid + "/not-a-match"
        data = {
            "persons": [ {
                "id": dpid,
                "changeMessage": reason
            }]
        }
        response = self._request(url, data)
        return dict(response.info())
    
    def delete_person_not_a_match(self, pid, dpid, reason=None):
        url = person_base + pid + "/not-a-match/" + dpid
        response = self._request(url, headers={"x-Reason":reason}, method="DELETE")
        return dict(response.info())

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (SearchAndMatch,)