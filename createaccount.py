from PyQt5 import QtCore, QtGui, QtWidgets
from dbcontroller import DBController
from user import User

class Ui_CreateAccount(object):

    def analysis(self):
        from analysis import Ui_MainWindow
        import sys
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow, user)
        self.MainWindow.show()
        
    def login(self):
        from login import Ui_Login
        import sys
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Login()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(445, 410)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(170, 310, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 270, 93, 28))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(300, 270, 93, 28))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.login)
        self.pushButton2.clicked.connect(Dialog.close)
        
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 190, 161, 22))
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 230, 161, 22))
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 70, 161, 22))
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 150, 161, 22))
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 110, 161, 22))
        self.lineEdit_5.setClearButtonEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        
        global dl
        dl = Dialog
        
        self.pushButton.clicked.connect(self.clicked)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def clicked(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        fname = self.lineEdit_3.text()
        email = self.lineEdit_4.text()
        lname = self.lineEdit_5.text()
        dbc = DBController()
        
        if dbc.checkIfUserExists(username, email):
            self.label.setText("User already exists!")
        else:
            dbc.createUser(username, password, email, fname, lname)
            global user
            user = dbc.getUser(username, password)
            self.analysis()
            dl.close()
            #self.label.setText("User created successfully")
        self.update()
        
            
    def update(self):
        self.label.adjustSize()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Create Account"))
        self.label.setText(_translate("Dialog", "New Label"))
        self.pushButton.setText(_translate("Dialog", "Confirm"))
        self.pushButton2.setText(_translate("Dialog", "Login"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Password"))
        self.label_2.setText(_translate("Dialog", "Enter details to create an account"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "First Name"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Email"))
        self.lineEdit_5.setPlaceholderText(_translate("Dialog", "Last Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_CreateAccount()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

