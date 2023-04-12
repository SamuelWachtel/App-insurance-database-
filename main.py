from database import Database

users_database = Database()
next_choice = True
users_database.greetings()
while next_choice:
    try:
        choice = input("1 = Create new user\n"
                       "2 = List all users\n"
                       "3 = Search for a user\n"
                       "4 = Remove user\n"
                       "5 = Exit\n")
        next_choice = False

    except ValueError:
        print("Error, you didn't choose the right number.\n")
        choice = "."
        next_choice = True

    if choice == "1":
        users_database.create_user()
        print("\nChoose next step\n")
        next_choice = True

    elif choice == "2":
        users_database.list_all_users()
        print("\nChoose next step\n")
        next_choice = True

    elif choice == "3":
        users_database.search_for_a_user()
        print("\nChoose next step\n")
        next_choice = True

    elif choice == "4":
        users_database.remove_user()
        print("\nChoose next step\n")
        next_choice = True

    elif choice == "5":
        print("See you soon.")
        next_choice = False
    else:
        print("You didn't choose any action, please try again:\n")
        next_choice = True