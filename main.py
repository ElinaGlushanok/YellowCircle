import sys
from random import randint
from CircleClass import CircleClass
from PyQt5.QtWidgets import  QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor

class Circle(CircleClass):
    def __init__(self):
        super().__init__()
        self.draw = False
        self.drawCircle.clicked.connect(self.new_circle)

    def new_circle(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        if self.draw:
            painter = QPainter(self)
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            painter.setPen(QColor(r, g, b))
            painter.setBrush(QColor(r, g, b))
            rad = randint(1, 200)
            painter.drawEllipse(100, 150, rad, rad)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())


