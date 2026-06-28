from product import Product
class Ecommercesystem:
    def __init__(self):
        self.products = []
        self.cart = []

    def add_product(self):
        product_id = int(input("enter product id:"))
        name = input("enter product name:")
        price = int(input("enter product price:"))
        product = Product(product_id, name, price)
        self.products.append(product)
        print("product added sucessfully.")

    def display_products(self): 
        if len(self.products) == 0:
            print("no product available.")
        else:
            for product in self.products:
                product.display() 

    def search_product(self):
        product_id = int(input("enter product id to search:"))
        for product in self.products:
            if product.product_id == product_id:
                print("product found.")
                product.display()
                return
        print("product not found.") 

    def add_to_cart(self):
        product_id = int(input("enter product id to add to cart:"))
        for product in self.products:
            if product.product_id == product_id:
                self.cart.append(product)
                print("product added to cart sucessfully.")
                return
        print("product not found.")

    def view_cart(self):
        if len(self.cart) == 0:
            print("cart is empty.")
        else:
            total = 0
            print("items in cart")
            print("-" * 30)
            for product in self.cart:
                print(f"{product.name} - ₹{product.price}")
                total += product.price
            print("-" * 30)
            print("total amount: ₹", total)    
                     



                           