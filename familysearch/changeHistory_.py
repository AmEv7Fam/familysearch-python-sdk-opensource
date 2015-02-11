"""FamilySearch Change History submodule"""
# Python imports

# Magic

class ChangeHistory:
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#change-history"""
        from . import FamilySearch
        FamilySearch.__bases__ += (ChangeHistory,)

    def get_person_change_history(self, pid):
        """Obsolete."""
        return self.get(self.tree_base + "persons/" + pid + "/changes")

    def get_child_change_history(self, caprid):
        """Obsolete."""
        return self.get(self.tree_base + "child-and-parents-relationships/"\
              + caprid + "/changes")

    def get_read_couple_change_history(self, crid):
        """Obsolete."""
        return self.get(self.tree_base + "couple-relationships/" + crid + "/changes")

    def restore_change(self, chid):
        """Obsolete."""
        return self.post(self.tree_base + "changes/" + chid + "/restore")

# FamilySearch imports

