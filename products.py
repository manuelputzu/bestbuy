class Product:
    def __init__(self, product_name: str, price: float, quantity: int, active: bool = True):

        if product_name == "":
            raise ValueError("Product name cannot be empty.")
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
        # Display basic product info
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Cannot buy more than available quantity.")
        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        return total_price


class NonStockedProduct(Product):
    def __init__(self, product_name: str, price: float):
        # For non-stocked products, quantity is always zero
        super().__init__(product_name, price, quantity=0)

    def set_quantity(self, quantity):
        # Don't allow changing quantity for non-stocked products
        raise ValueError("You can't set quantity for non-stocked products.")

    def buy(self, quantity):
        # No quantity check, just return the price for the licenses or digital goods
        return self.price * quantity

    def show(self):
        print(f"Non-Stocked Product: {self.name}, Price: {self.price}, Quantity: Not applicable")


class LimitedProduct(Product):
    def __init__(self, product_name: str, price: float, quantity: int, maximum: int):
        # Call the parent constructor
        super().__init__(product_name, price, quantity)
        self.maximum = maximum  # Set the maximum purchase limit

    def buy(self, quantity):
        # Check if the requested quantity exceeds the maximum allowed
        if quantity > self.maximum:
            raise ValueError(f"You can't buy more than {self.maximum} of this product.")
        return super().buy(quantity)  # Call the buy method from the parent class

    def show(self):
        print(f"Limited Product: {self.name}, Price: {self.price}, Max per order: {self.maximum}")