# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def__init__(self, name, attributes, is_man=False):
        self.name = name
        self.attributes = attributes
        self.rooms = rooms
        self.is_man = is_man
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
    def__init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
        self.rooms = rooms

class Ashley(Player):
    def__init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
        self.rooms = rooms

class Alex(Player):
    def__init__(self, name, attributes):
        super().__init__(name, is_man=True)
        self.name = name
        self.attributes = attributes
        self.rooms = rooms

class Candace(Player):
    def__init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
        self.rooms = rooms

