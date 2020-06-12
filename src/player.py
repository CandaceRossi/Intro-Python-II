# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = list(items)

    # def __str__(self, item, room):
    def get_item(self, item, room):
        items = Items(self, room)
        self.room.append(items)
        #output= f"{self.name} is in {self.room.name} with {self.item[i].name}

        # , donut_hunger, taco_hunger
        # self.donut_hunger = donut_hunger
        # self.taco_hunger = taco_hunger
    

    # def __str__(self)
    #     output = f""  

    # def eat(self, food_item):
    #     if food_item == taco
