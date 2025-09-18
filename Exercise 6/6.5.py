def even(num):
    even = []
    for n in num:
        if n % 2 == 0:
           even.append(n)
    return even
def main():
    set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(set)
    print(even(set))
    return
main()
