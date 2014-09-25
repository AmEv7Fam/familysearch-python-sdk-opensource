# Python imports

# Magic

class SearchAndMatch:
    def __init__(self):
        pass
    
    def person_search(self, query, **kwargs):
        url = tree_base + "search"
        url = self._add_query_params(url, query)
        url = self._add_query_params(url, kwargs)
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def person_matches(self, pid, query, **kwargs):
        url = person_base + pid + "/matches"
        url = self._add_query_params(url, query)
        url = self._add_query_params(url, kwargs)
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def person_matches_query(self, query, **kwargs):
        url = tree_base + "matches"
        url = self._add_query_params(url, query)
        url = self._add_query_params(url, kwargs)
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def read_person_not_a_match(self, pid):
        url = self.person_base + pid + "/not-a-match"
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
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