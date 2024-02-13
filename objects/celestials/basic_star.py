from PyQt5.QtWidgets import QPushButton, QWidget
from PyQt5.QtCore import QCoreApplication, Qt

class Star(QWidget):
    def __init__(self, star):
        super().__init__()
        self.name = star['name']
        self.planets = star['planets']
        self.color = star['color']
        if 'population' in star:
            self.population = star['population']
        else:
            self.population = None
        self.coordinates = (star['coordinates']['x'], star['coordinates']['y'])

        
    def calculate_population(self):
        if self.population:
            self.population+=1