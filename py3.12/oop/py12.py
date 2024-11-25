class Car:
    def __init__(self,brand,model,color):
        self.brand=brand
        self.model=model
        self.color=color
        self.__engine_status = False
    def start(self):
        print(f"{self.brand} {self.model} started")
    def stop(self):
        print(f"{self.brand} {self.model} stopped")
    def turn(self,direction):
        print(f"{self.brand} {self.model} turned {direction}")
    def speed(self,speed):
        print(f"{self.brand} {self.model} speed is {speed}")
    
    @property
    def engine_status(self):
        return self.__engine_status
    @engine_status.setter
    def engine_status(self, status):
        self.__engine_status = status
    
    @classmethod
    def from_string(cls, car_string):
        brand, model, color = car_string.split(",")
        return cls(brand, model, color)
    @staticmethod
    def is_motor(type):
        return type.lower() in ['electric', 'hybrid']


my_tesla = Car("Tesla","Model S","Black")
my_tesla.start()
print(my_tesla.brand)
my_tesla.year = 2023
print(my_tesla.year)
# print(my_tesla.__engine_status)

car_string = "Audi,RS7,Black"
my_new_car = Car.from_string(car_string)
print(my_new_car.brand)

