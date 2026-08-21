from models.order import Order, OrderItem


class OrderService:
    def __init__(self, db, cart_service):
        self.db = db
        self.cart_service = cart_service

    def checkout(self, user_id):
        cart = self.cart_service.get_cart(user_id)
        if cart.is_empty():
            print("Cart is empty. Cannot checkout.")
            return

        for item in cart.items:
            if item.product.stock < item.quantity:
                print(f"Not enough stock for {item.product.name}.")
                return

        order_id = self.db.execute(
            "INSERT INTO orders (user_id, total_amount) VALUES (%s, %s)",
            (user_id, cart.total()),
        )

        for item in cart.items:
            self.db.execute(
                """
                INSERT INTO order_items (order_id, product_id, quantity, price)
                VALUES (%s, %s, %s, %s)
                """,
                (order_id, item.product.product_id, item.quantity, item.product.price),
            )
            self.db.execute(
                "UPDATE products SET stock = stock - %s WHERE product_id = %s",
                (item.quantity, item.product.product_id),
            )

        self.cart_service.clear_cart(user_id)
        print(f"Checkout complete. Order ID: {order_id}")
        print(f"Total paid: ₹{cart.total():.2f}")

    def show_user_orders(self, user_id):
        orders = self.db.execute(
            "SELECT * FROM orders WHERE user_id = %s ORDER BY order_id",
            (user_id,),
            fetch=True,
        )
        if not orders:
            print("No orders yet.")
            return
        for row in orders:
            order = Order(row["user_id"], row["total_amount"], row["order_id"], row["order_date"])
            items = self.db.execute(
                """
                SELECT oi.quantity, oi.price, p.name
                FROM order_items oi
                JOIN products p ON oi.product_id = p.product_id
                WHERE oi.order_id = %s
                """,
                (row["order_id"],),
                fetch=True,
            )
            for item in items:
                order.add_item(OrderItem(item["name"], item["quantity"], item["price"]))
            print(order.display())
            print()
