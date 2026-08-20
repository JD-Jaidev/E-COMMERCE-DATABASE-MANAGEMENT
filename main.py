import getpass
import stdiomask

from database import Database
from services.user_service import UserService
from services.product_service import ProductService
from services.cart_service import CartService
from services.order_service import OrderService


class ECommerceApp:
    def __init__(self):
        print("------------------------- E - Commerce Database Management System -------------------------")
        host = "localhost"
        user = "root"
        password = stdiomask.getpass(prompt = "MySQL password: " , mask = '*')
        database = "ecommerce_db"

        self.db = Database(host, user, password, database)
        self.db.create_tables()

        self.user_service = UserService(self.db)
        self.product_service = ProductService(self.db)
        self.cart_service = CartService(self.db)
        self.order_service = OrderService(self.db, self.cart_service)

        self.current_user = None
        self.current_employee = None

    def run(self):
        while True:
            print("\n1. User Login")
            print("2. User Register")
            print("3. Employee Login")
            print("0. Exit")
            choice = input("Choice: ").strip()

            if choice == "1":
                self.user_login()
            elif choice == "2":
                self.user_register()
            elif choice == "3":
                self.employee_login()
            elif choice == "0":
                self.db.close()
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

    def user_register(self):
        name = input("Name: ").strip()
        email = input("Email: ").strip()
        user = self.user_service.register_user(name, email)
        if user:
            print("Registered successfully. You can now login with your email.")

    def user_login(self):
        email = input("Email: ").strip()
        user = self.user_service.login_user(email)
        if not user:
            print("User not found. Please register first.")
            return
        self.current_user = user
        print(f"Welcome {user.name}!")
        self.user_menu()

    def employee_login(self):
        name = input("Employee name: ").strip()
        password = getpass.getpass("Password: ")
        employee = self.user_service.login_employee(name, password)
        if not employee:
            print("Invalid employee name or password.")
            return
        self.current_employee = employee
        print(f"Welcome {employee.name}!")
        self.employee_menu()

    def user_menu(self):
        while True:
            print("\n------------------------- User Menu -------------------------")
            print("1. Display products")
            print("2. Add to cart")
            print("3. View cart")
            print("4. Checkout")
            print("5. My orders")
            print("0. Logout")
            choice = input("Choice: ").strip()

            if choice == "1":
                self.product_service.display_products()
            elif choice == "2":
                try:
                    product_id = int(input("Product ID: "))
                    quantity = int(input("Quantity: "))
                    self.cart_service.add_to_cart(self.current_user.user_id, product_id, quantity)
                except ValueError:
                    print("Please enter valid numbers.")
            elif choice == "3":
                cart = self.cart_service.get_cart(self.current_user.user_id)
                print(cart.display())
            elif choice == "4":
                self.order_service.checkout(self.current_user.user_id)
            elif choice == "5":
                self.order_service.show_user_orders(self.current_user.user_id)
            elif choice == "0":
                self.current_user = None
                print("Logged out.")
                break
            else:
                print("Invalid choice.")

    def employee_menu(self):
        while True:
            print("\n--- Employee Menu ---")
            print("1. Display products")
            print("2. Add product")
            print("3. Update product")
            print("0. Logout")
            choice = input("Choice: ").strip()

            if choice == "1":
                self.product_service.display_products()
            elif choice == "2":
                name = input("Product name: ").strip()
                try:
                    price = float(input("Price: "))
                    stock = int(input("Stock: "))
                except ValueError:
                    print("Please enter valid numbers.")
                    continue
                category = input("Category: ").strip() or "General"
                self.product_service.add_product(name, price, stock, category)
            elif choice == "3":
                try:
                    product_id = int(input("Product ID: "))
                    name = input("New name: ").strip()
                    price = float(input("New price: "))
                    stock = int(input("New stock: "))
                except ValueError:
                    print("Please enter valid numbers.")
                    continue
                category = input("New category: ").strip() or "General"
                self.product_service.update_product(product_id, name, price, stock, category)
            elif choice == "0":
                self.current_employee = None
                print("Logged out.")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = ECommerceApp()
    app.run()
