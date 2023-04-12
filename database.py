from user import User


class Database:

    users_list = []

    @staticmethod
    def greetings():
        print("Welcome to the insurance database app. Choose one of the actions bellow:\n")

    def create_user(self):
        user = User(input("Name: ").title(),
                    input("Surname: ").title(),
                    input("Date of birth [DD.MM.YYYY]: "),
                    input("Phone number: "))
        self.users_list.append(user)
        print("You have created the user:\n"
              "Name: {0}\n"
              "Surname: {1}\n"
              "Date of birth: {2}\n"
              "Phone number: {3}".format(user.name, user.surname, user.date_of_birth, user.phone_number))

    def list_all_users(self):
        enum_dtbz = enumerate(self.users_list, start=1)
        print("All users:")
        for index, user in enum_dtbz:
            print(f"{index}) {user}")

        for user in self.users_list:
            print(user)

    def search_for_a_user(self):
        searching = input("Enter the keyword:\n").upper()

        for user in self.users_list:
            if (user.name.upper() == searching
                    or user.surname.upper() == searching
                    or user.date_of_birth == searching
                    or user.phone_number == searching):
                print(user.name, user.surname, user.date_of_birth, user.phone_number)

    def remove_user(self):
        print("Enter an ID of user you want to delete: ")
        enum_dtbz = enumerate(self.users_list, start=1)
        for index, user in enum_dtbz:
            print(f"{index}) {user}")

        delete_again = True
        while delete_again:
            try:

                delete_user = int(input())
                delete_user -= 1
                if delete_user >= 0:
                    self.users_list.remove(self.users_list[delete_user])

                    enum_dtbz = enumerate(self.users_list, start=1)
                    print("Updated database:")
                    for index, user in enum_dtbz:
                        print(f"{index}) {user}")
                    delete_again = False
                else:
                    raise IndexError

            except IndexError:
                print("Error, user with ID you have entered does not exist, try again:")
                enum_dtbz = enumerate(self.users_list, start=1)
                for index, user in enum_dtbz:
                    print(f"{index}) {user}")
                delete_again = True
