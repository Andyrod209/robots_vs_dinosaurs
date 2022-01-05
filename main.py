from battlefield import Battlefield
from dinosaurs import Dinosaurs
from robot import Robots
from herd import Herd
from fleet import Fleet

first_battle = Battlefield()
# user input to start game
first_battle.run_game()
# printing a story line
first_battle.display_welcome()
# handling attacks, health, etc.
first_battle.battle()




# ### used for testing attack function for both robots and dinosaurs
# first_robot = Robots("R2D2")
# first_dino = Dinosaurs("rex", 25)
# first_robot.attack(first_dino)


# ### calling on both list from herd and fleet
# robot_fleet = Fleet()
# robot_fleet.create_fleet()
# print(robot_fleet.all_robots)
# dino_herd = Herd()
# dino_herd.create_herd()
# print(dino_herd.all_dinosaurs)
