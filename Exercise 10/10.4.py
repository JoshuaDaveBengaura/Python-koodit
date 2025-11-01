import random

class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change_speed):
        self.current_speed += change_speed

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours_travelled):
        travelled = self.current_speed * hours_travelled

        self.travelled_distance += travelled

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print("REG NUMBER / MAX SPEED / CURRENT SPEED / TRAVELED DISTANCE")
        for car in self.cars:
            print(
                f"{car.registration_number}        {car.maximum_speed}         {car.current_speed}             {car.travelled_distance}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)

cars = []
for n in range(1, 11):
    cars.append(Car(f"ABC-{n}", random.randint(100,200)))

race = Race("Race", 8000, cars)

hours = 0
lap = 10
while race.race_finished() == False:
    race.hour_passes()
    hours += 1
    if hours == lap:
        print("Hour", hours)
        race.print_status()
        lap += 10

print("FINAL STATUS after", hours, "hours")
for car in race.cars:
    print(car.registration_number, car.current_speed, car.travelled_distance)

winners = []
for w in cars:
    if w.travelled_distance >= race.distance:
        winners.append(w)

if len(winners) >= 2:
    for w in winners:
        print(f"CAR: {w.registration_number} PASSED THE FINISH LINE!")
    print("IT'S A TIE!")
elif len(winners) == 1:
    for w in winners:
        print(f"CAR: {w.registration_number} PASSED THE FINISH LINE!")
