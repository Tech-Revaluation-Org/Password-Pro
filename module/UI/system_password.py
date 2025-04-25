from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

# Dummy data for saved passwords (browser, username, password)
saved_passwords = [
    ("Google Chrome", "user1@gmail.com", "pass123"),
    ("Mozilla FireFox", "user2@hotmail.com", "pass456"),
    ("Microsoft Edge", "user3@yahoo.com", "pass789")
]

class sys_ui(object):
    def setupUi(self, MainWindow):
        # Setting up the UI
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Title Label for Saved Password
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(310, 10, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        
        # Show Password Button
        self.show_pass_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_pass_btn.setGeometry(QtCore.QRect(300, 80, 161, 31))
        self.show_pass_btn.setObjectName("show_pass_btn")
        
        # Transfer Password Label
        self.tp_label = QtWidgets.QLabel(self.centralwidget)
        self.tp_label.setGeometry(QtCore.QRect(300, 150, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tp_label.setFont(font)
        self.tp_label.setObjectName("tp_label")
        
        # Source Browser Label
        self.sb_label = QtWidgets.QLabel(self.centralwidget)
        self.sb_label.setGeometry(QtCore.QRect(30, 220, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sb_label.setFont(font)
        self.sb_label.setObjectName("sb_label")
        
        # Target Browser Label
        self.tb_label = QtWidgets.QLabel(self.centralwidget)
        self.tb_label.setGeometry(QtCore.QRect(30, 290, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tb_label.setFont(font)
        self.tb_label.setObjectName("tb_label")
        
        # Source Browser ComboBox
        self.src_brwser = QtWidgets.QComboBox(self.centralwidget)
        self.src_brwser.setGeometry(QtCore.QRect(200, 250, 161, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.src_brwser.setFont(font)
        self.src_brwser.setObjectName("src_brwser")
        self.src_brwser.addItem("Google Chrome")
        self.src_brwser.addItem("Microsoft Edge")
        self.src_brwser.addItem("Mozilla FireFox")
        self.src_brwser.addItem("Brave")
        
        # Target Browser ComboBox
        self.trgt_brwser = QtWidgets.QComboBox(self.centralwidget)
        self.trgt_brwser.setGeometry(QtCore.QRect(190, 320, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.trgt_brwser.setFont(font)
        self.trgt_brwser.setObjectName("trgt_brwser")
        self.trgt_brwser.addItem("Google Chrome")
        self.trgt_brwser.addItem("Microsoft Edge")
        self.trgt_brwser.addItem("Mozilla FireFox")
        self.trgt_brwser.addItem("Brave")
        
        # Transfer Password Button
        self.trnsfr_pass_btn = QtWidgets.QPushButton(self.centralwidget)
        self.trnsfr_pass_btn.setGeometry(QtCore.QRect(440, 280, 161, 31))
        self.trnsfr_pass_btn.setObjectName("trnsfr_pass_btn")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Connect button signals to functions
        self.show_pass_btn.clicked.connect(self.show_saved_passwords)
        self.trnsfr_pass_btn.clicked.connect(self.transfer_passwords)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Manager"))
        self.title.setText(_translate("MainWindow", "Saved Password"))
        self.show_pass_btn.setText(_translate("MainWindow", "Show Passwords"))
        self.tp_label.setText(_translate("MainWindow", "Transfer Password"))
        self.sb_label.setText(_translate("MainWindow", "Source Browser:"))
        self.tb_label.setText(_translate("MainWindow", "Target Browser:"))
        self.trnsfr_pass_btn.setText(_translate("MainWindow", "Transfer"))
        
    def show_saved_passwords(self):
        # For demonstration, using dummy saved password data
        if saved_passwords:
            output = ""
            for browser, username, password in saved_passwords:
                output += f"Browser: {browser}, Username: {username}, Password: {password}\n"
            QMessageBox.information(None, "Saved Passwords", output)
        else:
            QMessageBox.information(None, "Saved Passwords", "No passwords saved.")
            
    def transfer_passwords(self):
        source = self.src_brwser.currentText()
        target = self.trgt_brwser.currentText()
        
        if source == target:
            QMessageBox.warning(None, "Transfer Error", "Source and target browsers must be different!")
        else:
            # Here you would include logic to transfer passwords securely
            # For now, we simulate the transfer with a success message.
            QMessageBox.information(None, "Transfer", 
                                      f"Passwords transferred from {source} to {target} successfully!")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = sys_ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
