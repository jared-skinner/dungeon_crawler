from typing import Any

class Item:
    def __init__(self, name):
        self.name = name
        self.interactions = {}

    def act(self, other_thing: Any):
        # check if we can act on this thing
        pass

