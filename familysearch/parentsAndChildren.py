# Python imports

# Magic

class ParentsAndChildren:
    def __init__(self):
        pass

    def create_child_relationship(self, cpid, fpid='', mpid='', ftype='',
                                  mtype='', reason=None):
        url = self.tree_base + 'relationships'
        data = {
            "childAndParentsRelationships" : [ {
            "father" : {
                "resource" : "https://familysearch.org/platform/tree/persons/" + mpid,
                "resourceId" : mpid
            },
            "mother" : {
                "resource" : "https://familysearch.org/platform/tree/persons/" + fpid,
                "resourceId" : fpid
            },
              "child" : {
                "resource" : self.person_base + cpid,
                "resourceId" : cpid
            },
            "fatherFacts" : [ {
                "id" : fpid,
                "attribution" : {
                    "contributor" : {
                        "resource" : self.user_base + "/agents/" + self.current_user()['treeUserId']
                    },
                    "changeMessage" : reason
                },
                "type" : "http://gedcomx.org/" + ftype + "Parent"
            } ],
            "motherFacts" : [ {
                "id" : mpid,
                "attribution" : {
                    "contributor" : {
                        "resource" : self.user_base + "/agents/" + self.current_user()['treeUserId']
                    },
                    "changeMessage" : reason
                },
                "type" : "http://gedcomx.org/ "+ mtype + "Parent"
              } ]
            } ]
            }
        if not(mpid and fpid):
            raise ValueError("Provide at least one parent to create a child-parent relationship.")
        if not fpid:
            del data['childAndParentsRelationships'][0]["father"]
        if not ftype:
            del data['childAndParentsRelationships'][0]['fatherFacts']
        if not mpid:
            del data['childAndParentsRelationships'][0]["mother"]
        if not mtype:
            del data['childAndParentsRelationships'][0]['motherFacts']
        response = self._request(url, data)
        return dict(response.info())
    
    def cap_relationship_parent(self):
        pass # TODO
    
    def cap_relationship_conclusion(self):
        pass # TODO
    
    def child_relationship_restore(self):
        pass # TODO

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (ParentsAndChildren,)