num = float(input("Enter a number in inches: "))
while num > 0:
    print("That is", num * 2.54, "in centimetres")
    num = float(input("Enter another number in inches: "))
    if num < 0:
        print("An unexpected error occured")
        break