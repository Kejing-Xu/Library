# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '图书馆交互界面.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_library(object):
    def setupUi(self, library):
        library.setObjectName("library")
        library.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(library)
        self.pushButton.setGeometry(QtCore.QRect(130, 120, 131, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(library)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 170, 131, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(library)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 220, 131, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(library)
        self.label.setGeometry(QtCore.QRect(80, 40, 241, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(library)
        self.label_2.setGeometry(QtCore.QRect(80, 70, 241, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(library)
        self.pushButton.clicked.connect(library.click_admin)
        self.pushButton_2.clicked.connect(library.click_reader)
        self.pushButton_3.clicked.connect(library.click_util)
        QtCore.QMetaObject.connectSlotsByName(library)

    def retranslateUi(self, library):
        _translate = QtCore.QCoreApplication.translate
        library.setWindowTitle(_translate("library", "图书馆"))
        self.pushButton.setText(_translate("library", "管理员"))
        self.pushButton_2.setText(_translate("library", "读者"))
        self.pushButton_3.setText(_translate("library", "仅查看"))
        self.label.setText(_translate("library", "欢迎来到图书管理系统！"))
        self.label_2.setText(_translate("library", "请问您的身份是："))
