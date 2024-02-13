from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel

class Header(QWidget):
    def __init__(self, game_state):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)
        pause_btn = QPushButton('>')
        pause_btn.setMinimumSize(40,40)
        pause_btn.clicked.connect(lambda: game_state.changeState(pause_btn))
        speed_up_btn = QPushButton('Скорость х1')
        speed_up_btn.setMinimumSize(40,40)
        speed_up_btn.clicked.connect(lambda:game_state.change_speed_up(speed_up_btn))
        map_btn = QPushButton('map')
        map_btn.setMinimumSize(40,40)
        map_btn.clicked.connect(lambda:game_state.change_frame('map'))
        otherFrame_btn = QPushButton('other_frame')
        otherFrame_btn.setMinimumSize(40,40)
        otherFrame_btn.clicked.connect(lambda:game_state.change_frame('other_frame'))
        self.label = QLabel()
        self.label.setText(str(game_state.day))
        layout.addWidget(pause_btn)
        layout.addWidget(speed_up_btn)
        layout.addWidget(map_btn)
        layout.addWidget(otherFrame_btn)
        layout.addWidget(self.label)
        layout.addStretch(1)