import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic
from os import path
import os

import sys

app = QtWidgets.QApplication([])

win = uic.loadUi("calc.ui") 

win.show()

sys.exit(app.exec())