from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication,QMainWindow
import sys

class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button_clicked(self):
        self.label.setText("You Pressed Button")
        self.update()

    def initUI(self):
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Tech with Raj!")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("My First Label")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.button_clicked)


    def update(self):
        self.label.adjustSize()


def window():
    app=QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())

window()