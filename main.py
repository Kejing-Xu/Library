import os
from PyQt5 import QtWidgets
import sys
from library import Ui_library


class main_interaction(QtWidgets.QMainWindow,Ui_library):
    def __init__(self):
        super(main_interaction, self).__init__()
        self.setupUi(self)

    def click_admin(self):
        os.system("python sign_admin.py")

    def click_reader(self):
        os.system("python sign_reader.py")

    def click_util(self):
        os.system("python util_click.py")


app = QtWidgets.QApplication(sys.argv)
window = main_interaction()
window.show()
sys.exit(app.exec_())