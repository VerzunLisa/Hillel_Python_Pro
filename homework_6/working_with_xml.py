import xml.etree.ElementTree as ET


def display_products(filename="products.xml"):
    """A function for loading and outputting product data"""
    tree = ET.parse(filename)
    root = tree.getroot()

    print("Список продуктів:")
    for product in root.findall("product"):
        name = product.find("name").text
        quantity = product.find("quantity").text
        print(f"{name} - Кількість на складі: {quantity}")


def update_quantity(product_name, new_quantity, filename="products.xml"):
    """Function for changing the quantity of the product"""
    tree = ET.parse(filename)
    root = tree.getroot()

    for product in root.findall("product"):
        name = product.find("name").text
        if name == product_name:
            product.find("quantity").text = str(new_quantity)
            print(f"Оновлено кількість для {product_name}: {new_quantity}")
            break
    else:
        print(f"Продукт '{product_name}' не знайдено.")

    tree.write(filename, encoding="utf-8", xml_declaration=True)


display_products()

update_quantity("Молоко", 45)  # Зміна кількості молока на 45

display_products()
