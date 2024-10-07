import products  # Import modules
import store

# Setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450.0, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250.0, quantity=500),
    products.Product("Google Pixel 7", price=500.0, quantity=250)
]

best_buy = store.Store(product_list)


def start(store):
    while True:
        # Show menu
        print("\nMenu:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # List all products
            active_products = store.get_all_products()
            if active_products:
                print("\nProducts in store:")
                for product in active_products:
                    print(f"- {product.name}: Price: ${product.price}, Quantity: {product.get_quantity()}")
            else:
                print("No active products in store.")

        elif choice == '2':
            # Show total amount in store
            total_quantity = store.get_total_quantity()
            print(f"\nTotal quantity of products in store: {total_quantity}")

        elif choice == '3':
            # Make an order
            shopping_list = []
            while True:
                product_name = input("Enter the product name (or 'done' to finish): ")
                if product_name.lower() == 'done':
                    break
                quantity = int(input(f"Enter the quantity for {product_name}: "))

                # Find product by name
                found = False  # Flag to track if the product is found

                for p in product_list:
                    if p.name == product_name:
                        shopping_list.append((p, quantity))  # Append the product and quantity as a tuple
                        found = True  # Set the flag to True since the product was found
                        break  # Exit the loop once the product is found

                if not found:
                    print(f"Product '{product_name}' not found.")

            # Process the order
            if shopping_list:
                try:
                    total_price = store.order(shopping_list)
                    print(f"Total price of the order: ${total_price}")
                except ValueError as e:
                    print(e)

        elif choice == '4':
            print("Thank you for using the store interface. Goodbye!")
            break

        else:
            print("Invalid choice, please select a number between 1 and 4.")


# Start the store interface
if __name__ == "__main__":
    start(best_buy)
