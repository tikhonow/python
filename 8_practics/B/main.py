# Способ второй: использовать pyuic
# первым делом нужно выполнить команду pyuic5 ui_file.ui -o ui_file.py, которая создаст класс с дизайном
# далее нужно наследовать разрабатываемый класс от созданного
import sys
import sqlite3
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTextEdit, QTableWidgetItem
from desb import Ui_MainWindow
 

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("films.db")
        self.commandLinkButton.clicked.connect(self.res)
        self.cur = self.con.cursor()
        title = ('Название','Год','Продолжительность')
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        ls = self.cur.execute(f'SELECT * FROM genres').fetchall()
        ls = [elem[1] for elem in ls]
        ls.sort()
        self.combo.addItems(ls)


    def res(self):
        self.tableWidget.setRowCount(0)
        f = self.combo.currentText()
        if f == 'Не выбрано':
            data = self.cur.execute('SELECT * FROM Films').fetchmany(10)
        else:
            ID = self.cur.execute(f'SELECT * FROM Genres WHERE title = \'{f}\'').fetchall()
            data = self.cur.execute(f'SELECT * FROM Films WHERE genre = \'{ID[0][0]}\'').fetchmany(100)
        for i, line in enumerate(data):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                self.tableWidget.setItem(i, 0, QTableWidgetItem(line[1]))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(line[2])))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(line[4])))
 

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())