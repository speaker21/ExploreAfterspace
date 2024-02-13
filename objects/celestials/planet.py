from PyQt5.QtWidgets import QPushButton, QWidget
from PyQt5.QtCore import QCoreApplication, Qt

class Planet(QWidget):
    def __init__(self, parent, planet, game_state):
        super().__init__('', parent)
        self.name = planet['name']
        if 'population' in planet:
            self.population = planet['population']
        else:
            self.population = None
        self.clicked.connect(lambda:game_state.star_info_frame.show_window(self))

        self.setGeometry(20,20,20,20)
        self.setToolTip(self.name)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f"border-radius : 10; border : 1px solid black; background-color: {self.color}")
        
    def calculate_population(self):
        if self.population:
            self.population+=1