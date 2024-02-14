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
        self.food = planet['food']

    def calculate_state(self):
        self.food_production_and_consumption()
        self.calculate_population()

    def calculate_population(self):
        if self.food<0:
            self.population+=self.food
            self.food=0
        elif self.food>0:
            self.population=self.population+round((self.population/100)*10)

    def use_resources(self):
        # TODO
        self.ore-=10
        self.gas-=20

    def food_production_and_consumption(self):
        self.food+=10000
        self.food = self.food - round(self.population*0.7)
