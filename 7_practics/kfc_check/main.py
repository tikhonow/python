import sys, os, design
import check_design
from PyQt5 import QtWidgets
from PyQt5 import QtPrintSupport
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import re
import random
import datetime
ice,bur,five,kur = "","","",""
global final_price
final_price = []

class HtmlEditor(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.action_exit.triggered.connect(self.app_exit)
        self.action_reset.triggered.connect(self.reset)
        #Вывод в отдельное окно
        self.dialog = Dialog()

    def run(self):
        self.show_dialog()
        self.generate_receipt_head()
        if self.check_ice.isChecked() or self.spin_ice.value()!= 0:
            ice = self.check(self.check_ice.text(),"ice")
            self.print_check(ice)
        if self.check_bur.isChecked() or self.spin_bur.value()!= 0:
            bur = self.check(self.check_bur.text(),"bur")
            self.print_check(bur)
        if self.check_five.isChecked() or self.spin_five.value()!= 0:
            five = self.check(self.check_five.text(),"five")
            self.print_check(five)
        if self.check_kur.isChecked() or self.spin_kur.value()!= 0:
            kur = self.check(self.check_kur.text(),"kur")
            self.print_check(kur)
        self.print_final_price()

    def check(self,string1,name1):
        price = re.findall('(\d+)', string1)
        #count = getattr(self, 'spin_%s' % name1).value()
        count = 1 if getattr(self, 'spin_%s' % name1).value() == 0 else getattr(self, 'spin_%s' % name1).value()
        price = int(price[0]) * count
        final_price.append(price)
        pattern = re.compile(r'\w+')
        string1 = pattern.search(string1).group()
        return(f"{string1} X {count} ИТОГО: {price} Р")

    def show_dialog(self):
        self.dialog.show()

    def generate_receipt_head(self):
        self.dialog.textBrowser.setText(('<h4 align="center"> Продукция KFC рекомендуется для потребления\
            территории предприятия </h4><hr><h5 align="center">Ваш номер заказа в очереди</h5>'))
        time = datetime.datetime.now()
        time = time.strftime("%d-%m-%Y %H:%M")
        self.dialog.textBrowser.append((f"<h1> {random.randint(100,999)}</h1>"))
        self.dialog.textBrowser.append((f"Время: {time}"))

    def print_check(self,possition):
        self.dialog.textBrowser.append((f"<br><hr><ul><li>{possition}</li>"))

    def print_final_price(self):
        self.dialog.textBrowser.append((f"<br><hr> ИТОГО:{sum(final_price)} рублей"))

    def app_exit(self):
        self.action_exit = sys.exit()

    def reset(self):
        self.check_ice.setCheckState(False)
        self.check_bur.setCheckState(False)
        self.check_five.setCheckState(False)
        self.check_kur.setCheckState(False)
        self.spin_ice.setValue(0)
        self.spin_bur.setValue(0)
        self.spin_five.setValue(0)
        self.spin_kur.setValue(0)

        

class Dialog(QtWidgets.QDialog, check_design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = HtmlEditor()  # Создаём объект класса HtmlEditor
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

u_t = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt;\">Продукция KFC рекомендуется для потребления на территории предприятия</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">------------------------------------------------------------------</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Ваш номер заказа в очереди</span></p></body></html>"
