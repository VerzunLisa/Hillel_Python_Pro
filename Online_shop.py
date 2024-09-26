def create_product(name):
    def set_price(price):
        def set_quantity(quantity):
            product = {
                'name': name,
                'price': price,
                'quantity': quantity
            }

            def update_price(new_price):
                product['price'] = new_price
                return f"Ціна товару '{product['name']}' змінена на {product['price']}"

            return product, update_price

        return set_quantity

    return set_price


product_creator = create_product('Смартфон')
product_with_price = product_creator(9500)
product, change_price = product_with_price(50)  # Товар із назвою, ціною та кількістю
print(product)
print(change_price(8000))
print(product)
