import sys

from framework.room import Room 
from framework.util import save_game

class Game:
    def __init__(self) -> None:
        self.rooms = []
        self.current_room: Room
        self.splashscreen: str = ""

    def set_current_room(self, room: Room) -> None:
        self.current_room = room

    def start(self) -> None:
        self.main_loop()

    def set_splashscreen(self, splashscreen):
        self.splashscreen = splashscreen

    def main_loop(self) -> None:
        """
        This function is in charge of asking the player what they want to do next.  It uses a
        "while True" block to check what the player wanted to do last and then to prompt for the next
        action.
        """
        # these are the things a player can do
        # TODO: add "use x on y" to support interactions
        actions = ["go", "look", "options", "directions", "help", "exit", "save"]

        action = None

        print(self.splashscreen)

        while True:
            if action == None:
                self.message(self.current_room.description)
            elif action == "":
                # do nothing
                pass
            elif action == "look":
                if self.current_room.long_description == "":
                    self.message(self.current_room.description)
                else:
                    self.message(self.current_room.long_description)
            elif action in ("options", "help"):
                self.message("the options are:")
                for option in actions:
                    self.message(f"   * {option}")
            elif action == "exit":
                sys.exit()
            elif action == "directions":
                directions_message = "the directions are..."
                for direction in self.current_room.directions:
                    directions_message += f"\n    * {direction}"

                self.message(directions_message)
            elif action.startswith("go "):
                location = action[3:]
                if location not in self.current_room.directions:
                    self.message("you can't go there!")
                else:
                    self.current_room = self.current_room.directions[location].room
                    self.message(self.current_room.description)

                    if self.current_room.final:
                        sys.exit()
            elif action.startswith("save "):
                save_name = action[5:]
                save_game(self, save_name)
            else:
                self.message("THAT is not an option!")

            # get next action
            action = input("> ")


    def add_room(self, room: Room) -> Room:
        self.rooms.append(room)
        return room


    def link(self, room_1: Room, room_2: Room) -> None:
        """
        Link to rooms together.  This gives us an easy way to connect rooms in our maze
        """
        room_1.add_direction(room = room_2, locked = False)
        room_2.add_direction(room = room_1, locked = False)

    def message(self, text: str) -> None:
        """
        A nice way of displaying messages
        """
        print("")
        print(text)
        print("")
