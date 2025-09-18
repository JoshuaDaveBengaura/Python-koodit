def main():
    names = set()

    while True:
        name = input("Enter a name or press Enter to end: ")
        if name == "":
            break
        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)
    for n in names:
        print(n)
    return

main()
