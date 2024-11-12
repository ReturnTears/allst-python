global_var = 'a'
def my_func():
    local_var = 'b'
    print(global_var, local_var)

def greet(first_name, last_name):
    print(f"hello, {first_name} {last_name}")

def product(a, b, c):
    return a * b * c

def greed(name = "Guest"):
    print(f"hello, {name}")

def append_to(num, target=[]):
    target.append(num)
    return target

def append_to2(num, target=None):
    if target is None:
        target = []
    target.append(num)
    return target

def introduce(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}:{v}")

def minxed_args(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

def add(x, y, z):
    return x + y + z

def introduce(name, age):
    print(f"my name is {name} , and I`m {age} years old")
