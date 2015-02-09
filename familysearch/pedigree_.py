"""FamilySearch Pedigree submodule"""
# Python imports

# Magic

class Pedigree:
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#pedigree"""
        pass

    def get_ancestry(self, pid, query="", **kwargs):
        """Obsolete."""
        return self.get(self._add_query_params(
            self.tree_base + 'ancestry?person=' + pid, query, **kwargs))

    def get_descendancy(self, pid, query="", **kwargs):
        """Obsolete."""
        return self.get(self._add_query_params(
            self.tree_base + 'descendancy?person=' + pid, query, **kwargs))

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Pedigree,)