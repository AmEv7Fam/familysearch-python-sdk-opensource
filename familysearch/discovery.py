
# Python imports



from . import FamilySearch

# Magic

class Discovery(object):
    def __init__(self):
        self.root_collection = self._get(self.base + '/.well-known/collection')


# FamilySearch hookup

FamilySearch.__bases__ += (Discovery,)
