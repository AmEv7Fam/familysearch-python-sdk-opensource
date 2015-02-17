"""FamilySearch User submodule"""
# Python imports



# Magic

class User(object):
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#user"""

    def current_user(self):
        """https://familysearch.org/developers/docs/api/users/Current_User_resource"""
        return self.root_collection['response']['collections'][0]['links']\
        ['current-user']['href']
        
    def current_user_person(self):
        """https://familysearch.org/developers/docs/api/tree/Current_Tree_Person_resource"""
        return self.tree_base + "/current_person"

    def agent(self, uid):
        """https://familysearch.org/developers/docs/api/users/Agent_resource"""
        return self.user_base + "agents/" + uid

    def current_user_history(self):
        """https://familysearch.org/developers/docs/api/users/Current_User_History_resource."""
        return self.user_base + "current/history"

from familysearch import FamilySearch
FamilySearch.__bases__ += (User,)