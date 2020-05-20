import sys, os, design
from PyQt5 import QtWidgets
from PyQt5 import QtPrintSupport
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import re
ice = ""
bur = ""
kur = ""
five = ""
class HtmlEditor(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
    def run(self):
        if self.check_ice.isChecked() or self.spin_ice.value()!= 0:
            ice = self.check(self.check_ice.text(),"ice")
            print(ice)
        if self.check_bur.isChecked() or self.spin_bur.value()!= 0:
            bur = self.check(self.check_bur.text(),"bur")
            print(bur)
        if self.check_five.isChecked() or self.spin_five.value()!= 0:
            five = self.check(self.check_five.text(),"five")
            print(five)
        if self.check_kur.isChecked() or self.spin_kur.value()!= 0:
            kur = self.check(self.check_kur.text(),"kur")
            print(kur)

    def check(self,string1,name1):
        price = re.findall('(\d+)', string1)
        #count = getattr(self, 'spin_%s' % name1).value()
        count = 1 if getattr(self, 'spin_%s' % name1).value() == 0 else getattr(self, 'spin_%s' % name1).value()
        price = int(price[0]) * count
        pattern = re.compile(r'\w+')
        string1 = pattern.search(string1).group()
        return(f"{string1} X {count} ИТОГО: {price} Р")

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = HtmlEditor()  # Создаём объект класса HtmlEditor
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
