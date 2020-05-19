import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5 import QtPrintSupport

#--------
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#=--------
import design  #конвертированный файл дизайна
import os
class HtmlEditor(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.action_4.triggered.connect(self.close_application)#инициализируем кнопку выхода из программы
        self.pushButton.clicked.connect(self.parse_text)
        #работа с текстом
    def parse_text(self):
        textbox = self.plainTextEdit # поле для ввода текста
        text = textbox.toPlainText()
        self.textBrowser.append(text)
        
    def close_application(self):
        sys.exit()
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = HtmlEditor()  # Создаём объект класса HtmlEditor
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()


def exit_from_editor(self):
    self.action_4 = sys.exit()