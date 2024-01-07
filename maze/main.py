class Room:
    def __init__(self, name):
        self.name = name
        self.doors = []

    def add_door(self, door):
        self.doors.append(door)

    def view_all_doors(self):
        return self.doors


class Door:
    def __init__(self, first_room, second_room):
        self.first_room = first_room
        self.second_room = second_room

    def get_next_room(self, current_room):
        if current_room == self.first_room:
            return self.second_room
        elif current_room == self.second_room:
            return self.first_room
