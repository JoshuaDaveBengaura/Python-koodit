class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def info(self):
        print(f"This is {self.name}, he/she is a {self.species}")

    def do_sound(self):
        print(f"{self.name} has the sound: {self.sound}")

class Lion(Animal):
    def __init__(self, name, species = "Lion", sound = "Rawr"):
        self.sound = sound
        super().__init__(name, species)

class Elephant(Animal):
    def __init__(self, name = "Elephant", species = "Mammoth", sound = "HONK"):
        self.sound = sound
        super().__init__(name, species)

class Snake(Animal):
    def __init__(self, name, species = "Snake", sound = "SSSSSSNEK"):
        self.sound = sound
        super().__init__(name, species)

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(animal.name + " added")

    def all_sounds(self):
        print()
        print("MAKE SOME NOISE!")
        for s in self.animals:
            print(s.sound)

    def print_info(self):
        print()
        print(F"There are", len(self.animals), "animals in the zoo")
        for a in self.animals:
            print(a.name, "The", a.species, "and they make the sound", a.sound)

zoo = Zoo()

animal1 = Lion("Leo")
animal2 = Lion("Lio", "Cat", "Meowwwrrrr")
animal3 = Elephant("Lil guy")
animal4 = Elephant("Ellie", "Bush Elephant", "*wheeze*")
animal5 = Snake("Sssstephen")
animal6 = Snake("Sneyk", "Python", "Hello World")

zoo.add_animal(animal1)
zoo.add_animal(animal2)
zoo.add_animal(animal3)
zoo.add_animal(animal4)
zoo.add_animal(animal5)
zoo.add_animal(animal6)
zoo.print_info()
zoo.all_sounds()
