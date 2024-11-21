class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year, battery_szie):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery_szie = battery_szie
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_szie) + "-kwh battery.")

my_tesla = ElectricCar('tesla', 'red', 2019, 100)
print(my_tesla.make)
print(my_tesla.year)
print(my_tesla.battery_szie)
print(my_tesla.describe_battery())
