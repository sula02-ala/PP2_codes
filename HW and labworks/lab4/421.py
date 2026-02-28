import importlib

def handle_query():
    module_name, attribute_name = input().split()
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        return "MODULE_NOT_FOUND"
    try:
        attribute = getattr(module, attribute_name)
        if callable(attribute):
            return "CALLABLE"
        else:
            return "VALUE"
    except AttributeError:
        return "ATTRIBUTE_NOT_FOUND"
n = int(input())
for i in range(n):
    print(handle_query())