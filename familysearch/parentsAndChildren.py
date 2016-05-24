# -*- coding: utf-8 -*-

"""FamilySearch Parents and Children submodule"""

# Python imports

# Magic


class ParentsAndChildren:
    """https://familysearch.org/developers/docs/api/resources#parents-and-children"""

    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#parents-and-children"""

        self.child_base = self.tree_base + "child-and-parents-relationships/"

    def child_relationship(self, crid):
        """https://familysearch.org/developers/docs/api/tree/Child-and-Parents_Relationship_resource"""

        return self.child_base + crid

    def child_relationship_parent(self, crid, role):
        """https://familysearch.org/developers/docs/api/tree/Child-and-Parents_Relationship_Parent_resource"""

        return self.child_base + crid + "/" + role

    def child_relationship_conclusion(self, crid, role, cid):
        """https://familysearch.org/developers/docs/api/tree/Child-and-Parents_Relationship_Conclusion_resource"""

        return self.delete(
            self.child_base + crid + "/" + role + "/conclusions/" + cid)

    def child_relationship_notes(self, crid):
        """https://familysearch.org/developers/docs/api/tree/Child-and-Parents_Relationship_Notes_resource"""


        return self.child_base + crid + "/notes"

    def child_relationship_note(self, crid, nid):
        """https://familysearch.org/developers/docs/api/tree/Child-and-Parents_Relationship_Note_resource"""

        return self.child_base + crid + "/notes/" + nid

    def child_relationship_restore(self, crid):
        """https://familysearch.org/developers/docs/api/tree/Child-and-Parents_Relationship_Restore_resource"""

        return self.child_base + crid + "/restore"
