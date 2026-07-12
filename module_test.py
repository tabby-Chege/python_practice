def add_product(inventory, product_name, quantity, price):
    inventory[product_name] = {
        "quantity": quantity,
        "price": price
    }
    return inventory
def display_inventory(inventory):
    for product_name, details in inventory.items():
        print(f"product_name: {product_name}")
        print(f"Quantity: {details['quantity']}")
        print(f"Price: {details['price']}")