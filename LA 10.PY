class Vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    def describeVehicle(self):
        print(f"{self.brand}, {self.model}, and using {self.fuel_type} ")
class car(Vehicle):
    pass
class motorcycle(Vehicle):
    pass

ford = Vehicle("ford", "f-150", "diesel")
ford.describeVehicle()

kawasaki = Vehicle("wasaki", "125", "unleaded")
kawasaki.describeVehicle()
