import re


class User(object):
    def __init__(self, first_name, last_name, email):
        """Initialization first name, last name, email"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @property
    def f_name(self):
        return self.first_name

    @f_name.setter
    def f_name(self, other):
        self.first_name = other

    @property
    def l_name(self):
        return self.last_name

    @l_name.setter
    def l_name(self, other):
        self.last_name = other

    @property
    def em(self):
        return self.email

    @em.setter
    def em(self, other):
        if self.is_valid_email(other):
            self.email = other
        else:
            print(f"Невірний формат email: {other}")

    @staticmethod
    def is_valid_email(email):
        """A method to check if an email is valid"""
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def __repr__(self):
        """Returns representation User"""
        return f"User({self.first_name}, {self.last_name}, {self.email})"


def testing_user():
    user = User("Dima", "Vilar", "dima.vilar@gmail.com")
    print(user)
    user.f_name = "Roma"
    print(print(f"Після зміни first_n: {user.f_name}"))
    user.l_name = "Smith"
    print(f"Після зміни last_name: {user.l_name}")
    user.email = "roma.smith@example.com"
    print(f"Після зміни email: {user.email}")


testing_user()
