"""FamilySearch User submodule"""
# Python imports



# Magic

class User(object):
    """https://familysearch.org/developers/docs/api/resources#user"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#user"""
        pass

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
        """https://familysearch.org/developers/docs/api/users/Current_User_History_resource"""
        return self.user_base + "current/history"