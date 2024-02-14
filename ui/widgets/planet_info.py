from PyQt5.QtWidgets import QWidget
from config import map_size
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from ui.widgets.planet_button import PlanetButton

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
        self.setLayout(self.content_layout)

    def create_content(self, planet, game_state):
        self.current_planet = planet
        if self.content:
            self.content.deleteLater()
        self.content = QWidget()
        layout = QVBoxLayout()
        self.content.setLayout(layout)
        self.name_label = QLabel(planet.name)
        self.population_label = QLabel(str(planet.population))
        layout.addWidget(self.name_label)
        layout.addWidget(self.population_label)
        self.content_layout.addWidget(self.content)
        
    
    def create_content(self, planet, game_state):
        self.current_planet = planet
        self.current_planet_population = planet.population
        if self.content:
            self.content.deleteLater()
        self.content = QWidget()
        layout = QVBoxLayout()
        self.content.setLayout(layout)
        self.name_label = QLabel(planet.name)
        self.population_label = QLabel(str(planet.population))

        layout.addWidget(self.name_label)
        layout.addWidget(self.population_label)
        self.content_layout.addWidget(self.content)

    def update_info(self):
        if self.isVisible():
            self.update_population()

    def update_population(self):
        if self.current_planet_population != self.current_planet.population:
            self.population_label.setText(str(self.current_planet.population))

    def show_window(self, star, game_state):
        self.create_content(star, game_state)
        self.show()
