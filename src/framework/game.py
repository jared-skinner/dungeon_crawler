import sys
from framework.room import Room 

class Game:
    def __init__(self):
        self.rooms = []
        self.start_room: Room

    def set_start_room(self, room: Room):
        self.start_room = room

    def start(self):
        self.main_loop(self.start_room)

    def main_loop(self, entrance):
        """
        This function is in charge of asking the player what they want to do next.  It uses a
        "while True" block to check what the player wanted to do last and then to prompt for the next
        action.
        """
        # these are the things a player can do
        # TODO: add "use x on y" to support interactions
        actions = ["go", "look", "options", "directions", "help", "exit"]

        current_room = entrance

        action = None
        while True:
            if action == None:
                self.message(current_room.description)
            elif action == "":
                # do nothing
                pass
            elif action == "look":
                if current_room.long_description == "":
                    self.message(current_room.description)
                else:
                    self.message(current_room.long_description)
            elif action in ("options", "help"):
                self.message("the options are:")
                for option in actions:
                    self.message(f"   * {option}")
            elif action == "exit":
                sys.exit()
            elif action == "directions":
                directions_message = "the directions are..."
                for direction in current_room.directions:
                    directions_message += f"\n    * {direction}"

                self.message(directions_message)
            elif action.startswith("go "):
                location = action[3:]
                if location not in current_room.directions:
                    self.message("you can't go there!")
                else:
                    current_room = current_room.directions[location].room
                    self.message(current_room.description)

                    if current_room.final:
                        sys.exit()
            else:
                self.message("THAT is not an option!")

            # get next action
            action = input("> ")


    def add_room(self, room):
        self.rooms.append(room)
        return room


    def link(self, room_1, room_2):
        """
        Link to rooms together.  This gives us an easy way to connect rooms in our maze
        """
        room_1.add_direction(room = room_2, locked = False)
        room_2.add_direction(room = room_1, locked = False)

    def message(self, text):
        """
        A nice way of displaying messages
        """
        print("")
        print(text)
        print("")


def save_gaem():
    pass


