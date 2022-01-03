from robot import Robots

class RobotFleet:
    def __init__(self):
        self.all_robots = []

    def create_fleet(self):
        robot_one = Robots('R2D2')
        self.all_robots.append(robot_one)
        robot_two = Robots("B46")
        self.all_robots.append(robot_two)
        robot_three = Robots("RR100")
        self.all_robots.append(robot_three)