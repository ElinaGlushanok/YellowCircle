from random import randint
from PyQt5.QtWidgets import  QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor

class CircleClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.drawCircle = QPushButton('окружность', self)
        self.draw = False
        self.drawCircle.clicked.connect(self.new_circle)