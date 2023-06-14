# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proxy.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from database.db import proxy_set, proxy_read


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(290, 99)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(196, 65, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 171, 25))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 62, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton.clicked.connect(self.proxy)
        self.pushButton.clicked.connect(Form.close)
        self.proxy_load()
        Form.setWindowIcon(QtGui.QIcon("icon.ico"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "代理设置"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.label.setText(_translate("Form", "HTTP代理:"))

    def proxy(self):
        ip = self.lineEdit.text()
        proxy_set(ip)

    def proxy_load(self):
        ip = proxy_read()
        ip = ip[0]
        self.lineEdit.setText(ip)
