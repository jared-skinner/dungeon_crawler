from framework.item import Item

class Action:
    def __init__(self, name, descriptions, action):
        self.name = name
        self.descriptions = descriptions
        self.action = action
        self.call_count = 0

    def describe(self):
        if self.call_count >= len(self.descriptions) - 1:
            print(self.descriptions[-1])
        else:
            print(self.descriptions[self.call_count])

    def increment_call_count(self):
        self.call_count += 1

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
        self.items = {}
        self.commands = {}

    def add_direction(self, room, locked: bool, locked_description: str = "") -> None:
        self.directions[room.name] = Direction(room, locked, locked_description)

    def add_item(self, item: Item) -> None:
        self.items[item.name] = item

    def remove_item(self, item: Item) -> None:
        del self.items[item.name]

    def room_command(self, command: str) -> None:
        if command not in self.commands:
            # TODO: error message
            return

        self.commands[command].describe()

        if self.commands[command].action:
            self.commands[command].action(self)

        self.commands[command].increment_call_count()

    def register_command(self, name, descriptions, command = None) -> None:
        self.commands[name] = Action(name, descriptions, command)

class Direction:
    def __init__(self, room: Room, locked: bool, locked_description: str = ""):
        self.room = room 
        self.locked = locked 
        self.locked_description = locked_description
