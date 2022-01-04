from dinosaurs import Dinosaurs

class Herd:
    def __init__(self):
        self.all_dinosaurs = []
        
    def create_herd(self):
        first_dino = Dinosaurs('T Rex', 15)
        self.all_dinosaurs.append(first_dino)
        second_dino = Dinosaurs('Gaint Lizard', 20)
        self.all_dinosaurs.append(second_dino)
        third_dino = Dinosaurs('Velocirator', 20)
        self.all_dinosaurs.append(third_dino)
