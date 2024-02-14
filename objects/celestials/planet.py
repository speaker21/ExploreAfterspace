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
        self.ore = planet['ore']
        self.gas = planet['gas']

    def calculate_population(self):
        # TODO
        if self.population:
            self.population+=10

    def use_resources(self):
        # TODO
        self.ore-=10
        self.gas-=20