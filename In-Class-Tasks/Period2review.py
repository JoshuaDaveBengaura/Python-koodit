class Food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def info(self):
        print(f"Food: {self.name}, NUMBER OF CALORIES: {self.calories}")

class Fruit (Food):
    def __init__(self, name, calories, is_sweet):
        super().__init__(name, calories)
        self.is_sweet = is_sweet

    def info(self):
        super().info()
        print(f"Sweet: {'Yes' if self.is_sweet else 'No'}")

class Vegetable(Food):
    def __init__(self, name, calories, is_leafy):
        super().__init__(name, calories)
        self.is_leafy = is_leafy

    def print_info(self):
        super().info()
        print(f"Leafy: {'Yes' if self.is_leafy else 'No'}")

class Store:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item):
        self.inventory[item.name.lower()] = item

    def show_inventory(self):
        for i in self.inventory.values():
            i.info()

    def buy(self, product_name):
        name = product_name.lower()
        if name in self.inventory:
            return self.inventory[name]
        else:
            return None

class Smoothie:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

        total = 0
        for ingredient in ingredients:
            total += ingredient.calories

        self.total_calories = total

    def smoothie_info(self):
        print(f"Smoothie name:", self.name)
        print("Smoothie ingredients: ")

        for item in self.ingredients:
            print("-", item.name)

        print("Total calories:", self.total_calories)


store = Store()
store.add_item(Fruit("Apple", 52, True))
store.add_item(Fruit("Banana", 89, True))
store.add_item(Vegetable("Carrot", 41, False))

print("Welcome to the store!")
store.show_inventory()

ingredients = []
while True:
    choice = input("what do you wanna buy?/or type 'done': ")
    if choice.lower() == 'done':
        break
    item = store.buy(choice)
    if item:
        ingredients.append(item)
        print(f"{item.name} added.")
    else:
        print("not in store")

if ingredients:
    name = input("what is the smoothie called?: ")
    smoothie = Smoothie(name, ingredients)
    smoothie.smoothie_info()
else:
    print("cancelled")