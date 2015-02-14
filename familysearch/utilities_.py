"""FamilySearch Utilities submodule"""
# Python imports

# Magic

class Utilities:
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#utilities"""
        from familysearch import FamilySearch
        FamilySearch.__bases__ += (Utilities,)

    def get_pending_modifications(self):
        """Obsolete."""
        return self.get(self.root_collection['collections'][0]['links']\
                        ['pending-modifications']['href'])

    def redirect(self, params, **kwargs):
        """Obsolete."""
        params = self._add_query_params({access_token: session_id}, **params)
        return self._add_query_params(
          self.base + "platform/redirect", params, **kwargs)