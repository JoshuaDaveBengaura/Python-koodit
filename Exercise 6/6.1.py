import random

def dice():
    return random.randint(1, 6)

def main():
    result = 0
    while result != 6:
        result = dice()
        print("Dice rolled, you got", result)

main()
