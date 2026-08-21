from models.user import User, Employee

class UserService:
    def __init__(self, db):
        self.db = db

    def register_user(self, name, email):
        existing = self.db.execute(
            "SELECT user_id FROM users WHERE email = %s",
            (email,),
            fetch=True,
        )
        if existing:
            print("This email is already registered.")
            return None
        user_id = self.db.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (name, email),
        )
        return User(name, email, user_id)

    def login_user(self, email):
        rows = self.db.execute(
            "SELECT * FROM users WHERE email = %s",
            (email,),
            fetch=True,
        )
        if not rows:
            return None
        row = rows[0]
        return User(row["name"], row["email"], row["user_id"])

    def login_employee(self, name, password):
        rows = self.db.execute(
            "SELECT * FROM employees WHERE name = %s",
            (name,),
            fetch=True,
        )
        if not rows:
            return None
        employee = Employee(rows[0]["name"], rows[0]["password"], rows[0]["employee_id"])
        if employee.check_password(password):
            return employee
        return None
