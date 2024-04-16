import sys
from typing import Any

from framework.person import Person
from framework.room import Room 
from framework.util import save_game
from framework.interaction import Interaction

class Game:
    def __init__(self) -> None:
        self.rooms = []
        self.current_room: Room

        # TODO: let player enter their name
        self.player: Person = Person("test")
        self.splashscreen: str = ""
        self.interactions: list[Interaction] = []

    def get_thing(self, thing) -> Any:
        for item_name in self.current_room.items:
            if item_name == thing:
                return self.current_room.items[item_name]

        for item in self.player.inventory.items:
            if item.name == thing:
                return item

        self.message(f"{thing} is not available.  Are you sure you can use it?")
        return None

    def print_inventory(self) -> None:
        for item in self.player.inventory.items:
            print(item.name)

    def get(self, thing) -> None:
        item = None
        for item_name in self.current_room.items:
            if item_name == thing:
                 item = self.current_room.items[item_name]

        if item == None:
            self.message(f"{thing} could not be found.  Are you sure you spelled it right?")
            return

        if item.can_get == False:
            self.message(f"Unfourtinately you can't get {thing}")
            return

        self.player.inventory.add_item(item)

        # TODO
        #self.current_room.remove_item(item)


    def combine(self, command: str) -> None:
        """
        Using one thing act on another thing
        """
        # tokenize the input
        action_parts = command.split()

        # TODO, better message
        assert len(action_parts) == 4, self.message("Incomplete command!")

        actor_str = action_parts[1]
        action_str = action_parts[2]
        object_str = action_parts[3]

        actor = self.get_thing(actor_str)
        patient = self.get_thing(object_str)

        if actor == None or patient == None:
            return

        # look for an action
        needed_interaction = None
        for interaction in self.interactions:
            if interaction.actor == actor and interaction.patient == patient and interaction.name == action_str:
                needed_interaction = interaction

        if needed_interaction == None:
            # TODO: thrown an error!
            self.message(f"Unfourtinately you cannot {action_str} the {patient} with the {actor}")
            return

        needed_interaction.action(patient)
        self.message(needed_interaction.description)

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

    def add_interaction(self, interaction: Interaction) -> None:
        self.interactions.append(interaction)

    def set_current_room(self, room: Room) -> None:
        self.current_room = room

    def set_splashscreen(self, splashscreen):
        self.splashscreen = splashscreen

    def main_loop(self):
        actions = ["go", "look", "options", "directions", "help", "exit", "save", "with", "inventory"]

        action = None
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
                    print(f"   * {option}")
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
            elif action.startswith("with "):
                self.combine(action)
            elif action == "inventory":
                self.print_inventory()
            elif action.startswith("get "):
                self.get(action[4:])
            else:
                self.message("THAT is not an option!")

            # get next action
            action = input("> ")

    def start(self) -> None:
        """
        This function is in charge of asking the player what they want to do next.  It uses a
        "while True" block to check what the player wanted to do last and then to prompt for the next
        action.
        """
        print(self.splashscreen)
        self.main_loop()
