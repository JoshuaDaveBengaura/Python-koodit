import random
N = int(input("How many dots do you want? "))
n = 0
i = 0

while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y < 1:
        n += 1
    i += 1

approx = 4 * n / N
print("The approximation of pi is", approx)