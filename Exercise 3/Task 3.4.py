year = int(input("Give me a year "))
if year % 4 == 0:
    print("The year is a leap year.")
elif year % 100 % 400 == 0:
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")
