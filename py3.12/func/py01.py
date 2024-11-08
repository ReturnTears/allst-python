def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def greet(name, message):
    print(f"Hello, {name}! {message}")

def log(message, *details):
    print(f'Log: {message}')
    for detail in details:
        print(detail)


def combine(*args, glue='-'):
    return glue.join(args)