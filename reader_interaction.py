# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reader_interaction.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_reader(object):
    def setupUi(self, reader):
        reader.setObjectName("reader")
        reader.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(reader)
        self.pushButton.setGeometry(QtCore.QRect(60, 90, 131, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(reader)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 90, 131, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(reader)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 150, 131, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(reader)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 210, 131, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(reader)
        self.label.setGeometry(QtCore.QRect(90, 10, 221, 71))
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(reader)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 150, 131, 40))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(reader)
        self.pushButton.clicked.connect(reader.click_search) # type: ignore
        self.pushButton_2.clicked.connect(reader.click_change) # type: ignore
        self.pushButton_3.clicked.connect(reader.click_borrow) # type: ignore
        self.pushButton_4.clicked.connect(reader.click_return) # type: ignore
        self.pushButton_5.clicked.connect(reader.click_prolong) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(reader)

    def retranslateUi(self, reader):
        _translate = QtCore.QCoreApplication.translate
        reader.setWindowTitle(_translate("reader", "读者"))
        self.pushButton.setText(_translate("reader", "查找信息"))
        self.pushButton_2.setText(_translate("reader", "修改信息"))
        self.pushButton_3.setText(_translate("reader", "借阅新书"))
        self.pushButton_4.setText(_translate("reader", "还书"))
        self.label.setText(_translate("reader", "请问您要进行的操作是："))
        self.pushButton_5.setText(_translate("reader", "续借"))