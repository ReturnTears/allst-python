def uppercase_decorator(func):
    def wrapper():
        orig_result = func()
        modified_result = orig_result.upper()
        return modified_result
    return wrapper

def split_decorator(func):
    def wrapper():
        orig_result = func()
        modified_result = orig_result.split()
        return modified_result
    return wrapper

@uppercase_decorator
@split_decorator
def greet():
    return "hello there"

print(greet())
