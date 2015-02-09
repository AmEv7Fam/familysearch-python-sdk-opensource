"""FamilySearch User submodule"""
# Python imports

# Magic

class User(object):
    def __init__(self):
        """Obsolete."""
        pass

    def get_current_user(self):
        """Obsolete."""
        return self.get(self.root_collection['collections'][0]['links']
                        ['current-user']['href'])

    def get_current_user_person(self):
        """Obsolete."""
        return self.get(self.family_tree['collections'][0]['links']
                        ['current-user-person']['href'])

    def get_agent(self, uid):
        """Obsolete."""
        return self.get(self.user_base + "agents/" + uid)

    def get_current_user_history(self):
        """Obsolete."""
        return self.get(self.family_tree['collections'][0]['links']
                        ['current-user-history']['href'])

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (User,)
