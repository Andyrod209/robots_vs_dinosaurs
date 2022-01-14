from dinosaurs import Dinosaurs

class Herd:
    def __init__(self):
        self.all_dinosaurs = []
        self.create_herd()
        
    def create_herd(self):
        self.all_dinosaurs.append(Dinosaurs('T Rex'))
        
        self.all_dinosaurs.append(Dinosaurs('Gaint Lizard'))

        self.all_dinosaurs.append(Dinosaurs('Velocirator'))
        
