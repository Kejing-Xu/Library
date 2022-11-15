import os
from PyQt5 import QtWidgets
import sys
import pymysql
from sign_in import Ui_signin


class Sign(QtWidgets.QMainWindow, Ui_signin):
    def __init__(self):
        super(Sign, self).__init__()
        self.setupUi(self)
        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password='471225ABCD',
                                    database='library')
        self.cursor = self.conn.cursor()

    def comfirm(self):
        user_name=self.lineEdit.text()
        pw=self.lineEdit_2.text()
        sql_reader = 'select * from card where cno="%s" and password="%s"' % (user_name, pw)
        try:
            self.cursor.execute(sql_reader)
            administrator = self.cursor.fetchall()
            if len(administrator) == 0:
                print("请检查你的用户名和密码")
                return
            os.system("python reader_click.py %s" %user_name)
        except:
            print("登陆失败")
            return


app = QtWidgets.QApplication(sys.argv)
# MainWindow = QMainWindow()
window = Sign()
window.show()
sys.exit(app.exec_())