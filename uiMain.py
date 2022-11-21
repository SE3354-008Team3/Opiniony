import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from login import LoginUI
from createaccount import CreateAccountUI
from user import User
from dbcontroller import DBController

class MainUI:
    def __init__(self):
        # initialize the main window
        self.mainWindow = QtWidgets.QMainWindow()
        self.initLoginUi()

    def initLoginUi(self):
        self.loginWindow = LoginUI()


if __name__ == '__main__':
    db = DBController()
    user = db.getUser('collinmatz', 'secretpass123')
    db.uploadAnalysis(user, 1, 'This is a long analysis. I am testing to see how long the string is, and whether that will affect the spacing of the results window or not.')
    app = QtWidgets.QApplication(sys.argv)
    ui = MainUI()
    sys.exit(app.exec_())