from typing import Any

class Interaction:
    """ 
    This class is used for determining how a thing should act on another thing.
    The things can be items, people, or directions
    """
    def __init__(
        self,
        patient: Any,
        name: str,
        action: Any,
        description: str = "",
        actor: Any = None,
        visible: bool = False
    ):
        self.name = name
        self.actor = actor
        self.patient = patient
        self.action = action
        self.description = description
        self.visible = visible
