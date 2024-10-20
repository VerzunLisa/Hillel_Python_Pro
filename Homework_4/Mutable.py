class MutableClass:
    def add_attribute(self, name, value):
        """Adds a new attribute with a name and value."""
        setattr(self, name, value)

    def remove_attribute(self, name):
        """Deletes an attribute with a name"""
        if hasattr(self, name):
            delattr(self, name)
        else:
            print(f"Атрибут '{name}' не знайдено.")


obj = MutableClass()
obj.add_attribute("name", "Python")
print(obj.name)
obj.remove_attribute("name")
