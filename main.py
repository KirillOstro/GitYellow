import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.paintEvent())

    def paintEvent(self):
        qp = QPainter()
        qp.begin(self)
        for i in range(random.randint(1, 10)):
            self.drawCircle()
        qp.end()

    def drawCircle(self):
        self.qp.setBrush(QColor(255, 255, 0))
        x, y = random.randint(0, 800), random.randint(0, 600)
        width, height = random.randint(0, 100), random.randint(0, 100)
        self.qp.drawEllipse(x, y, width, height)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
