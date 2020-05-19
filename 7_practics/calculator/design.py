# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(290, 421)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color : black;")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label.setAcceptDrops(False)
        self.label.setStyleSheet("QLabel {\n"
"  qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"  background-color: black; \n"
"   color: white\n"
"}\n"
"\n"
"\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_n8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n8.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n8.setFont(font)
        self.pushButton_n8.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"   background-color : white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255, 250, 250, 0.9);\n"
"}")
        self.pushButton_n8.setObjectName("pushButton_n8")
        self.gridLayout.addWidget(self.pushButton_n8, 2, 1, 1, 1)
        self.pushButton_div = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_div.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255, 140, 0, 0.9);\n"
"}")
        self.pushButton_div.setObjectName("pushButton_div")
        self.gridLayout.addWidget(self.pushButton_div, 1, 4, 1, 1)
        self.pushButton_n0 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n0.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n0.setFont(font)
        self.pushButton_n0.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"  background-color : white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255, 250, 250, 0.9);\n"
"}\n"
"")
        self.pushButton_n0.setObjectName("pushButton_n0")
        self.gridLayout.addWidget(self.pushButton_n0, 5, 0, 1, 2)
        self.pushButton_mr = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_mr.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_mr.setFont(font)
        self.pushButton_mr.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(220, 220, 220, 0.8);\n"
"}")
        self.pushButton_mr.setObjectName("pushButton_mr")
        self.gridLayout.addWidget(self.pushButton_mr, 1, 3, 1, 1)
        self.pushButton_n4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n4.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n4.setFont(font)
        self.pushButton_n4.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    background-color : white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255, 250, 250, 0.9);\n"
"}")
        self.pushButton_n4.setObjectName("pushButton_n4")
        self.gridLayout.addWidget(self.pushButton_n4, 3, 0, 1, 1)
        self.pushButton_n3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n3.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n3.setFont(font)
        self.pushButton_n3.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"  background-color : white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255, 250, 250, 0.9);\n"
"}")
        self.pushButton_n3.setObjectName("pushButton_n3")
        self.gridLayout.addWidget(self.pushButton_n3, 4, 3, 1, 1)
        self.pushButton_n7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n7.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n7.setFont(font)
        self.pushButton_n7.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"   background-color : white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255, 250, 250, 0.9);\n"
"}")
        self.pushButton_n7.setObjectName("pushButton_n7")
        self.gridLayout.addWidget(self.pushButton_n7, 2, 0, 1, 1)
        self.pushButton_mul = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_mul.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255, 140, 0, 0.9);\n"
"}")
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.gridLayout.addWidget(self.pushButton_mul, 2, 4, 1, 1)
        self.pushButton_eq = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_eq.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_eq.setFont(font)
        self.pushButton_eq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_eq.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255, 140, 0, 0.9);\n"
"}")
        self.pushButton_eq.setObjectName("pushButton_eq")
        self.gridLayout.addWidget(self.pushButton_eq, 5, 4, 1, 1)
        self.pushButton_n9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n9.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n9.setFont(font)
        self.pushButton_n9.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    background-color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255, 250, 250, 0.9);\n"
"}\n"
"")
        self.pushButton_n9.setObjectName("pushButton_n9")
        self.gridLayout.addWidget(self.pushButton_n9, 2, 3, 1, 1)
        self.pushButton_m = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_m.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_m.setFont(font)
        self.pushButton_m.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(220, 220, 220, 0.8);\n"
"}")
        self.pushButton_m.setObjectName("pushButton_m")
        self.gridLayout.addWidget(self.pushButton_m, 1, 1, 1, 1)
        self.pushButton_n2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n2.setFont(font)
        self.pushButton_n2.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"   background-color : white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255, 250, 250, 0.9);\n"
"}\n"
"")
        self.pushButton_n2.setObjectName("pushButton_n2")
        self.gridLayout.addWidget(self.pushButton_n2, 4, 1, 1, 1)
        self.pushButton_ac = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_ac.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_ac.setFont(font)
        self.pushButton_ac.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(220, 220, 220, 0.8);\n"
"}")
        self.pushButton_ac.setObjectName("pushButton_ac")
        self.gridLayout.addWidget(self.pushButton_ac, 1, 0, 1, 1)
        self.pushButton_pc = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_pc.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_pc.setFont(font)
        self.pushButton_pc.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(220, 220, 220, 0.8);\n"
"}")
        self.pushButton_pc.setObjectName("pushButton_pc")
        self.gridLayout.addWidget(self.pushButton_pc, 5, 3, 1, 1)
        self.pushButton_n1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n1.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n1.setFont(font)
        self.pushButton_n1.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"   background-color : white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255, 250, 250, 0.9);\n"
"}")
        self.pushButton_n1.setObjectName("pushButton_n1")
        self.gridLayout.addWidget(self.pushButton_n1, 4, 0, 1, 1)
        self.pushButton_n6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n6.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n6.setFont(font)
        self.pushButton_n6.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"   background-color : white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255, 250, 250, 0.9);\n"
"}\n"
"")
        self.pushButton_n6.setObjectName("pushButton_n6")
        self.gridLayout.addWidget(self.pushButton_n6, 3, 3, 1, 1)
        self.pushButton_n5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n5.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_n5.setFont(font)
        self.pushButton_n5.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"    background-color : white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255, 250, 250, 0.9);\n"
"}\n"
"")
        self.pushButton_n5.setObjectName("pushButton_n5")
        self.gridLayout.addWidget(self.pushButton_n5, 3, 1, 1, 1)
        self.pushButton_sub = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_sub.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_sub.setFont(font)
        self.pushButton_sub.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255, 140, 0, 0.9);\n"
"}")
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.gridLayout.addWidget(self.pushButton_sub, 3, 4, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_add.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(255, 140, 0, 0.9);\n"
"}")
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 4, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton_n8.setText(_translate("MainWindow", "8"))
        self.pushButton_n8.setShortcut(_translate("MainWindow", "8"))
        self.pushButton_div.setText(_translate("MainWindow", "÷"))
        self.pushButton_div.setShortcut(_translate("MainWindow", "/"))
        self.pushButton_n0.setText(_translate("MainWindow", "0"))
        self.pushButton_n0.setShortcut(_translate("MainWindow", "0"))
        self.pushButton_mr.setText(_translate("MainWindow", "%"))
        self.pushButton_mr.setShortcut(_translate("MainWindow", "R"))
        self.pushButton_n4.setText(_translate("MainWindow", "4"))
        self.pushButton_n4.setShortcut(_translate("MainWindow", "4"))
        self.pushButton_n3.setText(_translate("MainWindow", "3"))
        self.pushButton_n3.setShortcut(_translate("MainWindow", "3"))
        self.pushButton_n7.setText(_translate("MainWindow", "7"))
        self.pushButton_n7.setShortcut(_translate("MainWindow", "7"))
        self.pushButton_mul.setText(_translate("MainWindow", "x"))
        self.pushButton_mul.setShortcut(_translate("MainWindow", "*"))
        self.pushButton_eq.setText(_translate("MainWindow", "="))
        self.pushButton_eq.setShortcut(_translate("MainWindow", "Return"))
        self.pushButton_n9.setText(_translate("MainWindow", "9"))
        self.pushButton_n9.setShortcut(_translate("MainWindow", "9"))
        self.pushButton_m.setText(_translate("MainWindow", "+/-"))
        self.pushButton_m.setShortcut(_translate("MainWindow", "M"))
        self.pushButton_n2.setText(_translate("MainWindow", "2"))
        self.pushButton_n2.setShortcut(_translate("MainWindow", "2"))
        self.pushButton_ac.setText(_translate("MainWindow", "AC"))
        self.pushButton_ac.setShortcut(_translate("MainWindow", "Esc"))
        self.pushButton_pc.setText(_translate("MainWindow", "."))
        self.pushButton_pc.setShortcut(_translate("MainWindow", "%"))
        self.pushButton_n1.setText(_translate("MainWindow", "1"))
        self.pushButton_n1.setShortcut(_translate("MainWindow", "1"))
        self.pushButton_n6.setText(_translate("MainWindow", "6"))
        self.pushButton_n6.setShortcut(_translate("MainWindow", "6"))
        self.pushButton_n5.setText(_translate("MainWindow", "5"))
        self.pushButton_n5.setShortcut(_translate("MainWindow", "5"))
        self.pushButton_sub.setText(_translate("MainWindow", "-"))
        self.pushButton_sub.setShortcut(_translate("MainWindow", "-"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_add.setShortcut(_translate("MainWindow", "+"))
        self.actionExit.setText(_translate("MainWindow", "Выйти"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionReset.setText(_translate("MainWindow", "Обновить"))
        self.actionReset.setShortcut(_translate("MainWindow", "Ctrl+R"))
