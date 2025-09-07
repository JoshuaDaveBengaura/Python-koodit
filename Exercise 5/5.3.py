num = int(input("Enter an integer: "))

prime = True

if num <= 1:
    prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

if prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")