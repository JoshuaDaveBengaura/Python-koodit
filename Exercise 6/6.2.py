import random

sides = int(input("How many sides does the dice have? "))

def dice():
    return random.randint(1, sides)

def main():
    result = 0
    while result != sides:
        result = dice()
        print("Dice rolled, you got", result)

main()
