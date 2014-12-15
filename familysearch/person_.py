# Python imports

# Magic

class Person:
    def __init__(self):
        self.person_base = self.tree_base + 'persons/'
        
    def create_person(self, data):
        url = self.tree_base + 'persons'
        response = self._request(url, data)
        return dict(response.info())
    
    def get_person(self, pid):
        return self.get(self.person_base + pid)
    
    def delete_person(self, pid, reason):
        url = self.person_base + pid
        response = self._request(url, headers={'X-Reason': reason}, method="DELETE")
        return dict(response.info())
    
    def restore_person(self, pid):
        url = self.person_base + pid + "/restore"
        response = self._request(url, method="POST", nojson=True)
        return dict(response.info())
    
    def get_parents(self, pid):
        return self.get(self.person_base + pid + "/parents")
    
    def get_spouses(self, pid):
        return self.get(self.person_base + pid + "/spouses")
    
    def get_children(self, pid):
        return self.get(self.person_base + pid + "/children")
    
    def get_memories_query(self, pid):
        return self.get(self.person_base + pid + '/memories')
    
    def get_person_portrait(self, pid):
        return self.get(self.person_base + pid + '/portrait')
        
    def get_person_portraits(self, pid):
        return self.get(self.person_base + pid + '/portraits')
    
    def get_spouse_relationships(self, pid):
        return self.get(self.person_base + pid + '/spouse-relationships')
    
    def get_child_relationships(self, pid):
        return self.get(self.person_base + pid + '/child-relationships')
    
    def get_parent_relationships(self, pid):
        return self.get(self.person_base + pid + '/parent_relationships')
    
    def get_person_with_relationships(self):
        return self.get(self.tree_base + "persons-with-relationships?person=" + pid)
    
    def get_person_conclusion(self, pid, data):
        url = self.person_base + pid
        response = self._request(url, data)
        return dict(response.info())
    
    def get_merge_constraint(self, pid, dpid):
        return self.get(self.person_base + pid + "/merges/" + dpid)
    
    def options_merge_constraint(self, pid, dpid):
        url = self.person_base + pid + "/merges/" + dpid
        response = self._request(url, method="OPTIONS")
        return dict(response.info())
    
    def post_merge_duplicate(self, pid, dpid, data):
        url = self.tree_base + pid + "/merges/" + dpid
        response = self._request(url, data)
        return dict(response.info())
    
    def get_person_change_summary(self, pid):
        return self.get(tree_base + "persons/" + pid + '/change-summary')
    
    def read_preferred_spouse_relationship(self, pid):
        url = self.tree_base + "/users/" + self.current_user()['treeUserId'] + \
            "/preferred-spouse-relationships/" + pid
        response = self._request(url)
        return dict(response.info())
    
    def update_preferred_spouse_relationship(self, pid, crid):
        url = self.tree_base + "/users/" + self.user['treeUserId'] + \
            "/preferred-spouse-relationships/" + pid
        response = self._request(url, headers={"Location": self.tree_base + \
            "/couple-relationships/" + crid}, method="PUT")
        return dict(response.info())
    
    def delete_preferred_spouse_relationship(self, uid, pid):
        url = self.tree_base + "/users/" + self.user['treeUserId'] + \
            "/preferred-spouse-relationships/" + pid
        response = self._request(url, method="DELETE")
        return dict(response.info())
    
    def read_preferred_parent_relationship(self, pid):
        url = self.tree_base + "/users/" + self.user['treeUserId'] + \
            "/preferred-parent-relationships/" + pid
        response = self._request(url)
        return dict(response.info())
    
    def update_preferred_parent_relationship(self, pid, crid):
        url = self.tree_base + "/users/" + self.user['treeUserId'] + \
            "/preferred-parent-relationships/" + pid
        response = self._request(url, headers={"Location": self.tree_base + \
            "/couple-relationships/" + crid}, method="PUT")
        return dict(response.info())
    
    def delete_preferred_parent_relationship(self, uid, pid):
        url = self.tree_base + "/users/" + self.user['treeUserId'] + \
            "/preferred-parent-relationships/" + pid
        response = self._request(url, method="DELETE")
        return dict(response.info())
    
    
# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Person,)
