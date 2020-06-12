from room import Room
from player import Player
from items import Items


#Declare all the items

burgers = Items("Burgers", "Press (f) to flip the burgers until they'r all flipped")
donuts = Items("Donuts", "Press (e) to eat donuts to your player's satisfaction")
sitting = Items("Sit", "Press (s) to sit down")
tacos = Items("Tacos", "Press (e) to eat tacos to your player's satisfaction")
dancing = Items("Dance", "Press (d) to dance to really get down")

#Declare all the rooms

outside = Room("Outside Backyard", """A barbeque grill sits in the center of a well groomed yard. 
Pre-party time! 
Flip some burgers to feed some friends. 
Just South of you lies the lit up skyline. 
For a better view, head inside the house.""", [burgers])

kitchen = Room("Kitchen", """Under a dim light a plate stacked with delicious donuts
catches your eye. Have a treat! 
An overhead surround sound plays Dilla which gets louder heading North, 
but East toward the windy breeze the electric city beckons. 
A smell of delicious Mexican cuisine permiates the air 
and the fire stove oven wafts a smoke signal in the distance.""", [donuts])

balcony = Room("Grand Overlook", """A highrise view of the amazing skyline appears before you. 
Have a seat to take it all in or head back to keep it moving.""", [sitting])

tacos = Room("Taco Hut", """The smell of delicious tacos at it's finest!
Enjoy refueling and after your energy is up, 
head North to follow the sounds in the distance.""", [tacos])

party = Room("Wolf Pack Party", """You've found Dj Kwest-on's amazing 
Dance Party where all your friends are dancing! To get to the after party you have
to dance it up! Use a combination of arrow keys to dance. 
Hint: down arrow is really getting down """, [dancing])


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
print("\n______Wolfpack Adventure______\n    ...An adventure awaits...")

# print(f'\n You are currently at the {}')
# Make a new player object that is currently in the 'outside' room.
renee_player = Player("Renee", outside)
renee_player.current_room = outside
direction = ["n", "s", "e", "w"]
choice = " "
# while True:
while choice not in direction:
# Write a loop that:
    # * Prints the current room name
    print(renee_player.current_room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print(renee_player.current_room.description + "\n")
    if len(renee_player.current_room.items) > 0:
        print(f"Mmm smells good!")
        for item in renee_player.current_room.items:
            print(item)
    else:
        print(f"This room has no items")
    # * Waits for user input and decides what to do
    choice = input("""Or make another selection:\n (n) - Move North\n (s) - Move South\n (e) - Move East\n (w) - Move West\n (f) - Flip Burgers\n""")

    if choice == 'f':
        if len(choice) <= 6:
            print(f"keep flipping")
        elif len(choice) == 7: 
            break 
            print(f"All Good! Burgers are flipped")
        else:
            print(f"invalid selection")
    else:
        choice = input("""Make another selection:\n (n) - Move North\n (s) - Move South\n (e) - Move East\n (w) - Move West\n""") 
    # * Print items in current room 
    # print(renee_player.current_room.items[0].name)
        # if len(renee_player.current_room.items) >= 1:
        #     for i in renee_player.current_room.items:
        #         print(f"{i} catches your eye")
    # * Waits for user input and decides what to do.
    # choice = input("type a direction")
    #user = int(input("[n] North  [s] South  [e] East  [w] West  [9] Quit"))
    # If the user enters a cardinal direction, attempt to move to the room there.
    if choice == 'n':
        #check if the current room has a n_to attribute
        if renee_player.current_room.n_to is not None:
            #move the player to that room
            renee_player.current_room = renee_player.current_room.n_to
        else:
            print(f"You can't move in that direction.")
    elif choice == 's':
        #check if the current room has a n_to attribute
        if renee_player.current_room.s_to is not None:
            #move the player to that room
            renee_player.current_room = renee_player.current_room.s_to    
        else:
            print(f"You can't move in that direction.")
        
    elif choice == 'e':
        #check if the current room has a n_to attribute
        if renee_player.current_room.e_to is not None:
            #move the player to that room
            renee_player.current_room = renee_player.current_room.e_to    
        else:
            print("You can't move in that direction.")
    elif choice == 'w':
        #check if the current room has a n_to attribute
        if renee_player.current_room.w_to is not None:
            #move the player to that room
            renee_player.current_room = renee_player.current_room.w_to    
        else:
            print("You can't move in that direction.")
    elif choice == 'q':
        break    


    #if choice in {'n', 's', 'e', 'w'}:
    #   if hasattr(renee_player.current_room, f'{choice}_to'):   
    #       renee_player.current_room = getattr(renee_player.current_room, f'{choice}_to')
        

# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


















