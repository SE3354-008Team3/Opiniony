# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from dbcontroller import DBController
from user import User

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(445, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 200, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 170, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 90, 161, 22))
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 130, 161, 22))
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.pushButton.clicked.connect(self.clicked)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def clicked(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        dbc = DBController()
        
        user = dbc.getUser(username, password)
        if user is not None:
            self.label.setText("Username: " + user.getUsername() + "\nEmail: " + user.getEmail() + "\nFirst Name: " + user.getFirstName() + "\nLast Name: " + user.getLastName())
        else:
            self.label.setText("User not found")
        self.update()
            
    def update(self):
        self.label.adjustSize()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "New Label"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "New Label"))
        self.pushButton.setText(_translate("Dialog", "Confirm"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Password"))
        self.label_2.setText(_translate("Dialog", "Enter your username and password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

