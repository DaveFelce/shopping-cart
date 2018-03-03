class User:

    def __init__(self, name):
        self.name = name
        self.carts = {}

    def add_cart(self, cart):
        self.carts[cart.cart_id] = cart

    def get_cart_by_id(self, cart_id):
        return self.carts[cart_id]