user = input("Enter username ")
password = input("Enter password ")
attempts = 1

while attempts < 5:
    if user == "python" and password == "rules":
        print("Welcome")
        break
    else:
        attempts += 1
        print("Icorrect credentials, please try again")
        user = input("Enter username ")
        password = input("Enter password ")
if attempts == 5:
    print("Access Denied")



