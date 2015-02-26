"""FamilySearch Utilities submodule"""
# Python imports

# Magic

class Utilities:
    """https://familysearch.org/developers/docs/api/resources#utilities"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#utilities"""
        pass

    def pending_modifications(self):
        """https://familysearch.org/developers/docs/api/tree/Pending_Modifications_resource"""
        return self.get(self.root_collection['response']['collections'][0]['links']\
                        ['pending-modifications']['href'])

    def redirect(self, **kwargs):
        """https://familysearch.org/developers/docs/api/tree/Redirect_resource"""
        return self._add_query_params(
            self.base + "platform/redirect", kwargs)
          
    def oembed(self, **kwargs):
        """https://familysearch.org/developers/docs/api/discovery/OEmbed_resource"""
        return self._add_query_params(
            self.base + "platform/oembed", kwargs)

from familysearch import FamilySearch
FamilySearch.__bases__ += (Utilities,)