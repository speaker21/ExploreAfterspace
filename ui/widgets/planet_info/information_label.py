from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt

class InformationLabel(QWidget):
    def __init__(self, title, value):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: white')
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.title = QLabel(str(title))
        self.value = QLabel(str(value))
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.value)
        self.layout.addStretch(1)

