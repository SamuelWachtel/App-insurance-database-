class User:
    def __init__(self, name, surname, date_of_birth, phone_number):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.name, self.surname, self.date_of_birth, self.phone_number)