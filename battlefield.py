import random
from fleet import Fleet
from herd import Herd
from weapon import Weapon


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
        print('')
        print('''In a cruel world called earth are vicious creatures called Dinosaurs!!! 
        Robots were sent to wipe these creatures out and create a new living species called humans...
        But of course they have deal with these tough creatures... ''')
        print('')

    def battle(self):
        print("Battle begins")
        print('')
        while len(self.herd.all_dinosaurs) > 0 and len(self.fleet.all_robots) > 0:
        # random number to select who goes first
            self.first_turn = random.randint(1, 2)
            if self.first_turn == 1:
                self.robo_turn()
                print('')
                
        
            elif self.first_turn == 2:
                self.dino_turn()
                print('')
                
            
            # removing any dinosaurs that have had their health fall to 0
            if self.herd.all_dinosaurs[self.random_dino_index].health <= 0:
                print(f"{self.herd.all_dinosaurs[self.random_dino_index].name} is out of health.")
                print('')
                self.herd.all_dinosaurs.remove(self.herd.all_dinosaurs[self.random_dino_index])
            # removing any robot that has had their health fall to 0
            if self.fleet.all_robots[self.random_robo_index].health <= 0:
                print(f"{self.fleet.all_robots[self.random_robo_index].name} is out of health.")
                print('')
                self.fleet.all_robots.remove(self.fleet.all_robots[self.random_robo_index])

            self.display_winners()
                
            
        


    def dino_turn(self):
        print("Dinosaurs attack")
        # selecting a Dinosaur with the random number
        self.random_robo_index = random.randint(0, (len(self.fleet.all_robots) - 1))
        self.random_dino_index = random.randint(0, (len(self.herd.all_dinosaurs) - 1))
        self.herd.all_dinosaurs[self.random_dino_index].attack(self.fleet.all_robots[self.random_robo_index])
        self.check_game()
       

    def robo_turn(self):
        print("Robots attack")
        # selecting a robot with the random number
        self.random_robo_index = random.randint(0, (len(self.fleet.all_robots) - 1))
        self.random_dino_index = random.randint(0, (len(self.herd.all_dinosaurs) - 1))
        
        self.fleet.all_robots[self.random_robo_index].attack(self.herd.all_dinosaurs[self.random_dino_index])
        self.check_game()
        
    # checking what happened for user to pick his next move
    def check_game(self):
        not_true = True
        while not_true is True:
            self.user = input('Push 1 to continue: ')
            if self.user == '1':
                not_true = False
                print('')
            else:
                print('INVALID CHOICE!')

            
    def display_winners(self):
        if len(self.fleet.all_robots) == 0:
            print('Robots have failed their mission and will have to resort to dropping meteors.')
        # displaying dinosaurs lost
        if len(self.herd.all_dinosaurs) == 0:
            print("The Dinosaurs have fallen and New life will be created!")
        pass