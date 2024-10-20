class Calculator:
    """Testing class"""
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


def call_function(obj, method_name, *args):
    method = getattr(obj, method_name, None)

    if callable(method):
        return method(*args)


obj = Calculator()
result_add = call_function(obj, "add", 7, 12)
print(result_add)
