# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def__init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f"{self.name}: {self.description}"
    def __repr__(self):
        return f"self.name = {self.name} ; self.attributes = 

#outside_room = Room("", "", [])
#kitchen_room = Room("", "", [])
#balcony_room = Room("", "", [])
#tacos_room = Room("", "", [])
#party_room = Room("", "", [])
