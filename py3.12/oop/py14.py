# Parent Class
class Vehicle:
    def __init__(self, wheels, type):
        self.wheels = wheels
        self.type = type

    def print_info(self):
        print(f"This is a {self.type} with {self.wheels} Wheels:")

class Car(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(4, "car")
        self.brand = brand
        self.model = model
        self.color = color
    def print_info(self):
        print(f"This is a {self.brand} {self.model} in {self.color}")

my_tesla = Car("Tesla", "Model 3", "Blue")
my_tesla.print_info()

