class LimitedAttributesMeta(type):
    MAX_ATTRIBUTES = 3

    def __new__(cls, name, bases, class_dict):
        attributes = {k: v for k, v in class_dict.items() if not k.startswith('__')}

        if len(attributes) > cls.MAX_ATTRIBUTES:
            raise AttributeError(f"Клас {name} може мати лише {cls.MAX_ATTRIBUTES} атрибути!")

        return super().__new__(cls, name, bases, class_dict)


class LimitedClass(metaclass=LimitedAttributesMeta):
    attr1 = 1
    attr2 = 2
    attr3 = 3

    
try:
    obj = LimitedClass()
    print("Клас створено успішно!")
except AttributeError as e:
    print(e)
