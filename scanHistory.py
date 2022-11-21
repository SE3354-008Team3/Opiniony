import sys
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QListWidget, QDialog, QApplication, QMessageBox
from PyQt5.QtCore import Qt

class Ui_ScanHistory:
    def __init__(self, user):
        # initialize the login window
        self.window = QDialog()
        self.window.setWindowTitle("Scan History")
        self.window.setGeometry(400,400,800,450)
        self.vbox = QVBoxLayout()
        self.vbox.addSpacing(20)
        scanHistoryLabel = QLabel(self.window)
        scanHistoryLabel.setText("<h3>Scan History</h3>")
        scanHistoryLabel.setAlignment(Qt.AlignCenter)

        # initialize scan history list from user object
        self.scansList = QListWidget()

        analysisList = user.getAnalysis()
        if len(analysisList) > 0:
            for analysis in analysisList:
                self.scansList.addItem(analysis['string'])
        else:
            self.scansList.addItem("No scans to display")
        
        self.scansList.itemClicked.connect(lambda item : self.clicked(item.text(), analysisList))
        self.vbox.addWidget(self.scansList)
        self.window.setLayout(self.vbox)
        self.window.show()
    
    def clicked(self, text, scans):
        date, value = "", ""
        for scan in scans:
            if scan['string'] == text:
                date = str(scan['date'])
                value = str(scan['value'])
                break

        box = QMessageBox()
        box.setText('Value: ' + value + '\n' + 'Date: ' + str(date) + '\n' + 'Text: ' + text)


if __name__ == '__main__':
    from dbcontroller import DBController
    dbc = DBController()
    user = dbc.getUser("collinmatz", "secretpass123")
    # dbc.uploadAnalysis(user, 1, "This is an analysis 234567 with a date!")

    app = QApplication(sys.argv)
    window = Ui_ScanHistory(user)
    sys.exit(app.exec_())