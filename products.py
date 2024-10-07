class Product:
    def __init__(self, product_name: str, price: float, quantity: int, active: bool = True):

        if not isinstance(product_name, str):
            raise TypeError(f"Expected a string but you entered a {type(product_name)}")
        if not isinstance(price, float):
            raise TypeError(f"Expected a float but you entered a {type(price)}")
        if not isinstance(quantity, int):
            raise TypeError(f"Expected an integer but you entered a {type(quantity)}")
        if price <= 0:
            raise ValueError(f"Expected a positive number, you enteres {price}.")
        if quantity <= 0:
            raise ValueError(f"Expected a positive number, you enteres {quantity}.")


        # if types and values are correct, assign them to attributes
        self.name = product_name
        self.price = price
        self.quantity = quantity
        self.active = active

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

        if quantity == 0:
            self.active = False
        else:
            self.active = True


    def is_active(self):
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        # Buys a given quantity of the product.

        # Returns the total price (float) of the purchase.
        total_price = self.price * quantity
        # Updates the quantity of the product.
        self.quantity -= quantity
        return quantity
        # Exception handling
