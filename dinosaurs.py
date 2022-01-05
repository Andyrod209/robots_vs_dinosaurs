from robot import Robots

class Dinosaurs:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
        
    
    def attack(self, robot):
        robot.health = robot.health - self.attack_power
        print(f'Robot {robot.name} was attacked by {self.name} for {self.attack_power} damage')
        print(f'Robot {robot.name} has {robot.health} health remaining')