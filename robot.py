from weapon import Weapon
import random

class Robots:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power_level = 100
        
    def weapon_of_choice(self):
        none_selected = True
        while none_selected is True:
            self.weapons = input('''
Select for
1 'flaming sword' for 25 damage 
2 'machine gun' for 15 damage
3 'missiles' for 21 damage
selected: ''')
        
            if self.weapons == '1':
            
                self.weapons = Weapon("flaming sword", 25)
                none_selected = False
        
            elif self.weapons == '2':
            
                self.weapons = Weapon("machine gun", 15)
                none_selected = False
        
            elif self.weapons == '3':
            
                self.weapons = Weapon("missiles", 21)
                none_selected = False

            else:
                print('INVALID CHOICE!')
        print('')
        
    def attack(self, dinosaur):
        self.weapon_of_choice()
        dinosaur.health = dinosaur.health - self.weapons.attack_power
        # take 10 from power_level
        self.power_level -= 10
        print(f'Dinosaur {dinosaur.name} was attacked by {self.name} with {self.weapons.name} for {self.weapons.attack_power} damage')
        print(f'Power left {self.power_level} for {self.name}')
        print(f'Dinosaur {dinosaur.name} has {dinosaur.health} health remaining')

        
        
                



    