# Python imports

# Magic

class Spouses:
    def __init__(self):
        self.couple_base = self.tree_base + 'couple-relationships/'
    
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
    
    def delete_couple_relationship(self, cpid, reason=None):
        url = self.couple_base + cpid
        response = self._request(url, headers={'X-Reason': reason}, method="DELETE")
        return dict(response.info())
    
    def restore_couple_relationship(self, cpid):
        url = self.couple_base + cpid + '/restore'
        response = self._request(url, method="POST", nojson=True)
        return dict(response.info()) 
# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Spouses,)