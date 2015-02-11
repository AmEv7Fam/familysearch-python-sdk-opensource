"""FamilySearch Vocabularies submodule"""
# Python imports

# Magic

class Vocabularies:
    """"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#vocabularies"""
        self.vocab_base = self.base + "platform/vocab/"
        from familysearch import FamilySearch
        FamilySearch.__bases__ += (Vocabularies,)

    def get_vocabulary_list(self, cvlid):
        """Obsolete."""
        return self.get(self.vocab_base + "lists/" + cvlid)

    def get_vocabulary_term(self, cvtid):
        """Obsolete."""
        return self.get(self.vocab_base + "lists/" + cvtid)