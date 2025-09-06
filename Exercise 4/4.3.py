num = []

while True:
    inp = input("Enter a number: ")
    if inp == "":
        print("Goodbye")
        break
    else:
        num.append(int(inp))

small = min(num)
big = max(num)
print("Your largest number is ", (big))
print("Your smallest number is ", (small))