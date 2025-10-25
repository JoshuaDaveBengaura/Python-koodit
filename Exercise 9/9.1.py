class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

car = Car("ABC-123", "142 km/h")

print("Registration number:", car.registration_number)
print("Maximum speed:", car.maximum_speed)
print("Current speed:", car.current_speed)
print("Travelled distance:", car.travelled_distance)