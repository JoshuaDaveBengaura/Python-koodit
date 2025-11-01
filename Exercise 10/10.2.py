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

class Building():
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator_count = elevator_count
        self.building_elevators = [Elevator(bottom_floor, top_floor) for e in range(elevator_count)]

    def run_elevator(self, elevator_number, floor_number):
        if elevator_number > self.elevator_count or elevator_number < 1:
            print("ELEVATOR DOES NOT EXIST")
        elif floor_number > self.top_floor or floor_number < 1:
            print("FLOOR DOES NOT EXIST")
        else:
            print(f"RUNNING ELEVATOR {elevator_number}")
            self.building_elevators[elevator_number - 1].go_to_floor(floor_number)




metropolia = Building(1, 7, 4)
metropolia.run_elevator(1, 7)
print()
metropolia.run_elevator(2, 6)
print()
metropolia.run_elevator(3, 4)
print()
metropolia.run_elevator(4, 5)




