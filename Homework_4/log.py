def log_methods(cls):
    """Decorator for logging class method calls."""
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, name):
            attr = getattr(self.wrapped, name)
            if callable(attr):
                def log_and_call(*args, **kwargs):
                    print(f"Logging: {name} called with {args} {kwargs}")
                    return attr(*args, **kwargs)
                return log_and_call
            return attr

    return Wrapper


@log_methods
class MyClass:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


obj = MyClass()
print(obj.add(5, 3))
print(obj.subtract(5, 3))
