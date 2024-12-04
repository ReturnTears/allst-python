class Adder:
    def __init__(self, x):
        self.x = x
    def __call__(self, y):
        return self.x + y

add_five = Adder(5)
print(add_five(6))

print(callable(add_five))
