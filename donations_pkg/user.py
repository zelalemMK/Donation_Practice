def login(database, username, password):
    """Log in functionality"""

    if username in database.keys():
        if password in database.values():
            print(f"Welcome back {username}!")
            return username
        else:
            print("Wrong password")
            return ""
    else:
        print("User not found.\nPlease press 2 toRegister.")
        return ""


def register(database, username):
    if username in database.keys():
        print("Username already registered.")
        return ""
    else:
        print("Username registered!")
        return username