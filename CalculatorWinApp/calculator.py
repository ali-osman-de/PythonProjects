
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainForm(QMainWindow):

    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(200,200,500,500)
        self.iniUI()

    def initUI(self):
        self.lbl_num1 = QtWidgets.QLabel(self)
        self.lbl_num1.setText('First Number: ')
        self.lbl_num1.move(50,30)


        self.lbl_num2 = QtWidgets.QLabel(self)
        self.lbl_num2.setText('Second Number: ')
        self.lbl_num2.move(50,30)