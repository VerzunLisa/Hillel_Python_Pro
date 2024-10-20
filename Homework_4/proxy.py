class Proxy:
    def __init__(self, obj):
        """Initializes the Proxy"""
        self._obj = obj

    def __getattr__(self, name):
        """
        Called when the attribute is not found in the Proxy class.
        Logs methods and arguments and then redirects calls.
        """
        attr = getattr(self._obj, name)

        if callable(attr):
            def log_and_call(*args, **kwargs):
                print(f"Викликано метод: {name}, з аргументами: {args}, {kwargs}")
                return attr(*args, **kwargs)
            return log_and_call
        return attr


class MyClass:
    def greet(self, name):
        return f"Hello, {name}!"


obj = MyClass()
proxy = Proxy(obj)
print(proxy.greet("Alice"))
