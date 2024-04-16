from framework.interaction import Interaction

class Item:
    def __init__(self, name: str, can_get: bool = False, description: str = "", get_description: str = "") -> None:
        self.name = name
        self.interactions = []
        self.can_get = can_get

        # the thing and what it does
        # for instance: with knife cut rope
        # so the rop item would validate that the knife can be used on it AND the knife can be used to cut the rope
        # when the kinfe is used to cut the rope it will result in a change to the properties of the rope

    def add_interaction(self, interaction: Interaction):
        self.interactions.append(interaction)
