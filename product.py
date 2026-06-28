
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display(self):
        print(f"product_id: {self.product_id}")
        print(f"name      : {self.name}")
        print(f"price     : ₹{self.price}")
        print("-" * 50)
