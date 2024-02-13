from PyQt5.QtWidgets import QPushButton, QWidget
from PyQt5.QtCore import Qt

class StarSprite(QPushButton):
    def __init__(self, parent, game_state, star) -> None:
        super().__init__('', parent)
        self.clicked.connect(
            lambda: game_state.star_info_frame.show_window(star))
        self.setGeometry(20, 20, 20, 20)
        self.setToolTip(star.name)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            f"border-radius : 10; border : 1px solid black; background-color: {star.color}")
