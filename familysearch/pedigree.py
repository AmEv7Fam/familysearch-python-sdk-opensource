"""FamilySearch Pedigree submodule"""
# Python imports

# Magic

class Pedigree:
    """https://familysearch.org/developers/docs/api/examples#pedigree"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#pedigree"""
        pass

    def ancestry(self, pid, query="", **kwargs):
        """https://familysearch.org/developers/docs/api/tree/Ancestry_resource"""
        return self._add_query_params(
            self.tree_base + 'ancestry?person=' + pid, kwargs)

    def descendancy(self, pid, **kwargs):
        """https://familysearch.org/developers/docs/api/tree/Descendancy_resource"""
        return self._add_query_params(
            self.tree_base + 'descendancy?person=' + pid, kwargs)
