"""
https://www.qt.io/qt-for-python
pyside2 is official interface

sudo pacman -S pyside2

"""

from PySide2 import QtCore, QtWidgets, QtGui
import random
import sys


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.hello = ['a', 'b', 'c']
        self.button = QtWidgets.QPushButton('click me')
        self.text = QtWidgets.QLabel('hello world')
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.magic)

    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
