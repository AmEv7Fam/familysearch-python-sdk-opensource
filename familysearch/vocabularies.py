"""FamilySearch Vocabularies submodule"""
# Python imports

# Magic

class Vocabularies:
    """https://familysearch.org/developers/docs/api/resources#vocabularies"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#vocabularies"""
        self.vocab_base = self.base + "platform/vocab/"

    def vocabulary_list(self, cvlid):
        """https://familysearch.org/developers/docs/api/cv/Controlled_Vocabulary_List_resource"""
        try:
            url = self.collections["FSCV"]["response"]['collections'][
                0]['links']['vocab-list']['template']
        except KeyError:
            self.update_collection("FSCV")
            url = self.collections["FSCV"]["response"]['collections'][
                0]['links']['vocab-list']['template']
        shim = {}
        shim["?access_token"] = ""
        shim["cvlid"] = cvlid
        return url.format(**shim)
    
    def vocabulary_lists(self):
        """https://familysearch.org/developers/docs/api/cv/Controlled_Vocabulary_List_resource"""
        try:
            url = self.collections["FSCV"]["response"]['collections'][
                0]['links']['vocab-lists']['href']
        except KeyError:
            self.update_collection("FSCV")
            url = self.collections["FSCV"]["response"]['collections'][
                0]['links']['vocab-lists']['href']
        return url

    def vocabulary_term(self, cvtid):
        """https://familysearch.org/developers/docs/api/cv/Controlled_Vocabulary_Term_resource"""
        #return self.vocab_base + "lists/" + cvtid
        """https://familysearch.org/developers/docs/api/cv/Controlled_Vocabulary_List_resource"""
        try:
            url = self.collections["FSCV"]["response"]['collections'][
                0]['links']['vocab-term']['template']
        except KeyError:
            self.update_collection("FSCV")
            url = self.collections["FSCV"]["response"]['collections'][
                0]['links']['vocab-term']['template']
        shim = {}
        shim["?access_token"] = ""
        shim["cvtid"] = cvtid
        return url.format(**shim)
