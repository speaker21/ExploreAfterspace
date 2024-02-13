from PyQt5.QtWidgets import QPushButton, QWidget
from PyQt5.QtCore import Qt

class PlanetButton(QPushButton):
    def __init__(self, game_state, planet) -> None:
        super().__init__(planet.name)
        self.clicked.connect(
            lambda: game_state.planet_info_frame.show_window(planet, game_state))
        self.setGeometry(20, 20, 20, 20)
