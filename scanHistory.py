import sys
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QListWidget, QDialog, QApplication, QMessageBox
from PyQt5.QtCore import Qt

class ScanHistoryWindow:

    class CustomListWidget(QListWidget):
        def clicked(self, item):
            QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())

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
        self.scansList = self.CustomListWidget()
        self.scansList.itemClicked.connect(self.scansList.clicked)

        analysisList = user.getAnalysis()
        if len(analysisList) > 0:
            for analysis in analysisList:
                self.scansList.addItem(analysis['string'])
        else:
            self.scansList.addItem("No scans to display")
        
        self.vbox.addWidget(self.scansList)
        self.window.setLayout(self.vbox)
        self.window.show()


if __name__ == '__main__':
    from dbcontroller import DBController
    dbc = DBController()
    user = dbc.getUser("testuser123", "secretpass123")
    # dbc.uploadAnalysis(user, 1, "This is an analysis 2")

    app = QApplication(sys.argv)
    window = ScanHistoryWindow(user)
    sys.exit(app.exec_())