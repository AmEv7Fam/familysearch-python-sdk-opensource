"""FamilySearch Person submodule"""
# Python imports

# Magic

class Person:
    """https://familysearch.org/developers/docs/api/examples#person"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#person"""
        self.person_base = self.tree_base + 'persons/'

    def persons(self):
        """https://familysearch.org/developers/docs/api/tree/Persons_resource"""
        return self.person_base[::-1]

    def person(self, pid):
        """https://familysearch.org/developers/docs/api/tree/Person_resource"""
        return self.person_base + pid

    def person_parents(self, pid):
        """https://familysearch.org/developers/docs/api/tree/Parents_of_a_Person_resource"""
        return self.person_base + pid + "/parents"

    def person_spouses(self, pid):
        """https://familysearch.org/developers/docs/api/tree/Spouses_of_a_Person_resource"""
        return self.person_base + pid + "/spouses"

    def person_children(self, pid):
        """https://familysearch.org/developers/docs/api/tree/Children_of_a_Person_resource"""
        return self.get(self.person_base+pid+"/children")

    def spouse_relationships(self, pid, **kwargs):
        """https://familysearch.org/developers/docs/api/tree/Person_Relationships_to_Spouses_resource"""
        return self._add_query_params(
            self.person_base + pid + '/spouse-relationships', kwargs)

    def child_relationships(self, pid, **kwargs):
        """https://familysearch.org/developers/docs/api/tree/Relationships_to_Children_resource"""
        return self._add_query_params(
            self.person_base + pid + '/child-relationships', kwargs)

    def parent_relationships(self, pid, **kwargs):
        """https://familysearch.org/developers/docs/api/tree/Relationships_to_Parents_resource"""
        return self._add_query_params(
            self.person_base + pid + '/parent_relationships', kwargs)

    def person_with_relationships(self, **kwargs):
        """https://familysearch.org/developers/docs/api/tree/Person_With_Relationships_resource"""
        return self._add_query_params(
            self.tree_base + "persons-with-relationships", kwargs)

    def person_conclusion(self, pid, cid):
        """https://familysearch.org/developers/docs/api/tree/Person_Conclusion_resource"""
        return self.person_base + pid + "conclusions" + cid
    
    def person_source_references(self, pid):
        """https://familysearch.org/developers/docs/api/tree/Person_Source_References_resource"""
        return self.person_base + pid + "source-references"

    def person_source_reference(self, pid, srid):
        """https://familysearch.org/developers/docs/api/tree/Person_Source_References_resource"""
        return self.person_base + pid + "source-references/" + srid
    
    def person_sources_query(self, pid):
        """https://familysearch.org/developers/docs/api/tree/Person_Sources_Query_resource"""
        return self.person_base + pid + "sources"

    def person_note(self, pid, nid):
        """https://familysearch.org/developers/docs/api/tree/Person_Note_resource"""
        return self.person_base + pid + "notes" + nid

    def person_discussion_references(self, pid):
        """https://familysearch.org/developers/docs/api/tree/Person_Discussion_References_resource"""
        return self.person_base + pid + "/discussion_reference"

    def person_discussion_reference(self, pid, drid):
        """https://familysearch.org/developers/docs/api/tree/Person_Discussion_References_resource"""
        return self.person_base + pid + "/discussion_reference/" + drid

    def person_merge(self, pid, dpid, **kwargs):
        """https://familysearch.org/developers/docs/api/tree/Person_Merge_resource"""
        return self._add_query_params(
            self.person_base + pid + "/merges/" + dpid, kwargs)

    def person_change_summary(self, pid):
        """https://familysearch.org/developers/docs/api/tree/Person_Merge_resource"""
        return self.person_base + pid + "/change-summary"

    def person_not_a_match(self, pid, dpid):
        """https://familysearch.org/developers/docs/api/tree/Person_Not_A_Match_resource"""
        return self.person_base + pid + "/not-a-match/" + dpid

    def person_restore(self, pid):
        """https://familysearch.org/developers/docs/api/tree/Person_Restore_resource"""
        return self.person_base + pid + "/restore"

    def preferred_spouse_relationship(self, pid, uid=None):
        """https://familysearch.org/developers/docs/api/tree/Preferred_Spouse_Relationship_resource"""
        if uid is None:
            uid = self.user['userId']
        return self.user_base + uid + "/preferred-spouse-relationships/" + pid

    def preferred_parent_relationship(self, pid, uid=None):
        """https://familysearch.org/developers/docs/api/tree/Preferred_Parent_Relationship_resource"""
        if uid is None:
            uid = self.user['userId']
        return self.user_base + uid +"/preferred-parent-relationships/" + pid

    def person_memories(self, pid):
        """https://familysearch.org/developers/docs/api/tree/Person_Memories_resource"""
        return self._add_query_params(
            self.person_base + pid + "/memories", kwargs)

    def person_memory_references(self, pid):
        """https://familysearch.org/developers/docs/api/tree/Person_Memory_References_resource"""
        return self.person_base + pid + "/memory-references"

    def person_memory_reference(self, pid, erid):
        """https://familysearch.org/developers/docs/api/tree/Person_Memory_References_resource"""
        return self.person_base + pid + "/memory-references/" + erid

    def person_memories_portrait(self, pid, **kwargs):
        """https://familysearch.org/developers/docs/api/tree/Person_Memories_Portrait_resource"""
        return self._add_query_params(self.person_base + pid + "/portrait", kwargs)

    def person_portraits(self, pid):
        """https://familysearch.org/developers/docs/api/tree/Person_Portraits_resource"""
        return self.person_base + "/portrait"