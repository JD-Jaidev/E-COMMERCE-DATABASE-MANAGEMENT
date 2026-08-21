class Person:
    """Base class for User and Employee."""

    def __init__(self, name):
        self.name = name

    def display(self):
        return self.name


class User(Person):
    def __init__(self, name, email, user_id=None):
        super().__init__(name)
        self.email = email
        self.user_id = user_id

    def display(self):
        return f"User: {self.name} ({self.email})"


class Employee(Person):
    def __init__(self, name, password, employee_id=None):
        super().__init__(name)
        self.password = password
        self.employee_id = employee_id

    def check_password(self, password):
        return self.password == password

    def display(self):
        return f"Employee: {self.name}"
