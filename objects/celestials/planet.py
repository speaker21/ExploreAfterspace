from PyQt5.QtWidgets import QPushButton, QWidget
from PyQt5.QtCore import QCoreApplication, Qt

class Planet(QWidget):
    def __init__(self, planet):
        super().__init__()
        self.name = planet['name']
        if 'population' in planet:
            self.population = planet['population']
        else:
            self.population = None

    def calculate_population(self):
        if self.population:
            self.population+=10