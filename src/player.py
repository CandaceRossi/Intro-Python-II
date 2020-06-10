# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def__init__(self, name, attributes, hunger, eat, is_man=False):
        self.name = name
        self.attributes = attributes
        self.rooms = rooms
        self.hunger = hunger
        self.eat = eat
        self.is_man = is_man
    def eat(self, food):
        if food > 0 and hunger < 25:
            hunger += food

#  def __str__(self):
#         #return a string representing the store
#         output = f"Welcome to {self.name}!"
#         i = 1
#         for attribute in self.attributes:
#             output += f'\n {i}{str(attribute.name)}'
#             i += 1
#         return output
#         return f"Welcome to {self.name}: Here are the attributes" {self.attributes}"

class Renee(Player):
    def__init__(self, name, attributes, hunger, eat):
    super().__init__( name, attributes, hunger, eat)
    # self.donutexcitement = donutexcitement

    def donutexcitement(self, donut):
        if donut == 1:
            print("Donuts are the best meal of the day. Not up for debate!")
class Ashley(Player):
    def__init__(self, name, attributes, hunger, eat):
    super().__init__( name, attributes, hunger, eat)
       

class Alex(Player):
    def__init__(self, name, attributes, hunger, eat):
    super().__init__(name, attributes, hunger, eat, is_man=True)
    # self.donutexcitement = donutexcitement   
    def donutexcitement(self, donut):
        if donut == 1:
            print("Donuts like the late great Dilla. Let's do this!")
class Candace(Player):
    def__init__(self, name, attributes, hunger, eat):
    super().__init__( name, attributes, hunger, eat)   

