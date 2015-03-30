"""FamilySearch Authorities submodule"""
# Python imports
 
# Magic

class Authorities():
    """https://familysearch.org/developers/docs/api/resources#authorities"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#authorities."""
        pass

    def dates(self, **kwargs):
        """https://familysearch.org/developers/docs/api/dates/Date_resource."""
        return self._add_query_params(
            self.base + '/platform/dates', kwargs)