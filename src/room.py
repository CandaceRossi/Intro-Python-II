# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, s_to, e_to, w_to, n_to):
        self.name = name
        self.description = description
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.n_to = None
        # self.item = item  , item

    def __str__(self):
        output = '{self.name): {self.description}\n'
        if self.s_to:
            output += 'To the south is: ' + self.s_to.name + '\n'
        if self.e_to:
            output += 'To the east is: ' + self.e_to.name + '\n'
        if self.w_to:
            output += 'To the west is: ' + self.w_to.name + '\n'
        if self.n_to:
            output += 'To the north is: ' + self.n_to.name + '\n'
            
        return output

    # def start_room():
    #     start_room_options = ["outside", "kitchen", "balcony", "tacos", "party"]