# Python imports

# Magic

class User(object):
    def __init__(self):
        pass
        
    def get_current_user(self):
        return self.get(self.root_collection['collections'][0]['links']\
                        ['current-user']['href'])
    
    def get_current_user_person(self):
        url = self.tree_base + "current-person"
        response = self._request(url)
        response = self._fs2py(response, 'persons')
        return response[0]
    
    def get_agent(self, uid):
        url = self.user_base + "agents/" + uid
        response = self._request(url)
        response = self._fs2py(response, 'agents')
        return response[0]
    
    def get_user_history(self):
        url = self.user_base + "current/history"
        response = self._request(url)
        response = self._fs2py(response, 'sourceDescriptions')
        return response[0]

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (User,)
