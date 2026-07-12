import calculate_total(
    add_product,
    update_quantity,
)

#assert
#assert 2=2=4
def test_add_product():
    inventory = {}
    add_product(inventory, "rice", 20, 1500)
    assert"rice
    product_name = "apple"
    price = 1.5
    quantity = 10

    updated_inventory = add_product(inventory, product_name, price, quantity)

    assert updated_inventory == {
        "apple": {"quantity": 10, "price": 1.5}
    }

    