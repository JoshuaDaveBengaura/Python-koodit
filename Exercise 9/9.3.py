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



car = Car("ABC-123", 142)

print("Registration number:", car.registration_number)
print("Maximum speed:", car.maximum_speed,"km/h")
print("Travelled distance:", car.travelled_distance)
print()

car.accelerate(30)
print("Current speed:", car.current_speed,"km/h")
car.accelerate(70)
print("Current speed:", car.current_speed,"km/h")
car.accelerate(50)
print("Current speed:", car.current_speed,"km/h")
if car.current_speed == car.maximum_speed:
    print("WE ZOOMIN BABY!")

print()
print("EMERGENCY BRAKE!")
car.accelerate(-200)
print("Current speed:", car.current_speed,"km/h")

print()
car.accelerate(142)
car.drive(1.5)
print("Current speed:", car.current_speed,"km/h")
print("Travelled distance:", car.travelled_distance)
