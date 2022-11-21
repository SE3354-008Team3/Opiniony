import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from login import LoginUI
from createaccount import CreateAccountUI
from user import User

class MainUI:
    def __init__(self):
        # initialize the main window
        self.mainWindow = QtWidgets.QMainWindow()
        self.initLoginUi()

    def initLoginUi(self):
        self.loginWindow = LoginUI()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainUI()
    sys.exit(app.exec_())