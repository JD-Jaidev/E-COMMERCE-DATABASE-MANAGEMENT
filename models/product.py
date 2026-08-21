class Product:
    def __init__(self, name, price, stock, category="General", product_id=None):
        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.stock = int(stock)
        self.category = category

    def display(self):
        return (
            f"ID: {self.product_id} | {self.name} | "
            f"₹{self.price:.2f} | Stock: {self.stock} | {self.category}"
        )
