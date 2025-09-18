def convert():
    gal = float(input("Enter amount of gas in Gallons, or enter a negative number to cancel: "))
    while gal >= 0:
        print(f"{gal} in Liters is {gal * 3.78541}")
        gal = float(input("Enter amount of gas in Gallons, or enter a negative number to cancel: "))
        if gal < 0:
            print("Process cancelled")
    return

convert()