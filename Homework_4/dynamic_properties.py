class DynamicProperties:
    def __init__(self):
        self._properties = {}

    def add_property(self, property_name, default_value):
        self._properties[property_name] = default_value

        def getter(self):
            return self._properties[property_name]

        def setter(self, value):
            self._properties[property_name] = value

        setattr(DynamicProperties, property_name, property(getter, setter))


obj = DynamicProperties()
obj.add_property('name', 'default_name')
print(obj.name)
obj.name = "Python"
print(obj.name)
