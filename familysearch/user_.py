# pylint: disable=no-member, cyclic-import, import-error
# Python imports

# Magic

class User(object):
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#user"""
        pass

    def get_current_user(self):
        """https://familysearch.org/developers/docs/api/users/Current_User_resource"""
        return self.get(self.root_collection['collections'][0]['links']
                        ['current-user']['href'])

    def get_current_user_person(self):
        """https://familysearch.org/developers/docs/api/tree/Current_Tree_Person_resource"""
        return self.get(self.family_tree['collections'][0]['links']
                        ['current-user-person']['href'])

    def get_agent(self, uid):
        """https://familysearch.org/developers/docs/api/users/Agent_resource"""
        return self.get(self.user_base + "agents/" + uid)

    def get_current_user_history(self):
        """https://familysearch.org/developers/docs/api/users/Current_User_History_resource """
        return self.get(self.family_tree['collections'][0]['links']
                        ['current-user-history']['href'])

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (User,)
