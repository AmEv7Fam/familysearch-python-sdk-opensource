"""FamilySearch Person submodule"""
# Python imports

# Magic

class Person:
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#person"""
        self.person_base = self.tree_base + 'persons/'

    def create_person(self, data):
        """Obsolete."""
        return self.post(self.tree_base+'persons', data)

    def get_person(self, pid):
        """Obsolete."""
        return self.get(self.person_base+pid)

    def delete_person(self, pid, reason):
        """Obsolete."""
        return self.delete(self.person_base+pid, headers={'X-Reason': reason})

    def restore_person(self, pid):
        """Obsolete."""
        return self.post(self.person_base+pid+"/restore", nojson=True)

    def get_parents(self, pid):
        """Obsolete."""
        return self.get(self.person_base+pid+"/parents")

    def get_spouses(self, pid):
        """Obsolete."""
        return self.get(self.person_base+pid+"/spouses")

    def get_children(self, pid):
        """Obsolete."""
        return self.get(self.person_base+pid+"/children")

    def get_memories_query(self, pid):
        """Obsolete."""
        return self.get(self.person_base+pid+'/memories')

    def get_person_portrait(self, pid):
        """Obsolete."""
        return self.get(self.person_base+pid+'/portrait')

    def get_person_portraits(self, pid):
        """Obsolete."""
        return self.get(self.person_base+pid+'/portraits')

    def get_spouse_relationships(self, pid):
        """Obsolete."""
        return self.get(self.person_base+pid+'/spouse-relationships')

    def get_child_relationships(self, pid):
        """Obsolete."""
        return self.get(self.person_base+pid+'/child-relationships')

    def get_parent_relationships(self, pid):
        """Obsolete."""
        return self.get(self.person_base+pid+'/parent_relationships')

    def get_person_with_relationships(self):
        """Obsolete."""
        return self.get(self.tree_base+"persons-with-relationships?person="+pid)

    def get_person_conclusion(self, pid, data):
        """Obsolete."""
        return self._request(self.person_base + pid, data)

    def get_merge_constraint(self, pid, dpid):
        """Obsolete."""
        return self.get(self.person_base+pid+"/merges/"+dpid)

    def options_merge_constraint(self, pid, dpid):
        """Obsolete."""
        return self.options(self.person_base+pid+"/merges/"+dpid)

    def post_merge_duplicate(self, pid, dpid, data):
        """Obsolete."""
        return self._post(self.tree_base+pid+"/merges/"+dpid, data)

    def get_person_change_summary(self, pid):
        """Obsolete."""
        return self.get(tree_base + "persons/" + pid + '/change-summary')

    def get_preferred_spouse_relationship(self, pid):
        """Obsolete."""
        return self.get(
          self.tree_base+"/users/"+self.user['treeUserId']+
          "/preferred-spouse-relationships/"+pid)

    def update_preferred_spouse_relationship(self, pid, crid):
        """Obsolete."""
        return self.put(
          self.tree_base+"/users/"+self.user['treeUserId']+
          "/preferred-spouse-relationships/"+pid,
          headers={"Location": self.tree_base+"/couple-relationships/"+crid})

    def delete_preferred_spouse_relationship(self, pid):
        """Obsolete."""
        return self.delete(
          self.tree_base + "/users/"+self.user['treeUserId']+
          "/preferred-spouse-relationships/" + pid)

    def get_preferred_parent_relationship(self, pid):
        """Obsolete."""
        return self.get(
          self.tree_base+"/users/"+self.user['treeUserId']+
          "/preferred-parent-relationships/" + pid)

    def update_preferred_parent_relationship(self, pid, crid):
        """Obsolete."""
        return self.put(
          self.tree_base + "/users/"+self.user['treeUserId']+
          "/preferred-parent-relationships/"+pid,
          headers={"Location": self.tree_base+"/couple-relationships/"+crid})

    def delete_preferred_parent_relationship(self, pid):
        """Obsolete."""
        return self.delete(
          self.tree_base+"/users/"+self.user['treeUserId']+
          "/preferred-parent-relationships/"+pid)
    
    
# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Person,)
