import random
amount = int(input("Amount of dice to be rolled: "))

dice = []

for r in range(amount):
    roll = random.randint(1, 6)
    dice.append(roll)

print("Your dice results are", dice)
print("The sum of the dice is", sum(dice))