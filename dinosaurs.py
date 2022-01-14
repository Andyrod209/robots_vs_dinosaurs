import random

class Dinosaurs:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.energy = 100
        
        
                    
        
   
    def attack(self, robot):

        self.abilities = ("Ram", "scratch", "bite", "tail whip", "head bump")
        self.attack_power_tuple = (25, 15, 26, 13, 17)
        # take 10 from energy
        self.energy -= 10
        self.attack_power = self.attack_power_tuple[random.randint(0, len(self.attack_power_tuple) - 1)]
        robot.health = robot.health - self.attack_power
        print(f'Robot {robot.name} was attacked by {self.name} with {self.abilities[random.randint(0, len(self.abilities) - 1)]} for {self.attack_power} damage')
        print('')
        print(f'Energy left {self.energy} for {self.name}')
        print('')
        print(f'Robot {robot.name} has {robot.health} health remaining')
        print('')
 
