# Python imports

# Magic

class Spouses:
    def __init__(self):
        pass # TODO
    
    def create_couple_relationship(self, mpid, fpid, change_message=None, date=None, place=None):
        url = self.tree_base + 'relationships'
        data = {
            "relationships" : [ {
            "type" : "http://gedcomx.org/Couple",
            "person1" : {
              "resource" : self.person_base + mpid,
              "resourceId" : mpid
            },
            "person2" : {
              "resource" : self.person_base + fpid,
              "resourceId" : fpid
            },
            "facts" : [ {
              "attribution" : {
                "contributor" : {
                  "resource" : self.user_base + "/agents/" + self.current_user()['treeUserId']
                },
                "changeMessage" : change_message
              },
              "type" : "http://gedcomx.org/Marriage",
              "date" : {
                "original" : date

              },
              "place" : {
                "original" : place
              }
            } ]
          } ]
        }
        response = self._request(url, data)
        return dict(response.info())
    
    def read_couple_relationship(self):
        pass # TODO
    
    def couple_relationship_conclusion(self):
        pass # TODO
    
    def couple_relationship_restore(self):
        pass # TODO

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Spouses,)