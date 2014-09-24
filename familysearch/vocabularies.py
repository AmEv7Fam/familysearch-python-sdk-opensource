# Python imports

# Magic

class Vocabularies:
    def __init__(self):
        self.vocab_base = self.base + "platform/vocab/"
    
    def vocabulary_list(self, cvlid):
        url = self.vocab_base + "lists/" + cvlid
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def vocabulary_term(self, cvtid):
        url = self.vocab_base + "lists/" + cvtid
        response = self._request(url)
        response = self._fs2py(response)
        return response

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Vocabularies,)