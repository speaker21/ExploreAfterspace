from PyQt5.QtWidgets import QWidget
from config import map_size
from PyQt5.QtCore import Qt
from ui.celestials.star_sprite import StarSprite

class StarMap(QWidget):
    def __init__(self, game_state):
        super().__init__()
        self.name = 'map'
        for star in game_state.stars_list:
            star_sprite = StarSprite(self, game_state, star)
            star_sprite.move(*star.coordinates)
        self.setGeometry(*map_size)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: black')
        self.setMinimumSize(800, 600)