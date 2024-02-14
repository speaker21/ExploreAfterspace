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

    def create_content(self, planet, game_state):
        self.current_planet = planet
        self.current_planet_population = planet.population
        self.current_planet_ore = planet.ore
        self.current_planet_gas = planet.gas
        if self.content:
            self.content.deleteLater()
        self.content = QWidget()
        layout = QVBoxLayout()
        self.content.setLayout(layout)
        self.name_label = InformationLabel('Название', planet.name)
        self.population_label = InformationLabel('Население', planet.population)
        self.ore_label = InformationLabel('Руда', planet.ore)
        self.gas_label = InformationLabel('Газ', planet.gas)
        layout.addWidget(self.name_label)
        layout.addWidget(self.population_label)
        layout.addWidget(self.ore_label)
        layout.addWidget(self.gas_label)
        layout.addStretch(1)
        self.content_layout.addWidget(self.content)

    def update_info(self):
        if self.isVisible():
            self.update_population()
            self.update_ore()
            self.update_gas()

    def update_population(self):
        if self.current_planet_population != self.current_planet.population:
            self.current_planet_population = self.current_planet.population
            self.population_label.value.setText(str(self.current_planet.population))
    
    def update_ore(self):
        if self.current_planet_ore != self.current_planet.ore:
            self.current_planet_ore = self.current_planet.ore
            self.ore_label.value.setText(str(self.current_planet.ore))

    def update_gas(self):
        if self.current_planet_gas != self.current_planet.gas:
            self.current_planet_gas = self.current_planet.gas
            self.gas_label.value.setText(str(self.current_planet.gas))

    def show_window(self, star, game_state):
        self.create_content(star, game_state)
        self.show()
