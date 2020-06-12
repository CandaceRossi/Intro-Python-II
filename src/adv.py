from room import Room
from player import Player

# Declare all the rooms


outside = Room("Outside Backyard", """A barbeque grill sits in the center of a well groomed 
yard. Pre-party time! Flip some burgers to feed some friends. Just South of you lies the lit up skyline. 
For a better view, head inside the house.""")

kitchen = Room("Kitchen", """Under a dim light a plate stacked with delicious donuts
catches your eye. Have a treat! An overhead surround sound plays Dilla
which gets louder heading North, but East toward the windy breeze the electric city beckons. 
A smell of delicious Mexican cuisine permiates the air and the fire stove oven wafts a smoke signal in the distance."""),

balcony = Room("Grand Overlook", """A highrise view of the amazing skyline appears before you. 
Have a seat to take it all in or head back to keep it moving.""")

tacos = Room("Taco Hut", """The smell of delicious tacos at it's finest!
Enjoy refueling and after your energy is up, head North to follow the sounds in the distance.""")

party = Room("Wolf Pack Party", """You've found Dj Kwest-on's amazing 
Dance Party where all your friends are dancing! To get to the after party you have
to dance it up! Use a combination of arrow keys to dance. Hint: down arrow is really getting down """)


# Link rooms together

outside.n_to = kitchen
kitchen.s_to = outside
kitchen.n_to = balcony
kitchen.e_to = tacos
balcony.s_to = kitchen
tacos.w_to = kitchen
tacos.n_to = party
party.s_to = tacos

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
renee_player = Player("Renee", outside, 35, 10)
renee_player.current_room = outside
while True:
# Write a loop that:
    # * Prints the current room name
    print(renee_player.current_room)
    # * Prints the current description (the textwrap module might be useful here).
    print(renee_player.current_room.description)
    # * Waits for user input and decides what to do.
    choice = input("type a direction")
    #user = int(input("[n] North  [s] South  [e] East  [w] West  [9] Quit"))
    # If the user enters a cardinal direction, attempt to move to the room there.
    if choice == 'n':
        #check if the current room has a n_to attribute
        if renee_player.current_room.n_to is not None:
            #move the player to that room
            renee_player.current_room = renee_player.current_room.n_to
        
    elif choice == 's':
        #check if the current room has a n_to attribute
        if renee_player.current_room.s_to is not None:
            #move the player to that room
            renee_player.current_room = renee_player.current_room.s_to    
        
        
    elif choice == 'e':
        #check if the current room has a n_to attribute
        if renee_player.current_room.e_to is not None:
            #move the player to that room
            renee_player.current_room = renee_player.current_room.e_to    
        
    elif choice == 'w':
        #check if the current room has a n_to attribute
        if renee_player.current_room.w_to is not None:
            #move the player to that room
            renee_player.current_room = renee_player.current_room.w_to    
        
        
    #if choice in {'n', 's', 'e', 'w'}:
    #   if hasattr(renee_player.current_room, f'{choice}_to'):   
    #       renee_player.current_room = getattr(renee_player.current_room, f'{choice}_to')
        

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


















