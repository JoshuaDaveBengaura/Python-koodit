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

cars = []
for n in range(1, 11):
    cars.append(Car(f"ABC-{n}", random.randint(100,200)))

while max(car.travelled_distance for car in cars) < 10000:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travelled_distance >= 10000:
            winners = []
            for w in cars:
                if w.travelled_distance >= 10000:
                    winners.append(w)
            if len(winners) >= 2:
                print(f"CAR: {car.registration_number} PASSED THE FINNISH LINE!")
                print("IT'S A TIE!")
            elif len(winners) == 1:
                print(f"CAR: {car.registration_number} PASSED THE FIINNISH LINE!")

print()
print("RESULTS TABLE")
print("REG NUMBER / MAX SPEED / CURRENT SPEED / TRAVELED DISTANCE")
for car in cars:
    print(f"{car.registration_number}        {car.maximum_speed}         {car.current_speed}             {car.travelled_distance}")
