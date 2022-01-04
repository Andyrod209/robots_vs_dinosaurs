import random
from fleet import Fleet
from herd import Herd

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
        first_turn = random.randint(1, 2)
        if first_turn == 1:
            print("Robots attack first")
            


    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass 

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass