class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def subtotal(self):
        return self.product.price * self.quantity

    def display(self):
        return f"{self.product.name} x {self.quantity} = ${self.subtotal():.2f}"


class Cart:
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total(self):
        return sum(item.subtotal() for item in self.items)

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            return "Cart is empty."
        lines = [item.display() for item in self.items]
        lines.append(f"Total: ${self.total():.2f}")
        return "\n".join(lines)
