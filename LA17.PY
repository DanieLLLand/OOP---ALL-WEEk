print("LA17")

class Player:
    def __init__(self,name,health,attack_power):
        self.name =  name
        self.health = health
        self.attack_power = attack_power
    def attack(self, target):
        target.health -= self.attack_power
        print(f"{nana.name} reduce the target players health by {miya.health}% using her  {nana.attack_power}% attack power") 
        print(f"{miya.name} reduce the target players health by {nana.health}% using her  {miya.attack_power}% attack power")
        
nana = Player("nana", 10, 10)
miya = Player("miya", 200, 20)

while nana.health > 0 and miya.health > 0:
    nana.attack(miya)
    if nana.health <= 0:
       print(f"{miya.name} has been defeated")
       break
  
    miya.attack(nana)
    if nana.health <= 0:
       print(f"{nana.name}, has been defeated")
       break
