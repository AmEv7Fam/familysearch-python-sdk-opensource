"""FamilySearch Spouses submodule"""
# Python imports

from . import FamilySearch

# Magic

class Spouses:
    """https://familysearch.org/developers/docs/api/resources#spouses"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#spouses"""
        self.couple_base = self.tree_base + 'couple-relationships/'
   
    def relationship(self):
        """https://familysearch.org/developers/docs/api/tree/Relationships_resource"""
        return self.tree_base + "relationships"

    def couple_relationship(self, cpid):
        """https://familysearch.org/developers/docs/api/tree/Couple_Relationship_resource"""
        return self.couple_base + cpid

    def couple_relationship_conclusion(self, cpid, cid):
        """https://familysearch.org/developers/docs/api/tree/Couple_Relationship_Conclusion_resource"""
        return self.couple_base + cpid + '/conclusions/' + cid

    def couple_relationship_restore(self, cpid):
        """https://familysearch.org/developers/docs/api/tree/Couple_Relationship_Restore_resource"""
        return self.couple_base + cpid + '/restore'

# FamilySearch hookup

FamilySearch.__bases__ += (Spouses,)
