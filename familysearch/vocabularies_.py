# pylint: disable=no-member, cyclic-import, import-error
# Python imports

# Magic

class Vocabularies:
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#vocabularies"""
        self.vocab_base = self.base + "platform/vocab/"

    def get_vocabulary_list(self, cvlid):
        """https://familysearch.org/developers/docs/api/cv/Controlled_Vocabulary_List_resource"""
        return self.get(self.vocab_base + "lists/" + cvlid)

    def get_vocabulary_term(self, cvtid):
        """https://familysearch.org/developers/docs/api/cv/Controlled_Vocabulary_Term_resource"""
        return self.get(self.vocab_base + "lists/" + cvtid)

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Vocabularies,)
