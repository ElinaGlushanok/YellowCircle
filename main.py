import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import  QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt

class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('circle.ui', self)
        self.draw = False
        self.drawCircle.clicked.connect(self.new_circle)

    def new_circle(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        if self.draw:
            painter = QPainter(self)
            painter.setPen(QColor(255, 255, 0))
            painter.setBrush(QColor(255, 255, 0))
            r = randint(1, 300)
            painter.drawEllipse(250, 250, r, r)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())


