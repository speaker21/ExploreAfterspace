from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QCoreApplication, Qt

class Star(QPushButton):
    def __init__(self, parent):
        super().__init__('1', parent)
        self.setGeometry(20,20,20,20)
        self.setToolTip('Sun')
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("border-radius : 10; border : 1px solid black; background-color: yellow")
        
    


