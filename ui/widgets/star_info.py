from PyQt5.QtWidgets import QWidget
from config import map_size
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from ui.widgets.planet_button import PlanetButton

class StarInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Star Information')
        self.setGeometry(*map_size)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: green')
        self.resize(400, 400)
        self.current_star = None
        self.content = None
        self.content_layout = QVBoxLayout()
        self.setLayout(self.content_layout)

    def create_content(self, star, game_state):
        self.current_star = star
        if self.content:
            self.content.deleteLater()
        self.content = QWidget()
        layout = QVBoxLayout()
        self.content.setLayout(layout)
        self.name_label = QLabel(star.name)
        self.population_label = QLabel(str(star.population))
        for planet in star.planets:
            planet_button = PlanetButton(game_state, planet)
            layout.addWidget(planet_button)

        layout.addWidget(self.name_label)
        layout.addWidget(self.population_label)
        self.content_layout.addWidget(self.content)
        
    
    def update_info(self, game_state):
        if self.current_star:
            self.create_content(self.current_star, game_state)

    def show_window(self, star, game_state):
        self.create_content(star, game_state)
        self.show()

    