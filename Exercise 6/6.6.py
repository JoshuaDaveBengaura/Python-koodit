import math

def calculate(s, price):
    rad = s / 200
    area = math.pi * rad ** 2
    return price / area

size1 = float(input("Pizza 1 diameter (cm): "))
cost1 = float(input("Pizza 1 price (€): "))

size2 = float(input("Pizza 2 diameter (cm): "))
cost2 = float(input("Pizza 2 price (€): "))

final1 = calculate(size1, cost1)
final2 = calculate(size2, cost2)

print("Pizza 1:", round(final1, 2), "€/m²")
print("Pizza 2:", round(final2, 2), "€/m²")

if final1 < final2:
    print("Pizza 1 is better value.")
elif final1 > final2:
    print("Pizza 2 is better value.")
else:
    print("Both are the same value.")