import products
from store import Store

product_list = [products.Product("MacBook Air M2", price=1450.0, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250.0, quantity=500),
                products.Product("Google Pixel 7", price=500.0, quantity=250),
               ]

store = Store(product_list)
products = store.get_all_products()
print(store.get_total_quantity())
print(store.order([(products[0], 1), (products[1], 2)]))