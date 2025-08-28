cabin = input("What is your chosen cabin class? ").lower()
if cabin == "a":
    print("Located above the car deck, equipped with a window.")
elif cabin == "b":
    print("Windowless cabin above the car deck.")
elif cabin == "c":
    print("Windowless cabin below the car deck.")
elif cabin == ("lux"):
    print("Upper-deck cabin with a balcony.")
else:
    print("This cabin doesn't exist.")
