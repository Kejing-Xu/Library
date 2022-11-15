from PyQt5 import QtWidgets
import sys
import pymysql
import util
from util_interaction import Ui_util_interaction


class mywindow(QtWidgets.QMainWindow, Ui_util_interaction):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password='471225ABCD',
                                    database='library')
        self.cursor = self.conn.cursor()
        self.util=util

    def click_search_book(self):
        bno=input("\n请输入书籍号:")
        self.util.find_book(self.cursor,bno)

    def click_all(self):
        self.util.show_all_books(self.cursor)


app = QtWidgets.QApplication(sys.argv)
# MainWindow = QMainWindow()
window = mywindow()
window.show()
sys.exit(app.exec_())