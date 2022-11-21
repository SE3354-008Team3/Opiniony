from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QListWidget, QMessageBox
from PyQt5.QtCore import Qt

class Ui_Results(object):

    def analysis(self):
        from analysis import Ui_MainWindow
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow, usr)
        self.MainWindow.show()

    def setupUi(self, Results, user):
        Results.setObjectName("Results")
        Results.setEnabled(True)
        Results.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Results)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 40, 91, 41))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 671, 351))
        self.label_2.setObjectName("label_2")
        
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(50, 20, 93, 28))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.analysis)
        self.pushButton2.clicked.connect(Results.close)
        
        Results.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Results)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Results.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Results)
        self.statusbar.setObjectName("statusbar")
        Results.setStatusBar(self.statusbar)
        
        global usr
        usr = user

        self.retranslateUi(Results)
        QtCore.QMetaObject.connectSlotsByName(Results)
        
        resultText = ""
        for x in user.getAnalysis():
            resultText += "Date: " + str(x['date']) + '\t\t\t' + 'Value: ' + str(x['value']) + '\n\n' + 'Text: ' + x['string'] + '\n\n\n'
            # resulttext += ''   
        self.label_2.setText(str(resultText))

    def retranslateUi(self, Results):
        _translate = QtCore.QCoreApplication.translate
        Results.setWindowTitle(_translate("Results", "Results"))
        self.label.setText(_translate("Results", "<html><head/><body><p><span style=\" font-size:16pt;\">Results</span></p></body></html>"))
        self.label_2.setText(_translate("Results", "<html><head/><body><p><span style=\" font-size:12pt;\">TextLabel</span></p></body></html>"))
        self.pushButton2.setText(_translate("MainWindow", "Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Results = QtWidgets.QMainWindow()
    ui = Ui_Results()
    ui.setupUi(Results)
    Results.show()
    sys.exit(app.exec_())

