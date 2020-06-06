# свяжем PyQT и csv
# для работы с таблицами в PyQT существует класс QTableWidget. 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QTableWidget, QHBoxLayout
import csv


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.sum = 0.0
        self.loadUI()

        self.loadTable('8_practics/rating_new.csv')

    def loadUI(self):
        self.setGeometry(100, 100, 450, 300)
        self.lay = QHBoxLayout()
        self.table = QTableWidget()
        self.lay.addWidget(self.table)
        self.setLayout(self.lay)

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            title = next(reader)
            self.table.setColumnCount(len(title))
            self.table.setHorizontalHeaderLabels(title)
            self.table.setRowCount(0)
            for i, row in enumerate(reader):
                self.table.setRowCount(self.table.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(elem))
                row.pop(0)
                ar = ((row))
                sum = 0
                for i in ar:
                    sum += int(i)
                print(sum)

                    
        self.table.resizeColumnsToContents()
                
    def colorRow(self, row, color):
        for i in range(self.table.columnCount()):
            self.table.item(row, i).setBackground(color)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

# loadTable загружает данные в таблицу
# для отображения таблицы необходимо указать кол-во столбцов и строк, 
# но так как мы не знаем их кол-во, то будем изменять это значение на ходу
# т.к. reader - итератор, то получить можно получить первое значение с помощью функции next
# setHorizontalHeaderLabels устанавливает горизонтальные заголовки для таблицы
# setColumnCount устанавливаем в 0, далее на каждой итерации будем увеличивать на один перед добавлением
# setItem добавляет элемент принимая координаты i, j и сам элемент
# элементом является класс QTableWidgetItem