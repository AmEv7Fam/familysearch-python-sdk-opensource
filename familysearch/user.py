# Python imports

# Magic

class User(object):
    def __init__(self):
        pass
        
    def current_user(self):
        url = self.user_base + "current"
        response = self._request(url)
        response = self._fs2py(response, 'users')
        return response[0]
    
    def current_user_person(self):
        url = self.tree_base + "current-person"
        response = self._request(url)
        response = self._fs2py(response, 'persons')
        return response[0]
    
    def agents(self, uid):
        url = self.user_base + "agents/" + uid
        response = self._request(url)
        response = self._fs2py(response, 'agents')
        return response[0]
    
    def current_user_history(self):
        url = self.user_base + "current/history"
        response = self._request(url)
        response = self._fs2py(response)
        return response

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (User,)