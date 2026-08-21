from models.cart import Cart, CartItem
from models.product import Product


class CartService:
    def __init__(self, db):
        self.db = db

    def add_to_cart(self, user_id, product_id, quantity):
        rows = self.db.execute(
            "SELECT * FROM products WHERE product_id = %s",
            (product_id,),
            fetch=True,
        )
        if not rows:
            print("Product not found.")
            return
        product = rows[0]
        if product["stock"] < quantity:
            print("Not enough stock.")
            return

        existing = self.db.execute(
            "SELECT cart_id, quantity FROM cart_items WHERE user_id = %s AND product_id = %s",
            (user_id, product_id),
            fetch=True,
        )
        if existing:
            new_qty = existing[0]["quantity"] + quantity
            if product["stock"] < new_qty:
                print("Not enough stock.")
                return
            self.db.execute(
                "UPDATE cart_items SET quantity = %s WHERE cart_id = %s",
                (new_qty, existing[0]["cart_id"]),
            )
        else:
            self.db.execute(
                "INSERT INTO cart_items (user_id, product_id, quantity) VALUES (%s, %s, %s)",
                (user_id, product_id, quantity),
            )
        print("Item added to cart.")

    def get_cart(self, user_id):
        rows = self.db.execute(
            """
            SELECT c.quantity, p.product_id, p.name, p.price, p.stock, p.category
            FROM cart_items c
            JOIN products p ON c.product_id = p.product_id
            WHERE c.user_id = %s
            """,
            (user_id,),
            fetch=True,
        )
        cart = Cart(user_id)
        for row in rows:
            product = Product(
                row["name"],
                row["price"],
                row["stock"],
                row["category"],
                row["product_id"],
            )
            cart.add_item(CartItem(product, row["quantity"]))
        return cart

    def clear_cart(self, user_id):
        self.db.execute("DELETE FROM cart_items WHERE user_id = %s", (user_id,))
