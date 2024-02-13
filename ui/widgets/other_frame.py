from PyQt5.QtWidgets import QWidget
from ui.stars.basic_star import Star
from logic.starmap_coordinates import make_star_coordinates
from config import map_size
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel

class OtherFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.name = 'other_frame'
        
        self.setGeometry(*map_size)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: green')
        self.setMinimumSize(800, 600)

        self.name_label = QLabel('name')
        self.planets_label = QLabel('planets')

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.name_label)
        layout.addWidget(self.planets_label)
        layout.addStretch(1)