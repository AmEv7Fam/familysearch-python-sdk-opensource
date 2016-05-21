# -*- coding: utf-8 -*-

"""FamilySearch Spouses submodule"""

# Python imports

# Magic


class Spouses:
    """https://familysearch.org/developers/docs/api/resources#spouses"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#spouses"""
        self.couple_base = self.tree_base + 'couple-relationships/'

    def relationship(self):
        """https://familysearch.org/developers/docs/api/tree/Relationships_resource"""
        return self.tree_base + "relationships"

    def couple_relationship(self, cpid, **kwargs):
        """https://familysearch.org/developers/docs/api/tree/Couple_Relationship_resource"""
        return self._add_query_params(self.couple_base + cpid, kwargs)

    def couple_relationship_conclusion(self, cpid, cid):
        """https://familysearch.org/developers/docs/api/tree/Couple_Relationship_Conclusion_resource"""
        return self.couple_base + cpid + '/conclusions/' + cid

    def couple_relationship_notes(self, crid):
        """https://familysearch.org/developers/docs/api/tree/Couple_Relationship_Notes_resource"""
        return self.couple_base + crid + "/notes"

    def couple_relationship_note(self, crid):
        """https://familysearch.org/developers/docs/api/tree/Couple_Relationship_Note_resource"""
        return self.couple_base + crid + "/notes/" + nid

    def couple_relationship_restore(self, cpid):
        """https://familysearch.org/developers/docs/api/tree/Couple_Relationship_Restore_resource"""
        return self.couple_base + cpid + '/restore'
