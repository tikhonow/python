import sys
import time
import sqlite3
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTextEdit, QTableWidgetItem


class MyWindow(QMainWindow):
    data = []
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui',self)
        self.con = sqlite3.connect("films.db")
        self.cur = self.con.cursor()
        self.find1.clicked.connect(self.find_name)
        self.find2.clicked.connect(self.find_parametrs)
        title = ('ID','Название','Год','Продолжительность')
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Interactive)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        ls = self.cur.execute(f'SELECT * FROM genres').fetchall()
        ls = [elem[1] for elem in ls]
        ls.sort()
        self.combo.addItems(ls)
        self.save.triggered.connect(self.save_func)
        self.delet.clicked.connect(self.del_prep)
        self.add.clicked.connect(self.add_prep)

    def add_prep(self):
        add.show()

    def del_prep(self):
        notice.show()
        
    def save_func(self):
        to_check = []
        from_check = []
        for i in range(len(self.data)):
            ID = self.tableWidget.item(i, 0).text()
            NAME = self.tableWidget.item(i, 1).text()
            YEAR = self.tableWidget.item(i, 2).text()
            DUR = self.tableWidget.item(i, 3).text()
            to_check.append((ID, NAME, YEAR, DUR))
            ID1 = str(self.data[i][0])
            NAME1 = str(self.data[i][1])
            YEAR1 = str(self.data[i][2])
            DUR1 = str(self.data[i][4])
            from_check.append((ID1, NAME1, YEAR1, DUR1))
        for elem in to_check:
            if elem not in from_check:
                self.cur.execute(f'UPDATE films SET title = \'{elem[1]}\' WHERE id = \'{elem[0]}\'')
        self.con.commit()

    def find_name(self):
        name = self.name.text()
        self.data = self.cur.execute(f'SELECT * FROM Films WHERE Title LIKE \'%{name}%\'').fetchmany(100)
        self.prnt()

    def find_parametrs(self):
        dur = self.dur.text().isnumeric()
        year = self.year.text().isnumeric()
        f = self.combo.currentText()
        reguest = ''
        if f == 'не выбрано':
            reguest = 'SELECT * FROM Films'
            if dur or year:
                reguest += " WHERE "
            if dur:
                txt = self.dur.text()
                reguest += f'duration = \'{txt}\''
            if dur and year:
                reguest += " AND "
            if year:
                txt = self.year.text()
                reguest += f'year = \'{txt}\''
        else:
            ID = self.cur.execute(f'SELECT * FROM Genres WHERE title = \'{f}\'').fetchall()
            reguest = f'SELECT * FROM Films WHERE genre = \'{ID[0][0]}\''
            if dur:
                txt = self.dur.text()
                reguest += f' AND duration = \'{txt}\''
            if year:
                txt = self.year.text()
                reguest += f' AND year = \'{txt}\''
        self.data = self.cur.execute(reguest).fetchmany(100)
        self.prnt()

    def prnt(self):
        self.tableWidget.setRowCount(0)
        for i, line in enumerate(self.data):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                item = QTableWidgetItem(str(line[0]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 0, item)
                self.tableWidget.setItem(i, 1, QTableWidgetItem(line[1]))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(line[2])))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(str(line[4])))
        self.tableWidget.resizeColumnsToContents()
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    notice = Notice()
    add = Add()
    sys.exit(app.exec_())