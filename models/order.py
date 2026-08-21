class OrderItem:
    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = float(price)

    def line_total(self):
        return self.price * self.quantity

    def display(self):
        return f"  {self.product_name} x {self.quantity} = ₹{self.line_total():.2f}"


class Order:
    def __init__(self, user_id, total_amount, order_id=None, order_date=None):
        self.order_id = order_id
        self.user_id = user_id
        self.total_amount = float(total_amount)
        self.order_date = order_date
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display(self):
        lines = [
            f"Order #{self.order_id} | Total: ₹{self.total_amount:.2f} | Date: {self.order_date}"
        ]
        for item in self.items:
            lines.append(item.display())
        return "\n".join(lines)
