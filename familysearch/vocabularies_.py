"""FamilySearch Vocabularies submodule"""
# Python imports

# Magic

class Vocabularies:
    """https://familysearch.org/developers/docs/api/resources#vocabularies"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#vocabularies"""
        self.vocab_base = self.base + "platform/vocab/"
        from familysearch import FamilySearch
        FamilySearch.__bases__ += (Vocabularies,)

    def vocabulary_list(self, cvlid):
        """https://familysearch.org/developers/docs/api/cv/Controlled_Vocabulary_List_resource"""
        return self.vocab_base + "lists/" + cvlid

    def vocabulary_term(self, cvtid):
        """https://familysearch.org/developers/docs/api/cv/Controlled_Vocabulary_Term_resource"""
        return self.vocab_base + "lists/" + cvtid