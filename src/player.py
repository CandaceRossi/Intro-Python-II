# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def__init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
        self.rooms = rooms

    def __str__(self):
        #return a string representing the store
        output = f"Welcome to {self.name}!"
        i = 1
        for attribute in self.attributes:
            output += f'\n {i}{str(attribute.name)}'
            i += 1
        return output
        return f"Welcome to {self.name}: Here are the attributes" {self.attributes}"

    def __repr__(self):
    #also returns a string
    return f"self.name = {self.name} ; self.attributes = 

outside_room = Room("Running", "All your running needs", [])
kitchen_room = Room("Baseball", "Blue Jays fans only", [])
balcony_room = Room("Basketball", "Indoor and outdoor products", [])
tacos_room = Room("Football", "The American kind", [])
party_room = Room("Football", "The American kind", [])
