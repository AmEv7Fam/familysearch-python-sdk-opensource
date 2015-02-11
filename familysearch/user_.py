"""FamilySearch User submodule"""
# Python imports

from . import FamilySearch

# Magic

class User(object):
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#user"""
        pass

    def current_user(self):
        """https://familysearch.org/developers/docs/api/users/Current_User_resource"""
        return self.root_collection['collections'][0]['links']\
        ['current-user']['href']
        
    def current_user_person(self):
        """https://familysearch.org/developers/docs/api/tree/Current_Tree_Person_resource"""
        return self.family_tree['collections'][0]['links']\
        ['current-user-person']['href']

    def agent(self, uid):
        """https://familysearch.org/developers/docs/api/users/Agent_resource"""
        return self.user_base + "agents/" + uid

    def current_user_history(self):
        """https://familysearch.org/developers/docs/api/users/Current_User_History_resource."""
        return self.family_tree['collections'][0]['links']\
        ['current-user-history']['href']

# FamilySearch hookup

FamilySearch.__bases__ += (User,)
