from PyQt5.QtWidgets import QWidget
from config import map_size
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from ui.widgets.planet_button import PlanetButton
from ui.widgets.planet_info.information_label import InformationLabel

class PlanetInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Planet Information')
        self.setGeometry(*map_size)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: green')
        self.resize(400, 400)
        self.current_planet = None
        self.content = None
        self.content_layout = QVBoxLayout()
        self.current_planet_population = None
        self.setLayout(self.content_layout)

    def create_content(self, planet):
        self.current_planet = planet
        if self.content:
            self.content.deleteLater()
        self.content = QWidget()
        layout = QVBoxLayout()
        self.content.setLayout(layout)

        self.name_label = InformationLabel('Название', planet.name)
        self.population_label = InformationLabel('Население', planet.population)
        self.ore_label = InformationLabel('Руда', planet.ore)
        self.gas_label = InformationLabel('Газ', planet.gas)
        self.food_label = InformationLabel('Пища', planet.food)
        if planet.production_building:
            self.current_planet_building_production = planet.production_building
            self.building_food_production_label = InformationLabel('Производство пищи', str(planet.production_building.size))

        build_button = QPushButton('build')
        build_button.clicked.connect(lambda:planet.production_building.build_new(self))

        layout.addWidget(self.name_label)
        layout.addWidget(self.population_label)
        layout.addWidget(self.ore_label)
        layout.addWidget(self.gas_label)
        layout.addWidget(self.food_label)
        if self.current_planet_building_production:
            layout.addWidget(self.building_food_production_label)
        layout.addWidget(build_button)
        
        layout.addStretch(1)
        self.content_layout.addWidget(self.content)

    def update_info(self):
        if self.isVisible():
            self.update_population()
            self.update_ore()
            self.update_gas()
            self.update_food()
            self.update_build_production()

    def update_population(self):
        if  self.population_label.value.text() != self.current_planet.population:
            self.population_label.value.setText(str(self.current_planet.population))
    
    def update_ore(self):
        if self.ore_label.value.text() != self.current_planet.ore:
            self.ore_label.value.setText(str(self.current_planet.ore))

    def update_gas(self):
        if self.gas_label.value.text() != self.current_planet.gas:
            self.gas_label.value.setText(str(self.current_planet.gas))

    def update_food(self):
        if self.food_label.value.text() != self.current_planet.food:
            self.food_label.value.setText(str(self.current_planet.food))

    def update_build_production(self):
        if self.building_food_production_label.value.text()!=self.current_planet.production_building.size:
            self.building_food_production_label.value.setText(str(self.current_planet.production_building.size))
            

    def show_window(self, star):
        self.create_content(star)
        self.show()
