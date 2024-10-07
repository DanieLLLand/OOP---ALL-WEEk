print("LA9")

class car:
    def __init__(self, brand):
        self.brand = brand 
    def __str__(self, brand):
        self.brand = brand 
        return f"{self.brand}"
my_car = car("toyota")
print(my_car.brand)
del my_car
print(my_car)