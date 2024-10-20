def create_class(class_name, methods):
    return type(class_name, (object,), methods)


def say_hello(self):
    return "Hello!"


def say_goodbye(self):
    return "Goodbye!"


methods = {
    'say_hello': say_hello,
    'say_goodbye': say_goodbye
}
MyClass = create_class("MyClass", methods)
obj = MyClass()
print(obj.say_hello())
print(obj.say_goodbye())
