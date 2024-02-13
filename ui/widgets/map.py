from PyQt5.QtWidgets import QWidget
from ui.stars.basic_star import Star
from logic.starmap_coordinates import make_star_coordinates
from config import map_size
from PyQt5.QtCore import Qt

class StarMap(QWidget):
    def __init__(self):
        super().__init__()
        self.name = 'map'
        star_coordinates_list = make_star_coordinates(600, 600, 20)
        for star_coordinate in star_coordinates_list:
            qbtn = Star(self)
            qbtn.move(*star_coordinate)
        self.setGeometry(*map_size)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: black')
        self.setMinimumSize(800, 600)