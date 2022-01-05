from weapon import Weapon
import random

class Robots:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.random_number = random.randint(1, 3)
        
        if self.random_number == 1:
            self.weapons_to_select_from = ["flaming sword", 25]
            self.weapons = Weapon(self.weapons_to_select_from[0],self.weapons_to_select_from[1])
        
        elif self.random_number == 2:
            self.weapons_to_select_from = ["machine gun", 15]
            self.weapons = Weapon(self.weapons_to_select_from[0],self.weapons_to_select_from[1])
        
        elif self.random_number == 3:
            self.weapons_to_select_from = ["missiles", 21]
            self.weapons = Weapon(self.weapons_to_select_from[0],self.weapons_to_select_from[1])

        
    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapons.attack_power
        print(f'Dinosaur {dinosaur.name} was attacked by {self.name} with {self.weapons.name} for {self.weapons.attack_power} damage')
        print(f'Dinosaur {dinosaur.name} has {dinosaur.health} health remaining')

        
        
                



    