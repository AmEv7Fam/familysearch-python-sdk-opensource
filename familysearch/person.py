# Python imports

# Magic

class Person:
    def __init__(self):
        self.person_base = self.tree_base + 'persons/'
        
    def create_person(self, data):
        url = self.tree_base + 'persons'
        response = self._request(url, data)
        return dict(response.info())
    
    def read_person(self, pid):
        url = self.person_base + pid
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def delete_person(self, pid, reason):
        url = self.person_base + pid
        response = self._request(url, headers={'X-Reason': reason}, method="DELETE")
        return dict(response.info())
    
    def restore_person(self, pid):
        url = self.person_base + pid + "/restore"
        response = self._request(url, method="POST", nojson=True)
        return dict(response.info())
    
    def parents(self, pid):
        url = self.person_base + pid + "/parents"
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def spouses(self, pid):
        url = self.person_base + pid + "/spouses"
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def children(self, pid):
        url = self.person_base + pid + "/children"
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def memories_query(self, pid):
        url = self.person_base + pid + '/memories'
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def person_portrait(self, pid):
        url = self.person_base + pid + '/portrait'
        response = self._request(url)
        response = self._fs2py(response)
        return response
        
    def person_portraits(self, pid):
        url = self.person_base + pid + '/portraits'
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def spouse_relationships(self, pid):
        url = self.person_base + pid + '/spouse-relationships'
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def child_relationships(self, pid):
        url = self.person_base + pid + '/child-relationships'
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def parent_relationships(self, pid):
        url = self.person_base + pid + '/parent_relationships'
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def person_with_relationships(self):
        url = self.tree_base + "persons-with-relationships?person=" + pid
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def person_conclusion(self, pid, data):
        url = self.person_base + pid
        response = self._request(url, data)
        return dict(response.info())
    
    def person_merge_analysis(self, pid, dpid):
        url = self.tree_base + pid + "/merges/" + dpid
        response = self._request(url)
        response = self._fs2py(request)
        return response
    
    def read_merge_constraint(self, pid, dpid):
        url = self.tree_base + pid + "/merges/" + dpid
        response = self._request(url, method="OPTIONS")
        return dict(response.info())
    
    def merge_duplicate(self, pid, dpid, data):
        url = self.tree_base + pid + "/merges/" + dpid
        response = self._request(url, data)
        return dict(response.info())
    
    def person_change_summary(self, pid):
        url = tree_base + "persons/" + pid + '/change-summary'
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def read_preferred_spouse_relationship(self, pid):
        url = self.tree_base + "/users/" + self.current_user()['treeUserId'] + \
            "/preferred-spouse-relationships/" + pid
        response = self._request(url)
        return dict(response.info())
    
    def update_preferred_spouse_relationship(self, pid, crid):
        url = self.tree_base + "/users/" + self.current_user()['treeUserId'] + \
            "/preferred-spouse-relationships/" + pid
        response = self._request(url, headers={"Location": self.tree_base + \
            "/couple-relationships/" + crid}, method="PUT")
        return dict(response.info())
    
    def delete_preferred_spouse_relationship(self, uid, pid):
        url = self.tree_base + "/users/" + self.current_user()['treeUserId'] + \
            "/preferred-spouse-relationships/" + pid
        response = self._request(url, method="DELETE")
        return dict(response.info())
    
    def read_preferred_parent_relationship(self, pid):
        url = self.tree_base + "/users/" + self.current_user()['treeUserId'] + \
            "/preferred-parent-relationships/" + pid
        response = self._request(url)
        return dict(response.info())
    
    def update_preferred_parent_relationship(self, pid, crid):
        url = self.tree_base + "/users/" + self.current_user()['treeUserId'] + \
            "/preferred-parent-relationships/" + pid
        response = self._request(url, headers={"Location": self.tree_base + \
            "/couple-relationships/" + crid}, method="PUT")
        return dict(response.info())
    
    def delete_preferred_parent_relationship(self, uid, pid):
        url = self.tree_base + "/users/" + self.current_user()['treeUserId'] + \
            "/preferred-parent-relationships/" + pid
        response = self._request(url, method="DELETE")
        return dict(response.info())
    
    
# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Person,)