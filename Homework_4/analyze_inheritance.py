def analyze_inheritance(cls):
    """The function analyzes class inheritance and outputs base class methods."""
    inherited_methods = set()

    for base in cls.__bases__:
        base_methods = set(dir(base))
        inherited_methods.update(base_methods)

    print(f"Успадковані методи класу {cls.__name__}:")
    for method in sorted(inherited_methods):
        if not method.startswith("__"):
            print(method)


class Parent:
    def parent_method(self):
        pass


class Child(Parent):
    def child_method(self):
        pass


analyze_inheritance(Child)
