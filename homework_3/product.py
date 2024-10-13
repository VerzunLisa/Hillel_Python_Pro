class ProductWithGetSet:
    def __init__(self, name, price):
        """Initialization name and price"""
        self.name = name
        self.set_price(price)

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price < 0:
            raise ValueError("Ціна не може бути від'ємною")
        self._price = price


class ProductWithProperty:
    def __init__(self, name, price):
        """Initialization name and price"""
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Ціна не може бути від'ємною")
        self._price = value


class PriceDescriptor:
    def __init__(self):
        """Initialization price"""
        self._price = None

    def __get__(self, instance, owner):
        return self._price

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Ціна не може бути від'ємною")
        self._price = value


class ProductWithDescriptor:
    price = PriceDescriptor()

    def __init__(self, name, price):
        self.name = name
        self.price = price


def test_product_class():
    print("Тестування ProductWithGetSet:")
    product_1 = ProductWithGetSet("Phone", 800)
    print(f"Ціна: {product_1.get_price()}")
    product_1.set_price(900)
    print(f"New Ціна: {product_1.get_price()}")
    print("\nТестування ProductWithProperty:")
    product_2 = ProductWithProperty("Laptop", 2500)
    print(f"Ціна: {product_2.price}")
    product_2.price = 2200
    print(f"New Ціна: {product_2.price}")
    print("\nТестування ProductWithDescriptor:")
    product_3 = ProductWithDescriptor("TV", 1600)
    print(f"Ціна: {product_3.price}")
    product_3.price = 1350
    print(f"New Ціна: {product_3.price}")


test_product_class()
