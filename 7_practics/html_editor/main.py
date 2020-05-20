import sys, os, design
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtPrintSupport
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *


class HtmlEditor(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action_4.triggered.connect(self.close_application)
        self.action.triggered.connect(self.info)
        self.action_2.triggered.connect(self.save)
        self.action_3.triggered.connect(self.printer)
        self.pushButton.clicked.connect(self.parse_text)
        self.pushButton_example.clicked.connect(self.example)
    
    def parse_text(self):#перевод текста в html
        textbox = self.plainTextEdit 
        text = textbox.toPlainText()   
        self.textBrowser.setText(text)
    
    def example(self):
        example_html = '''        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Hello!</title>
        </head>
        <body>
            <h1>Hello World!</h1>
            <p>This is a simple paragraph.</p>
        </body>
        </html>'''
        self.plainTextEdit.insertPlainText(example_html)

    def save(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "WEB documents (*.html")
        textbox = self.plainTextEdit 
        text = textbox.toPlainText()   
        try:
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.dialog_critical(str(e))

        else:
            self.path = path

    def printer(self):
        dlg = QPrintDialog()
        if dlg.exec_():
            textbox = self.plainTextEdit  
            self.textbox.print_(dlg.printer())
            
    def info(self):
        info="Данную программу создал Тихонов Руслан.Студент ПМИ 1 курс"
        self.plainTextEdit.insertPlainText("")
        self.plainTextEdit.insertPlainText(info)
    def close_application(self):
        sys.exit()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = HtmlEditor()  # Создаём объект класса HtmlEditor
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
