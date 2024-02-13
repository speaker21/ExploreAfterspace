from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QCoreApplication, Qt

class Star(QPushButton):
    def __init__(self, parent, star, game_state):
        super().__init__('', parent)
        self.name = star['name']
        self.planets = star['planets']
        self.color = star['color']
        if 'population' in star:
            self.population = star['population']
        else:
            self.population = None
        self.clicked.connect(lambda:game_state.show_star_info(self))

        self.setGeometry(20,20,20,20)
        self.setToolTip(self.name)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(f"border-radius : 10; border : 1px solid black; background-color: {self.color}")
        
    def calculate_population(self):
        if self.population:
            self.population+=1