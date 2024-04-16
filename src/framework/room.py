class Room:
    """
    The Room class gives us a template for creating rooms.  Each room has a name, a description,
    and an optional long_description.  Directions are added using the link function above.

    The main loop is in charge of using this information to run the dungeon
    """
    def __init__(self, name: str, description: str, long_description: str = "", final: bool = False):
        self.name = name
        self.description = description
        self.long_description = long_description
        self.directions = {}
        self.final = final

    def add_direction(self, room, locked: bool, locked_description: str = "") -> None:
        self.directions[room.name] = Direction(room, locked, locked_description)

class Direction:
    def __init__(self, room: Room, locked: bool, locked_description: str = ""):
        self.room = room 
        self.locked = locked 
        self.locked_description = locked_description


