print("LA 12")

class Toy():
    def __init__(self, name, prize):
        self.name = name
        self.prize = prize
    def describeToy(self):
        print(f"toy: {self.name}, prize: {self.prize} ")
class car(Toy):
    def __init__(self, name, prize):
             super().__init__(name, prize)
      
pokemon = Toy("pokemons", "$10,000")
pokemon.describeToy()
