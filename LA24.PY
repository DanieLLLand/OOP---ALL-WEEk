
print("LA24")

from abc import ABC, abstractmethod

class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass
        
class Warrior(GameCharacter):
    def attack(self):
        print("Warrior: swing sword")
class Mage(GameCharacter):
    def attack(self):
        print("Mage: cast fireballs")
class Archer(GameCharacter):
    def attack(self):
        print("Archer: Shoots an arrow")
class Healer(GameCharacter):
    def attack(self):
        print("Healer: Cast healing spell on ally")
        
warrior = Warrior()
mage = Mage()
archer = Archer()
healer = Healer()

warrior.attack()
mage.attack()
archer.attack()
healer.attack()