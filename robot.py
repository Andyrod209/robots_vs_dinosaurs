from weapons import Weapon

class Robots:
    def __init__(self, name):
        self.name = name
        self.health = 100
        print(self.name, self.health) 
        self.weapon = Weapon("flaming sword", 25)
        
    def attack(self, dinosaur):
        dinosaur = dinosaur.health - self.weapon.attack_power
        print(dinosaur,"Health left for", dinosaur.name)
        

    

    