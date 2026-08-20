import mysql.connector


class Database:
    """Simple MySQL connection helper."""

    def __init__(self, host="localhost", user="root", password="", database="ecommerce_db"):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
        )

    def execute(self, query, values=None, fetch=False):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query, values or ())
        if fetch:
            result = cursor.fetchall()
            cursor.close()
            return result
        self.conn.commit()
        last_id = cursor.lastrowid
        cursor.close()
        return last_id

    def create_tables(self):
        self.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(150) NOT NULL UNIQUE
            )
            """
        )
        self.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                employee_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL UNIQUE,
                password VARCHAR(100) NOT NULL
            )
            """
        )
        self.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                product_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(150) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                stock INT NOT NULL,
                category VARCHAR(100)
            )
            """
        )
        self.execute(
            """
            CREATE TABLE IF NOT EXISTS cart_items (
                cart_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                product_id INT NOT NULL,
                quantity INT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            )
            """
        )
        self.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                order_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                total_amount DECIMAL(10, 2) NOT NULL,
                order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
            """
        )
        self.execute(
            """
            CREATE TABLE IF NOT EXISTS order_items (
                item_id INT AUTO_INCREMENT PRIMARY KEY,
                order_id INT NOT NULL,
                product_id INT NOT NULL,
                quantity INT NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                FOREIGN KEY (order_id) REFERENCES orders(order_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            )
            """
        )
        self._add_default_employee()

    def _add_default_employee(self):
        rows = self.execute(
            "SELECT employee_id FROM employees WHERE name = %s",
            ("admin",),
            fetch=True,
        )
        if not rows:
            self.execute(
                "INSERT INTO employees (name, password) VALUES (%s, %s)",
                ("admin", "admin123"),
            )

    def close(self):
        self.conn.close()
