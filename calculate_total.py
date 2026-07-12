#pytest: write the testand running them
#tests functions
def calculate_total(inventory, product_name, price, quantity):
    product_name = input("Enter the product name:")
    product_name = product_name.strip().lower()

    inventory[product_name] = {
        "quantity": quantity,
        "price": price
    }
    return inventory
def update_inventory(inventory, product_name, quantity):
    product_name = product_name.strip().lower()
    if product_name in inventory:
        inventory[product_name]["quantity"] += quantity
        return True
    return False