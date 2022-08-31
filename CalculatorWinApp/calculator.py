
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainForm(QMainWindow):

    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(200,200,500,500)
        self.initUI()

    def initUI(self):
        self.lbl_num1 = QtWidgets.QLabel(self)
        self.lbl_num1.setText('First Number: ')
        self.lbl_num1.move(50,30)

        self.lbl_num1 = QtWidgets.QLineEdit(self)
        self.lbl_num1.move(150,30)
        self.lbl_num1.resize(200,32)

        self.lbl_num2 = QtWidgets.QLabel(self)
        self.lbl_num2.setText('Second Number: ')
        self.lbl_num2.move(50,80)

        self.lbl_num2 = QtWidgets.QLineEdit(self)
        self.lbl_num2.move(150,80)
        self.lbl_num2.resize(200,32)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText('Topla')
        self.btn_topla.move(150,130)
        self.btn_topla.clicked.connect(self.toplama)

        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText('Çıkar')
        self.btn_cikar.move(150,170)
        self.btn_cikar.clicked.connect(self.cikarma)

        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText('Çarp')
        self.btn_carp.move(150,210)
        self.btn_carp.clicked.connect(self.carpma)

        self.btn_bolme = QtWidgets.QPushButton(self)                              
        self.btn_bolme.setText('Böl')
        self.btn_bolme.move(150,250)
        self.btn_bolme.clicked.connect(self.bolme)

        self.result = QtWidgets.QLabel(self)
        self.result.setText('Result: ')
        self.result.move(400,55)

    def toplama(self):
        result = int(self.lbl_num1.text()) + int(self.lbl_num2.text())
        return self.result.setText('Sonuç: '+ str(result))

    def cikarma(self):
        result = int(self.lbl_num1.text()) - int(self.lbl_num2.text())
        return self.result.setText('Sonuç: '+ str(result))

    def carpma(self):
        result = int(self.lbl_num1.text()) * int(self.lbl_num2.text())
        return self.result.setText('Sonuç: '+ str(result))

    def bolme(self):
        result = int(self.lbl_num1.text()) / int(self.lbl_num2.text())
        return self.result.setText('Sonuç: '+ str(result))




def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()