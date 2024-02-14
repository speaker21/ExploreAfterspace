from PyQt5.QtWidgets import QWidget
from objects.celestials.planet import Planet

class Star(QWidget):
    def __init__(self, star):
        super().__init__()
        self.name = star['name']
        self.planets = []
        for planet in star['planets']:
            planet_object = Planet(planet)
            self.planets.append(planet_object)
        self.color = star['color']
        self.coordinates = (star['coordinates']['x'], star['coordinates']['y'])
        
        self.population = 0
        self.ore = 0
        self.gas = 0

        self.calculate_population()
        self.calculate_ore()
        self.calculate_gas()

    def calculate_population(self):
        self.population=0
        for planet in self.planets:
            self.population+=planet.population

    def update_data(self):
        self.calculate_ore()
        self.calculate_gas()
        self.calculate_population()

    def calculate_ore(self):
        self.ore=0
        for planet in self.planets:
            self.ore+=planet.ore

    def calculate_gas(self):
        self.gas=0
        for planet in self.planets:
            self.gas+=planet.gas