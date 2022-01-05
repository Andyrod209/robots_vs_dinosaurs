from dinosaurs import Dinosaurs

class Herd:
    def __init__(self):
        self.all_dinosaurs = []
        self.create_herd()
        
    def create_herd(self):
        first_dino = Dinosaurs('T Rex')
        self.all_dinosaurs.append(first_dino)

        second_dino = Dinosaurs('Gaint Lizard')
        self.all_dinosaurs.append(second_dino)

        third_dino = Dinosaurs('Velocirator')
        self.all_dinosaurs.append(third_dino)
