# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'util_interaction.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_util_interaction(object):
    def setupUi(self, util_interaction):
        util_interaction.setObjectName("util_interaction")
        util_interaction.resize(400, 300)
        self.label = QtWidgets.QLabel(util_interaction)
        self.label.setGeometry(QtCore.QRect(90, 60, 241, 41))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(util_interaction)
        self.pushButton.setGeometry(QtCore.QRect(130, 110, 131, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(util_interaction)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 170, 131, 40))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(util_interaction)
        self.pushButton.clicked.connect(util_interaction.click_search_book)
        self.pushButton_2.clicked.connect(util_interaction.click_all)
        QtCore.QMetaObject.connectSlotsByName(util_interaction)

    def retranslateUi(self, util_interaction):
        _translate = QtCore.QCoreApplication.translate
        util_interaction.setWindowTitle(_translate("util_interaction", "查询"))
        self.label.setText(_translate("util_interaction", "请问您要查询的内容是："))
        self.pushButton.setText(_translate("util_interaction", "查找书籍"))
        self.pushButton_2.setText(_translate("util_interaction", "显示所有书籍"))
