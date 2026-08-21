from models.product import Product


class ProductService:
    def __init__(self, db):
        self.db = db

    def display_products(self):
        rows = self.db.execute("SELECT * FROM products ORDER BY product_id", fetch=True)
        if not rows:
            print("No products found.")
            return
        print("\n------------------------- Product List -------------------------")
        for row in rows:
            product = Product(
                row["name"],
                row["price"],
                row["stock"],
                row["category"],
                row["product_id"],
            )
            print(product.display())

    def get_product(self, product_id):
        rows = self.db.execute(
            "SELECT * FROM products WHERE product_id = %s",
            (product_id,),
            fetch=True,
        )
        if not rows:
            return None
        row = rows[0]
        return Product(row["name"], row["price"], row["stock"], row["category"], row["product_id"])

    def add_product(self, name, price, stock, category):
        product_id = self.db.execute(
            "INSERT INTO products (name, price, stock, category) VALUES (%s, %s, %s, %s)",
            (name, price, stock, category),
        )
        print(f"Product added with ID {product_id}.")

    def update_product(self, product_id, name, price, stock, category):
        product = self.get_product(product_id)
        if not product:
            print("Product not found.")
            return
        self.db.execute(
            """
            UPDATE products
            SET name = %s, price = %s, stock = %s, category = %s
            WHERE product_id = %s
            """,
            (name, price, stock, category, product_id),
        )
        print("Product updated.")
