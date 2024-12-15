print("LA7,")

class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car = car("Honda" , "white")
print(f"{car.brand}, {car.color}")
car.brand = "ford"
car.color = "black"
print(f"{car.brand}, {car.color}")
