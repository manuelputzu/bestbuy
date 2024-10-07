class Store:
    """a list of products that exist in the store"""

    def __init__(self, product_list):
        # Create a list of products from a given list
        self.products  = product_list


    # Adds a product to store.
    def add_product(self, product):
        self.products.append(product)


    # Removes a product from store.
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)


    # Returns how many items are in the store in total.
    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity = total_quantity + product.get_quantity()
        return total_quantity


    # Returns all products in the store that are active.
    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    # Buys the products and returns the total price of the order.
    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            if product.get_quantity() >= quantity:
                 total_price += product.price * quantity
                 product.buy(quantity) # reduce the quantity
            else:
                raise ValueError(f"not enough stock for {product.name}")
        return total_price
