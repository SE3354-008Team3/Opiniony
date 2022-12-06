from PyQt5 import QtCore, QtGui, QtWidgets
from sentiClass import SentimentAnalysis
from dbcontroller import DBController
from user import User

class Ui_MainWindow(object):

    def account(self):
        from account import Ui_Account
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Account()
        self.ui.setupUi(self.MainWindow, usr)
        self.MainWindow.show()
        
    def results(self):
        from results import Ui_Results
        self.Results = QtWidgets.QMainWindow()
        self.ui = Ui_Results()
        self.ui.setupUi(self.Results, usr)
        self.Results.show()

    def setupUi(self, MainWindow, user):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 30, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 300, 800, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 230, 131, 28))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 130, 501, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhUrlCharactersOnly)
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 190, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(60, 220, 501, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_2.setInputMethodHints(QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhNoPredictiveText)
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 300, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 400, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.account)
        self.pushButton_3.clicked.connect(MainWindow.close)
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 450, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.results)
        self.pushButton_4.clicked.connect(MainWindow.close)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.pushButton_2.clicked.connect(self.clicked)

        global usr
        usr = user
        
        global mw
        mw = MainWindow
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def clicked(self):
        url = self.textEdit.toPlainText() # url to web scrape
        text = self.textEdit_2.toPlainText() # text to analyze
        anl = 0
        if text != "":
            anl, _ = SentimentAnalysis.sentimentAnalysis(userInput=text)
        else:
            anl, text = SentimentAnalysis.sentimentAnalysis(url=url)
        self.label_4.setText("Analysis value: " + str(anl) + "\nString: " + text)
        dbc = DBController()
        dbc.uploadAnalysis(usr, anl, text)
        #usr.getAnalysis().append(anl)
        self.update()
        # call bertTester using text/url as parameter
        
    def update(self):
        self.label.adjustSize()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Home"))
        self.label_2.setText(_translate("MainWindow", "New Analysis URL"))
        self.label_4.setText(_translate("MainWindow", "Analysis value: \nString: "))
        self.pushButton.setText(_translate("MainWindow", "Upload Document"))
        self.label_3.setText(_translate("MainWindow", "New Analysis Text"))
        self.pushButton_2.setText(_translate("MainWindow", "Analyze"))
        self.pushButton_3.setText(_translate("MainWindow", "Account"))
        self.pushButton_4.setText(_translate("MainWindow", "Results"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Enter URL"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Enter text to analyze"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
