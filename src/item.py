class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return f"{self.name}: {self.description}"
    
    def add_item(self, room):
        print({})

burger = Item("Burgers", "Press (f) to flip the burgers until they'r all flipped")
donut = Item("Donuts", "Press (e) to eat donuts to your player's satisfaction")
chair = Item("Chair", "Press (s) to sit down")
taco = Item("Tacos", "Press (e) to eat tacos to your player's satisfaction")
dance = Item("Dance", "Press (d) to dance to really get down")