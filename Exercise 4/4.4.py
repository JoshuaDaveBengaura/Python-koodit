import random
num = random.randint(1,10)

guess = int(input("Guess what number I'm thinking of? :^) "))

while True:
    if guess == num:
        print("THAT'S CORRECT! :^D")
        break
    elif guess > num:
        print("Too high")
        guess = int(input("Try again :^) "))
    elif guess < num:
        print("Too low")
        guess = int(input("Try again :^) "))


