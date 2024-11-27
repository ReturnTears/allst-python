class Vehicle:
    def travel_distance(self, miles):
        print(f"The vehicle has traveled {miles} miles")
    def start_engine(self):
        print("The engine starts up with a roar .")

class Car(Vehicle):
    def travel_distance(self, miles):
        super().travel_distance(miles)
        print(f"The Car has traveled {miles} miles to its odometer")
    def start_engine(self):
        super().start_engine()
        print("The Car starts with a click .")
    

my_car = Car()
my_car.travel_distance(100)
my_car.start_engine()
