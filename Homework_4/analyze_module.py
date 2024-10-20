def analyze_module(module_name):
    module = __import__(module_name)
    print(f"Module: {module_name}")
    for name_item in dir(module):
        item = getattr(module, name_item)
        if isinstance(item, type):
            print(f"\n Class: {name_item}")
            for method_name in dir(item):
                method = getattr(item, method_name)
                if callable(method):
                    print(f"Method: {method_name}")
        elif callable(item):
            print(f"Function: {name_item}")


module_name = input("Введіть назву модуля: ")
analyze_module(module_name)
