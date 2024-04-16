from framework.game import Game
from framework.room import Room
from framework.item import Item
from framework.interaction import Interaction

class Quest():
    """
    This is a little example to give you an idea of how all the pieces are suppose to go together.
    """
    def __init__(self):
        # Create a new instance of the Game class
        self.game = Game()
        self.initialize_game()

    def initialize_game(self):
        game = self.game

        # create all the rooms
        entrance = game.add_room(Room(
            name = "entrance",
            description = "Welcome weary traveler to the cave of DOOM!!!",
            long_description = """
    There's moss growing on the walls and crumbly stones everywhere.

    You notice some rope and a knife on the ground.  They both look pretty new.  

    The ground feels pretty solid, but it looks like you are the first to come here in a very long time.  Step carefully...
            """
        ))

        rope = Item(name = "rope", can_get = True)
        knife = Item(name = "knife", can_get = True)
        def cut_rope(rope): rope.name = "rope cut in two (you really ought to be more careful what you do with that knife...)"

        cut = Interaction(
            name = "cut",
            actor = knife,
            patient = rope,
            action = cut_rope,
            description = "The knife cuts the rope cleanly in two.  Now you have a knife an some useless rope?"
        )
        game.add_interaction(cut)

        entrance.add_item(knife)
        entrance.add_item(rope)

        large_cavern = game.add_room(Room(
            name = "large cavern",
            description = "You find yourself in a large cavern",
            long_description = """
    This room is so big there isn't even a echo.  It looks like it was man-made, but man... who made 
    this place.  You notice that the floor is made of marbel tiles.  There are no columns in sight.
    What's holding this place up!?
            """
        ))

        small_cavern = game.add_room(Room(
            name = "small cavern",
            description = "You find yourself in a small cavern",
            long_description = """
    Is this a cavern for ants?!  It needs to be at least... three times bigger.  Seriously though, this 
    place is tiny!  Oddly it still feels cavernous.
            """
        ))

        windy_passage = game.add_room(Room(
            name = "windy passage",
            description = "This looks to be the start of a windy passage",
            long_description = """
    The walls are made of some smooth stone that you are not familiar with.  The passage goes on for a
    long ways, twisting and turning.  Oddly this is the only passage which doesn't seem to be touched
    by time.
            """
        ))

        long_tunnel = game.add_room(Room(
            name = "long tunnel",
            description = "The entrance narrows to a tunnel that seems to stretch on forever",
            long_description = """
    This tunnel descents deep into the earth.  The walls are cut rough of a green, blue stone.
            """
        ))

        gift_shop = game.add_room(Room(
            name = "gift shop",
            description = "A gift shop in the cave of doom?!  Who woulda figured",
            long_description = """
    It seems like everything in here is a nike product...

    nike shoes, nike rope, nike bags of sand.  They tought of everything.  

    The beach supplies are on discount!  Time to pick up a spare towel!
            """
        ))

        treasure_room = game.add_room(Room(
            name = "treasure room",
            description = "You did it, you found the treasure room!  Congratulations, the quest was a success",
            long_description = """

            """, 
            final = True
        ))

        # link the rooms together
        game.link(entrance, large_cavern)
        game.link(entrance, long_tunnel)

        game.link(long_tunnel, gift_shop)
        game.link(gift_shop, small_cavern)
        game.link(gift_shop, windy_passage)

        game.link(small_cavern, large_cavern)
        game.link(windy_passage, treasure_room)
        game.set_current_room(entrance)


        game.set_splashscreen(
r""" 
                                             __----~~~~~~~~~~~------___
                                  .  .   ~~//====......          __--~ ~~
                  -.            \_|//     |||\\  ~~~~~~::::... /~
               ___-==_       _-~o~  \/    |||  \\            _/~~-
       __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
   _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
 .~       .~       |   \\ -_    /  /-   /   ||      \   /
/  ____  /         |     \\ ~-_/  /|- _/   .||       \ /
|~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\
         '         ~-|      /|    |-~\~~       __--~~
                     |-~~-_/ |    |   ~\_   _-~            /\
                          /  \     \__   \/~                \__
                      _--~ _/ | .-~~____--~-/                  ~~==.
                     ((->/~   '.|||' -_|    ~~-/ ,              . _||
                                -_     ~\      ~~---l__i__i__i--~~_/
                                _-~-__   ~)  \--______________--~~
                              //.-~~~-~_--~- |-------~~~~~~~~
                                     //.-~~~--\


                QUEST 
                    - A Game by Jared Skinner


"""
        )




    def start(self):
        # run the dungeon!
        self.game.start()
