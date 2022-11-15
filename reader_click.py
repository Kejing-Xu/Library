from PyQt5 import QtWidgets
import sys
from reader_interaction import Ui_reader
from reader import ReaderClass
import sys

cno = sys.argv[1]


class mywindow(QtWidgets.QMainWindow, Ui_reader):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    def click_search(self):
        ReaderClass(cno).get_reader_info()

    def click_change(self):
        ReaderClass(cno).change_personal_file()

    def click_borrow(self):
        ReaderClass(cno).borrow()

    def click_return(self):
        ReaderClass(cno).return_book()

    def click_prolong(self):
        ReaderClass(cno).prolong_borrow()


app = QtWidgets.QApplication(sys.argv)
# MainWindow = QMainWindow()
window = mywindow()
window.show()
sys.exit(app.exec_())
