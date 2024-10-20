class MyClass:
    """Testing class"""
    def __init__(self, value):
        self.value = value

    def say_hello(self):
        return f"Hello, {self.value}"


def analyze_object(x):
    """Analysis of the object"""
    print(f"Тип об'єкта: {type(x)}")
    attributes_and_methods = dir(x)
    print("\n Список атрибутів і методів:")
    for at in attributes_and_methods:
        print(at)
    print("\nТип кожного атрибуту або методу:")
    for at in attributes_and_methods:
        at_type = type(getattr(x, at))
        print(f"{at}: {at_type}")


obj = MyClass("World")
analyze_object(obj)
