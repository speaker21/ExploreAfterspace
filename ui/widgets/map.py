from PyQt5.QtWidgets import QWidget
from ui.stars.basic_star import Star
from logic.starmap_coordinates import make_star_coordinates
from config import map_size
from PyQt5.QtCore import Qt
import json

class StarMap(QWidget):
    def __init__(self, game_state):
        super().__init__()
        self.name = 'map'
        with open('data/stars.json', 'r', encoding='utf-8') as stars_json:
            star_list = json.load(stars_json)
        for star in star_list:
            star_sprite = Star(self, star, game_state)
            star_sprite.move(star['coordinates']['x'], star['coordinates']['y'])
            game_state.stars_list.append(star_sprite)
        self.setGeometry(*map_size)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: black')
        self.setMinimumSize(800, 600)