from framework.game import Game
from framework.room import Room
from framework.item import Item
from framework.interaction import Interaction

"""
This is a little example to give you an idea of how all the pieces are suppose to go together.

    Story idea: Lowly pesant who discovers that the princess that was kidnapped by a dragon IS a dragon and must be saved


    And the might hero swings his sword slaying the Dragon!




"""
game = Game()

game.set_splashscreen(
    r""" 

#######################################################################



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


#######################################################################

""")

game.set_introduction(
"""
...........
...........
...........
...........

Ugh... How late did you stay out last night.  The sun is shining painfully bright in your eyes.
"""
)


# ENTRANCE
entrance = game.add_room(Room(
    name = "bedroom",
    description = "",
    long_description = """There's moss growing on the walls and crumbly stones everywhere.  When was the last time this room was cleaned up!? It's so bright in here that you have to squint to see anything.  I wonder what the room would look like with a little shade..."""
))

## Items
entrance.add_item(Item(name = "rope", can_get = True))
entrance.add_item(Item(name = "knife", can_get = True))
entrance.add_item(Item(name = "flute", can_get = True))
entrance.add_item(Item(name = "anvil", can_get = True))

## Commands
def draw_shades(room): room.long_description = """Your sheets look terrible.  You should probably burn them"""
entrance.register_command(name="draw shades", command=draw_shades, descriptions=["As you draw the shades you realize you are using old newspaper.  You should probably invest in your decore"])

entrance.register_command(name="make bed", descriptions=["Your bed looks slightly less horrible", "Yeah, that's worse", "Why don't you give up already?"])

entrance.register_command(name="dance", descriptions=["That was a mistake, but it appears that some of the carpet pulled up.  What's that shiny thing", "Your body refuses"])

























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
    long_description = """Is this a cavern for ants?!  It needs to be at least... three times bigger.  Seriously though, this place is tiny!  Oddly it still feels cavernous."""
))

windy_passage = game.add_room(Room(
    name = "windy passage",
    description = "This looks to be the start of a windy passage",
    long_description = """The walls are made of some smooth stone that you are not familiar with.  The passage goes on for a long ways, twisting and turning.  Oddly this is the only passage which doesn't seem to be touched by time."""
))

long_tunnel = game.add_room(Room(
    name = "long tunnel",
    description = "The entrance narrows to a tunnel that seems to stretch on forever",
    long_description = """This tunnel descents deep into the earth.  The walls are cut rough of a green, blue stone."""
))

gift_shop = game.add_room(Room(
    name = "gift shop",
    description = "A gift shop in the cave of doom?!  Who woulda figured",
    long_description = """It seems like everything in here is a nike product...\n\n nike shoes, nike rope, nike bags of sand.  They tought of everything.  \n\n The beach supplies are on discount!  Time to pick up a spare towel!"""
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




game.start()
