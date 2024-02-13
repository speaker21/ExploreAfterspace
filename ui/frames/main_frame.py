from PyQt5.QtWidgets import QWidget, QVBoxLayout
from config import map_size
from PyQt5.QtCore import Qt
from ui.widgets.header import Header
from ui.widgets.map import StarMap
from ui.widgets.map2 import StarMap2

class MainFrame(QWidget):
    def __init__(self, game_state):
        super().__init__()

        self.initUI(game_state)


    def initUI(self, game_state):
        self.resize(600, 600)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.header = Header(game_state)
        self.star_map = StarMap()
        self.other_frame = StarMap2()
        frames = (self.star_map, self.other_frame)

        layout.addWidget(self.header)
        for frame in frames:
            game_state.frames.append(frame)
            layout.addWidget(frame)
            frame.hide()
        
        self.setWindowTitle('ExploreAfterspace Диман здарова')
        self.setAttribute(Qt.WA_StyledBackground, True)
        # self.setStyleSheet('background-color: black')
        layout.addStretch(1)
        self.show()