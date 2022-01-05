import random
from fleet import Fleet
from herd import Herd
from dinosaurs import Dinosaurs
from robot import Robots

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        no_start = True
        while no_start is True:
            user_start = input("press 1 to start game ")
            if user_start == "1":
                self.welcome = False
                no_start = False
            else:
                print("")

    def display_welcome(self):
        self.welcome = True
        print('''In a cruel world called earth are vicious creatures called Dinosaurs!!! 
        Robots were sent to wipe these creatures out and create a new living species called humans...
        But of course they have deal with these tough creatures... ''')

    def battle(self):
        print("Battle begins")
        while len(self.herd.all_dinosaurs) > 0 and len(self.fleet.all_robots) > 0:
        # random number to select who goes first
            self.first_turn = random.randint(1, 2)
            if self.first_turn == 1:
                self.robo_turn()
                self.dino_turn()
        
            elif self.first_turn == 2:
                self.dino_turn()
                self.robo_turn()
            
            if self.herd.all_dinosaurs[self.random_dino_index].health == 0:
                print(f"{self.herd.all_dinosaurs[self.random_dino_index].name} is out of health.")
                self.herd.all_dinosaurs.remove(self.herd.all_dinosaurs[self.random_dino_index])
            if len(self.herd.all_dinosaurs) == 0:
                print("The Dinosurs have fallen and New life will be created!")

                
            
        


    def dino_turn(self):
        print("Dinosaurs attack first")
        # selecting a Dinosaur with the random number
        random_robo_index = random.randint(0, (len(self.fleet.all_robots) - 1))
        self.random_dino_index = random.randint(0, (len(self.herd.all_dinosaurs) - 1))
        self.herd.all_dinosaurs[self.random_dino_index].attack(self.fleet.all_robots[random_robo_index])
       

    def robo_turn(self):
        print("Robots attack first")
        # selecting a robot with the random number
        random_robo_index = random.randint(0, (len(self.fleet.all_robots) - 1))
        self.random_dino_index = random.randint(0, (len(self.herd.all_dinosaurs) - 1))
        self.fleet.all_robots[random_robo_index].attack(self.herd.all_dinosaurs[self.random_dino_index])
        

    def show_dino_opponent_options(self):
        pass 

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass