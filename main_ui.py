# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import threading

import markdown
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

import data.requests
from api import Ui_Form
from database.db import key_get
from proxy import Ui_Form as Ui_Form_proxy


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(270, 462)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 252, 341))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(11, 355, 201, 51))
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(215, 355, 47, 51))
        font.setFamily("黑体")
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(215, 330, 47, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 270, 22))
        self.menubar.setObjectName("menubar")
        self.menuAPI_Key = QtWidgets.QMenu(self.menubar)
        self.menuAPI_Key.setObjectName("menuAPI_Key")
        MainWindow.setMenuBar(self.menubar)
        MainWindow.setWindowIcon(QtGui.QIcon("icon.ico"))

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAPI = QtWidgets.QAction(MainWindow)
        self.actionAPI.setObjectName("actionAPI")
        self.menuAPI_Key.addAction(self.actionAPI)
        self.menubar.addAction(self.menuAPI_Key.menuAction())
        self.actionproxy = QtWidgets.QAction(MainWindow)
        self.actionproxy.setObjectName("actionproxy")
        self.menuAPI_Key.addAction(self.actionproxy)

        self.retranslateUi(MainWindow)
        self.pushButton.pressed.connect(self.add_data)
        self.pushButton.clicked.connect(self.call_function)
        self.pushButton.clicked.connect(self.textEdit.clear)
        self.pushButton_2.clicked.connect(self.textBrowser.clear)
        self.actionAPI.triggered.connect(self.window_api)
        self.actionproxy.triggered.connect(self.window_proxy)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.textEdit.keyPressEvent = self.on_key_press


    def on_key_press(self, event):
        if event.key() == Qt.Key_Return:
            self.add_data()
            self.call_function()
            self.textEdit.clear()
        else:
            QtWidgets.QPlainTextEdit.keyPressEvent(self.textEdit, event)

    def add_data(self):
        text = self.textEdit.toPlainText()
        self.textBrowser.append("我：" + text + "\n")

    def call_function(self):
        def _slot1(textBrowser, textEdit):
            text = textEdit.toPlainText()
            key = key_get()
            key = key[0]
            role = "user"
            temperature = 0.6
            output = markdown.markdown(data.requests.request(key, role, text, temperature))
            print(output)
            textBrowser.append("ChatGPT：" + output + '\n\n')

        threading.Thread(target=_slot1, args=(self.textBrowser, self.textEdit)).start()

    def window_api(self):
        self.form2 = QtWidgets.QWidget()
        self.ui2 = Ui_Form()
        self.ui2.setupUi(self.form2)
        self.form2.show()

    def window_proxy(self):
        self.form3 = QtWidgets.QWidget()
        self.ui3 = Ui_Form_proxy()
        self.ui3.setupUi(self.form3)
        self.form3.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "梦璃雨落 - ChatGPT"))
        self.pushButton.setText(_translate("MainWindow", "发送"))
        self.pushButton_2.setText(_translate("MainWindow", "清空"))
        self.menuAPI_Key.setTitle(_translate("MainWindow", "设置"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionAPI.setText(_translate("MainWindow", "API Key"))
        self.actionproxy.setText(_translate("MainWindow", "代理设置"))
