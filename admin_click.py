from PyQt5 import QtWidgets
import sys
import pymysql
from admin_interact import Ui_Administrator
from admin import AdminClass


class Admin(QtWidgets.QMainWindow, Ui_Administrator):
    def __init__(self):
        super(Admin, self).__init__()
        self.setupUi(self)
        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password='471225ABCD',
                                    database='library')
        self.cursor = self.conn.cursor()
        self.AdminClass =AdminClass

    def click_add_book(self):
        self.AdminClass().add_newbook()

    def click_add_card(self):
        self.AdminClass().add_card()

    def click_delete_book(self):
        self.AdminClass().delete_book()

    def click_delete_card(self):
        self.AdminClass().delete_card()


app = QtWidgets.QApplication(sys.argv)
# MainWindow = QMainWindow()
window = Admin()
window.show()
sys.exit(app.exec_())