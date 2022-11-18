from PyQt5 import QtCore, QtGui, QtWidgets
from dbcontroller import DBController
from user import User

class Ui_Login(object):

    def analysis(self):
        from analysis import Ui_MainWindow
        import sys
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow, user)
        self.MainWindow.show()
        
    def createaccount(self):
        from createaccount import Ui_CreateAccount
        import sys
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_CreateAccount()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

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
        
        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(300, 170, 93, 28))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.createaccount)
        self.pushButton2.clicked.connect(Dialog.close)
        
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
        
        global dl
        dl = Dialog
        
        self.pushButton.clicked.connect(self.clicked)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def clicked(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        dbc = DBController()

        global user
        user = dbc.getUser(username, password)
        if user is not None:
            #self.label.setText("Username: " + user.getUsername() + "\nEmail: " + user.getEmail() + "\nFirst Name: " + user.getFirstName() + "\nLast Name: " + user.getLastName())
            self.analysis()
            dl.close()
        else:
            self.label.setText("User not found")
        self.update()
            
    def update(self):
        self.label.adjustSize()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "New Label"))
        self.pushButton.setText(_translate("Dialog", "Confirm"))
        self.pushButton2.setText(_translate("Dialog", "Create Account"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Password"))
        self.label_2.setText(_translate("Dialog", "Enter your username and password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

