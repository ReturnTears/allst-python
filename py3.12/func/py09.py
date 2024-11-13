# First-Class and High-Order Functions
def greet(name):
    return f"Hello {name}"

def salute(greet_func, name):
    return greet_func(name)

print(salute(greet, "John"))
