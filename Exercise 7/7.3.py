def main():
    airports = {"EFHK":"Helsinki-Vantaa Airport"}
    while True:
        print("1. Enter new airport")
        print("2. Fetch airport info")
        print("3. Quit")
        choice = input("Your choice (1,2,3): ")
        if choice == "1":
            icao = input("Enter ICAO code: ")
            name = input("Enter airport name: ")
            airports[icao] = name
            print(f"Airport {icao}-{name} added")
        elif choice == "2":
            icao = input("Enter ICAO code: ")
            if icao in airports:
                print(f"{icao} - {airports[icao]}")
            else:
                print(f"No information found for ICAO code {icao}.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3")

main()