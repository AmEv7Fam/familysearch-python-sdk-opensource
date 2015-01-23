"""FamilySearch Places submodule"""
# Python imports

# Magic

class Places:
    def __init__(self):
        """"""
        self.places_base = self.base + "/platform/places/"

    def get_places_search(self, q):
        """"""
        return self.get(self.places_base + "search?q=name:" + q)

    def get_place_description(self, pdid, children=None):
        """"""
        url = self.places_base + "description/" + pdid
        if children:
            url = url + "/children"
        return self.get(url)

    def get_place_group(self, pgid):
        """"""
        return self.get(self.places_base + "gropus/" + pgid)

    def get_place(self, pid):
        """"""
        return self.get(self.places_base + str(pid))

    def get_place_type(self, ptid):
        """"""
        return self.get(self.places_base + "types/" + ptid)

    def get_place_type_group(self, ptgid):
        """"""
        return self.get(self.places_base + "type-gropus/" + ptgid)

    def get_place_types(self):
        """"""
        return self.get(self.places_base + "types")

    def get_place_type_groups(self):
        """"""
        return self.get(self.places_base + "type-groups")

# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Places,)
