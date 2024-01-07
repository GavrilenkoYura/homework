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

class Player:
    def __init__(self, name, start_room):
        self.name = name
        self.curr_room = start_room

    def look_around(self):
        doors = self.curr_room.view_all_doors()
        print(f'You are in {self.curr_room.name}.')
        print('The are doors leading to the following rooms:')
        for door in doors:
            print(door)

    def enter_room(self, door):
        self.curr_room = door.get_next_room(self.curr_room)
        self.look_around()