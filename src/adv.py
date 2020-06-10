from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Backyard", """A barbeque grill sits in the center of a well groomed 
    yard. Just North of you lies the lit up skyline, the electirc city fun beckons"""),

    'kitchen':    Room("Kitchen", """Under a dim light a plate stacked with delicious donuts
    catches your sight. Have a treat but not too many! An overhead surround sound plays Dilla
    which gets louder heading north and east toward a windy breeze."""),

    'balcony': Room("Grand Overlook", """A highrise view of the amazing skyline appears before you. 
    Have a seat to take it all in. Ahead to the north, a smell of delicious mexican cuisine 
    permiates the air and the fire stove oven wafts a smoke signal in the distance."""),

    'tacos':   Room("Taco Hut", """The smell of delicious mexican cuisine at it's finest!
    After your energy is filled, head west to north and follow the sounds in the distance."""),

    'party': Room("Wolf Pack Party", """You've found Dj Kwest-on's amazing 
    Dance Party where all your friends are dancing! To get to the after party you have
    to dance it up! Use a combination of all directions to really groove. 
    Hint: South is really gettin down """),
}


# Link rooms together

room['outside'].n_to = room['kitchen']
room['kitchen'].s_to = room['outside']
room['kitchen'].n_to = room['balcony']
room['kitchen'].e_to = room['tacos']
room['balcony'].s_to = room['kitchen']
room['tacos'].w_to = room['kitchen']
room['tacos'].n_to = room['party']
room['party'].s_to = room['tacos']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#user = int(input("[n] North  [s] South  [e] East  [w] West  [9] Quit"))
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
