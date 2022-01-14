from robot import Robots

class Fleet:
    def __init__(self):
        self.all_robots = []
        self.create_fleet()
        
    def create_fleet(self):
        
        self.all_robots.append(Robots('R2D2'))
        
        self.all_robots.append(Robots("B46"))
        
        self.all_robots.append(Robots("RR100"))