from room import Room

# Declare all the rooms

room = {
    'outside': Room("Outside Backyard", """A barbeque grill sits in the center of a well groomed 
    yard. Pre-party time! Flip some burgers to feed some friends. Just South of you lies the lit up skyline. 
    For a better view, head inside the house."""),

    'kitchen': Room("Kitchen", """Under a dim light a plate stacked with delicious donuts
    catches your eye. Have a treat! An overhead surround sound plays Dilla
    which gets louder heading North, but East toward the windy breeze the electric city beckons. 
    A smell of delicious Mexican cuisine permiates the air and the fire stove oven wafts a smoke signal in the distance."""),

    'balcony': Room("Grand Overlook", """A highrise view of the amazing skyline appears before you. 
    Have a seat to take it all in or head back to keep it moving."""),

    'tacos': Room("Taco Hut", """The smell of delicious tacos at it's finest!
    Enjoy refueling and after your energy is up, head North to follow the sounds in the distance."""),

    'party': Room("Wolf Pack Party", """You've found Dj Kwest-on's amazing 
    Dance Party where all your friends are dancing! To get to the after party you have
    to dance it up! Use a combination of arrow keys to dance. Hint: down arrow is really getting down """),
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
print(Room('outside'))
while True:
    answer = input("Flip burgers"(f) or "Head south"(s)).lower().strip()
    try:
        if answer == "f":
            times = 0
            if answer <= 6:
                print(f"keep flipping")
            else:
                print(f"All good! Do you want to flip more? or head inside?"):
                answer = input("Flip burgers"(f) "Head south"(s)).lower().strip()
                answer == "yes"
                    if answer <= 4:
                        print("flip")
                    else:
                        print("These burgers are flipped and served! Are you ready to head inside or do you want to quit the game?")
                            answer = input("Head south"(s) "Quit game"(q)).lower().strip()
                                if answer == "s":
                                    print(Room(kitchen))
                                elif answer == "q":
                                    break
                    except ValueError:
                        print("PLease enter a valid number")
        elif answer == "s"
                print(Room(kitchen))
    except ValueError:
        print("PLease enter a valid number")


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#user = int(input("[n] North  [s] South  [e] East  [w] West  [9] Quit"))
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
