# -*- coding: utf-8 -*-

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

        try:
            url = self.collections['FSDA']['response']['collections'][0][
                'links']['normalized-date']['template']
        except KeyError:
            self.update_collection("FSDA")
            url = self.collections['FSDA']['response']['collections'][0][
                'links']['normalized-date']['template']
        shim = {}
        shim["?date,access_token"] = ""
        return self._add_query_params(url.format(**shim), kwargs)
