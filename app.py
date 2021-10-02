from donations_pkg.homepage import show_homepage, donate, show_donation
from donations_pkg.user import login, register

database = {"admin":"1234"}
donations = []
authorized_user = ""







while True:

    show_homepage()

    if authorized_user == "":
        print("You must be logged in.")
    else:
        print(f"Logged in as: {authorized_user}")

    choice = input("Choose your option: ")

    if choice == "1":
        
        username = input("Username: ")
        password = input("Password: ")
        authorized_user = login(database, username, password)
        
    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        authorized_user = register(database, username)
        if authorized_user:
            database[authorized_user] = password


    elif choice == "3":
        if not authorized_user:
            print("You are not logged in!")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
        
        
    elif choice == "4":
        show_donation(donations)
        
        
    elif choice == "5":
        print("Thank you for your time, Goodbye!")
        break
    else:
        print("Please choose between 1-5")



