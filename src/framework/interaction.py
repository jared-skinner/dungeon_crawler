from typing import Any

class Interaction:
    """ 
    This class is used for determining how a thing should act on another thing.
    The things can be items, people, or directions
    """
    def __init__(self, mover: Any, action: Any, description: str = "", visible: bool = False):
        self.mover = mover
        self.action = action
        self.description = description
        self.visible = visible
