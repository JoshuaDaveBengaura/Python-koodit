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


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume


electric = ElectricCar("ABC-15", 180, 52.5)
gas = GasolineCar("ACD-123", 165, 32.3)

electric.accelerate(150)
gas.accelerate(120)

electric.drive(3)
gas.drive(3)

print(f"Electric car ({electric.registration_number}) travelled: {electric.travelled_distance} km")
print(f"Gasoline car ({gas.registration_number}) travelled: {gas.travelled_distance} km")