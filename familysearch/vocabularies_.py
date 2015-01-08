# pylint: disable=no-member, cyclic-import, import-error
# Python imports

# Magic

class Vocabularies:
    def __init__(self):
        """"""
        self.vocab_base = self.base + "platform/vocab/"

    def get_vocabulary_list(self, cvlid):
        """"""
        return self.get(self.vocab_base + "lists/" + cvlid)

    def get_vocabulary_term(self, cvtid):
        """"""
        return self.get(self.vocab_base + "lists/" + cvtid)

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Vocabularies,)
