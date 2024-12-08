def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print("wrapper executed this before {}".format(original_func.__name__))
        return original_func(*args, **kwargs)
    return wrapper_func

@decorator_func
def func_to_be_decorated():
    print("This is the function to be decorated")
