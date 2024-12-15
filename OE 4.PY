#OE 4

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        damage = self.power
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage! {target.name} has {target.health} health remaining.")

    def special_move(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def defend(self, attacker):
        reduced_damage = attacker.power // 2
        self.health -= reduced_damage
        print(f"{self.name} defends against {attacker.name}! Takes {reduced_damage} damage. {self.name} has {self.health} health remaining.")

class Warrior(Character):
    def special_move(self):
        print(f"{self.name} uses Shield Bash! Warrior's power doubles for the next attack.")
        self.power *= 2

class Mage(Character):
    def special_move(self, target):
        print(f"{self.name} casts Fireball! {target.name} takes 120 damage.")
        target.health -= 120
        print(f"{target.name} has {target.health} health remaining.")

class Archer(Character):
    def special_move(self):
        print(f"{self.name} shoots a Piercing Arrow! It ignores defenses.")

    def attack(self, target):
        damage = self.power
        target.health -= damage
        print(f"{self.name}'s Piercing Arrow hits {target.name} for {damage} damage! {target.name} has {target.health} health remaining.")

class Monster(Character):
    def special_move(self):
        print(f"{self.name} roars and gains extra health! Increases health by 60.")
        self.health += 60
        print(f"{self.name} now has {self.health} health.")

warrior = Warrior("Warrior", 220, 25)
mage = Mage("Mage", 160, 18)
archer = Archer("Archer", 200, 30)
monster = Monster("Monster", 350, 35)

print("\n=== Battle Begins ===\n")

warrior.attack(monster)
warrior.special_move()

mage.attack(monster)
mage.special_move(monster)

archer.attack(monster)
archer.special_move()

monster.attack(warrior)
monster.special_move()

monster.attack(mage)
monster.special_move()

monster.attack(archer)
monster.special_move()

print("\n=== Polymorphism Demonstration ===\n")
characters = [warrior, mage, archer, monster]
for character in characters:
    character.special_move()

print("\n=== Battle Ends ===")
