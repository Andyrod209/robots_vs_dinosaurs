from weapons import Weapon

class Robots:
    def __init__(self, name):
        self.name = name
        self.health = 100
        print(self.name, self.health) 
        self.weapon = Weapon("flaming sword", 25)
        
    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power
        print(f'Dinosaur {dinosaur.name} was attacked by {self.name} with {self.weapon.name} for {self.weapon.attack_power} damage')
        print(f'Dinosaur {dinosaur.name} has {dinosaur.health} health remaining')

    

    