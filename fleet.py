from robot import Robots

class Fleet:
    def __init__(self):
        self.all_robots = []
        self.create_fleet()
        
    def create_fleet(self):
        robot_one = Robots('R2D2')
        self.all_robots.append(robot_one)
        
        robot_two = Robots("B46")
        self.all_robots.append(robot_two)
        
        robot_three = Robots("RR100")
        self.all_robots.append(robot_three)