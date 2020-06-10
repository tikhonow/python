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
from design_b import Ui_MainWindow

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("films.db")
        self.commandLinkButton.clicked.connect(self.run)
        self.cur = self.con.cursor()
        title = ('Название фильма','Год','Продолжительность')
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

    def run(self):
        f = self.textEdit.toPlainText()
        self.tableWidget.setRowCount(0)
        res = self.cur.execute(f'SELECT * FROM genres WHERE title = \'{str(f).lower()}\'').fetchmany(1)
        if len(res) != 0:
            data = self.cur.execute(f'SELECT * FROM Films WHERE genre = \'{res[0][0]}\'').fetchmany(100)
            for i, line in enumerate(data):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                self.tableWidget.setItem(i, 0, QTableWidgetItem(line[1]))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(line[2])))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(line[4])))

            self.tableWidget.resizeColumnsToContents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())