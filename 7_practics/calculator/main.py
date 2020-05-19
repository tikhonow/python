import sys, os, design
from PyQt5 import QtWidgets
from PyQt5 import QtPrintSupport
from PyQt5.QtGui import *
from PyQt5.QtCore import *

zero_error = 'Делить на 0' + '\n' + 'нельзя !'
uncorrect = 'Ошибка!' + '\n' + 'Данные не верны !'
class Calculator(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #кнопки 0 - 9
        self.pushButton_n0.clicked.connect(self.print_l)
        self.pushButton_n1.clicked.connect(self.print_l)
        self.pushButton_n2.clicked.connect(self.print_l)
        self.pushButton_n3.clicked.connect(self.print_l)
        self.pushButton_n4.clicked.connect(self.print_l)
        self.pushButton_n5.clicked.connect(self.print_l)
        self.pushButton_n6.clicked.connect(self.print_l)
        self.pushButton_n7.clicked.connect(self.print_l)
        self.pushButton_n8.clicked.connect(self.print_l)
        self.pushButton_n9.clicked.connect(self.print_l)
        #кнопки операций и скобок
        self.pushButton_div.clicked.connect(self.print_l)
        self.pushButton_mul.clicked.connect(self.print_l)
        self.pushButton_sub.clicked.connect(self.print_l)
        self.pushButton_add.clicked.connect(self.print_l)
        self.pushButton_sk_left.clicked.connect(self.print_l)
        self.pushButton_sk_right.clicked.connect(self.print_l)
        #cxbnftv
        self.pushButton_eq.clicked.connect(self.calc)
        self.pushButton_ac.clicked.connect(self.res)

    def print_l(self):
        if self.label.text() == '0' or self.label.text() == zero_error:
            self.label.setText('')
        sender = self.label.text() + self.sender().text()
        self.label.setText(sender)
    
    def calc(self):
        try:
            answer = eval(self.label.text())
            print(answer)
            self.label.setText(str(answer))
        except ArithmeticError:
            self.label.setText(str(zero_error))
        except Exception:
            self.label.setText(uncorrect)

    def res(self):
        self.label.setText('')

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Calculator()  # Создаём объект класса Calculator
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
