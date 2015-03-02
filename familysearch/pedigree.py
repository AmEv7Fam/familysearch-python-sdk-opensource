"""FamilySearch Pedigree submodule"""
# Python imports

# Magic

class Pedigree:
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#pedigree"""
        pass

    def ancestry(self, pid, query="", **kwargs):
        """Obsolete."""
        return self._add_query_params(
            self.tree_base + 'ancestry?person=' + pid, kwargs)

    def descendancy(self, pid, **kwargs):
        """Obsolete."""
        return self._add_query_params(
            self.tree_base + 'descendancy?person=' + pid, kwargs)