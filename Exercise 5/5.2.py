num = []

while True:
    n = (input("Enter a number, or press Enter to quit: "))
    if n == "":
        print("Program terminated.")
        break
    number = int(n)
    num.append(number)


num.sort(reverse = True)

for i in num[:5]:
    print(i)
