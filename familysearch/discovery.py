
# Python imports

# Magic

class Discovery(object):
    def collection(self):
        url = self.base + '/.well-known/collection'
        response = self._request(url)
        return self._fs2py(response)

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Discovery,)
