class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.starting_floor = self.bottom_floor

    def floor_up(self):
        if self.starting_floor < self.top_floor:
            self.starting_floor +=1
            print(f"FLOOR: {self.starting_floor}")

    def floor_down(self):
        if self.starting_floor > self.bottom_floor:
            self.starting_floor -=1
            print(f"FLOOR: {self.starting_floor}")

    def go_to_floor(self, floor_number):

        while floor_number > self.starting_floor:
            self.floor_up()
            if floor_number == self.starting_floor:
                print(f"NOW AT FLOOR: {self.starting_floor}")

        while floor_number < self.starting_floor:
            self.floor_down()
            if floor_number == self.starting_floor:
                print(f"NOW AT FLOOR: {self.starting_floor}")



e1 = Elevator(1, 10)
e1.go_to_floor(5)
e1.go_to_floor(1)
e1.go_to_floor(10)

print()

e2 = Elevator(5, 15)
e2.go_to_floor(5)
e2.go_to_floor(10)
e2.go_to_floor(15)
e2.go_to_floor(20)