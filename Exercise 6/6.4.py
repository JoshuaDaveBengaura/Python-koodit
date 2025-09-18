numbers = []

def add():
    while True:
        num = int(input("Enter a number to add to the list, or enter 0 to end: "))
        numbers.append(num)
        if num == 0:
            break
    return print("The sum of the numbers are", sum(numbers))
add()