from battlefield import Battlefield
from dinosaurs import Dinosaurs
from robot import Robots

first_battle = Battlefield()
# user input to start game
first_battle.run_game()
# printing a story line
first_battle.display_welcome()
# handling attacks, health, etc.
first_battle.battle()




# ## used for testing attack function for both robots and dinosaurs
# first_robot = Robots("R2D2")
# first_dino = Dinosaurs("rex", 25)
# first_robot.attack(first_dino)
