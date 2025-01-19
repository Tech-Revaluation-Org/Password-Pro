from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import random

password_list = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sidebar = QtWidgets.QFrame(self.centralwidget)
        self.sidebar.setGeometry(QtCore.QRect(9, 9, 121, 581))
        self.sidebar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar.setObjectName("sidebar")
        self.passkeeper_btn = QtWidgets.QPushButton(self.sidebar)
        self.passkeeper_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.passkeeper_btn.setGeometry(QtCore.QRect(10, 50, 101, 23))
        self.passkeeper_btn.setStyleSheet("color: rgb(51, 51, 51);\n"
"background-color: rgb(0, 123, 255);\n"
"border: None;\n"
"")
        self.passkeeper_btn.setObjectName("passkeeper_btn")
        self.passgenarator_btn = QtWidgets.QPushButton(self.sidebar)
        self.passgenarator_btn.setGeometry(QtCore.QRect(10, 110, 101, 23))
        self.passgenarator_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.passgenarator_btn.setStyleSheet("color: rgb(51, 51, 51);\n"
"background-color: rgb(0, 123, 255);\n"
"border: None;")
        self.passgenarator_btn.setObjectName("passgenarator_btn")
        self.viewpass_btn = QtWidgets.QPushButton(self.sidebar)
        self.viewpass_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.viewpass_btn.setGeometry(QtCore.QRect(10, 180, 101, 23))
        self.viewpass_btn.setStyleSheet("color: rgb(51, 51, 51);\n"
"background-color: rgb(0, 123, 255);\n"
"border: None;")
        self.viewpass_btn.setObjectName("viewpass_btn")
        self.settings_btn = QtWidgets.QPushButton(self.sidebar)
        self.settings_btn.setGeometry(QtCore.QRect(10, 540, 101, 23))
        self.settings_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.settings_btn.setStyleSheet("color: rgb(51, 51, 51);\n"
"background-color: rgb(0, 123, 255);\n"
"border: None;")
        self.settings_btn.setObjectName("settings_btn")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(130, 10, 641, 581))
        self.stackedWidget.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.passwordkeperpage = QtWidgets.QWidget()
        self.passwordkeperpage.setObjectName("passwordkeperpage")
        self.wn_label = QtWidgets.QLabel(self.passwordkeperpage)
        self.wn_label.setGeometry(QtCore.QRect(180, 40, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wn_label.setFont(font)
        self.wn_label.setStyleSheet("color: rgb(51, 51, 51);")
        self.wn_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wn_label.setObjectName("wn_label")
        self.website_name = QtWidgets.QLineEdit(self.passwordkeperpage)
        self.website_name.setGeometry(QtCore.QRect(90, 120, 411, 31))
        self.website_name.setStyleSheet("color: rgb(51, 51, 51);\n"
"border: 3px solid #DDDDDD;\n"
"border-radius: 15px;")
        self.website_name.setObjectName("website_name")
        self.user_name = QtWidgets.QLineEdit(self.passwordkeperpage)
        self.user_name.setGeometry(QtCore.QRect(90, 250, 411, 31))
        self.user_name.setStyleSheet("color: rgb(51, 51, 51);\n"
"border: 3px solid #DDDDDD;\n"
"border-radius: 15px;")
        self.user_name.setObjectName("user_name")
        self.usr_n_label = QtWidgets.QLabel(self.passwordkeperpage)
        self.usr_n_label.setGeometry(QtCore.QRect(180, 170, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.usr_n_label.setFont(font)
        self.usr_n_label.setStyleSheet("color: rgb(51, 51, 51);")
        self.usr_n_label.setAlignment(QtCore.Qt.AlignCenter)
        self.usr_n_label.setObjectName("usr_n_label")
        self.pass_label = QtWidgets.QLabel(self.passwordkeperpage)
        self.pass_label.setGeometry(QtCore.QRect(180, 300, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pass_label.setFont(font)
        self.pass_label.setStyleSheet("color: rgb(51, 51, 51);")
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        self.passwords = QtWidgets.QLineEdit(self.passwordkeperpage)
        self.passwords.setGeometry(QtCore.QRect(80, 380, 411, 31))
        self.passwords.setStyleSheet("color: rgb(51, 51, 51);\n"
"border: 3px solid #DDDDDD;\n"
"border-radius: 15px;")
        self.passwords.setObjectName("passwords")
        self.pushButton = QtWidgets.QPushButton(self.passwordkeperpage)
        self.pushButton.setGeometry(QtCore.QRect(240, 450, 91, 31))
        self.pushButton.clicked.connect(self.save_password)
        self.pushButton.setStyleSheet("color: rgb(51, 51, 51);\n"
"background-color: rgb(0, 123, 255);\n"
"border: 3px solid  rgb(0, 123, 255);\n"
"border-radius: 15px")
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.passwordkeperpage)
        self.passwordgenaratorpage = QtWidgets.QWidget()
        self.passwordgenaratorpage.setObjectName("passwordgenaratorpage")
        self.pass_length = QtWidgets.QLineEdit(self.passwordgenaratorpage)
        self.pass_length.setGeometry(QtCore.QRect(70, 190, 181, 20))
        self.pass_length.setObjectName("pass_length")
        self.pass_len_label = QtWidgets.QLabel(self.passwordgenaratorpage)
        self.pass_len_label.setGeometry(QtCore.QRect(90, 140, 201, 31))
        self.pass_len_label.setObjectName("pass_len_label")
        self.pass_strngth = QtWidgets.QComboBox(self.passwordgenaratorpage)
        self.pass_strngth.setGeometry(QtCore.QRect(350, 190, 141, 22))
        self.pass_strngth.setObjectName("pass_strngth")
        self.pass_strngth.addItem("")
        self.pass_strngth.addItem("")
        self.pass_strngth.addItem("")
        self.pass_strn_label = QtWidgets.QLabel(self.passwordgenaratorpage)
        self.pass_strn_label.setGeometry(QtCore.QRect(340, 140, 201, 31))
        self.pass_strn_label.setObjectName("pass_strn_label")
        self.gnrt_pass_btn = QtWidgets.QPushButton(self.passwordgenaratorpage)
        self.gnrt_pass_btn.setGeometry(QtCore.QRect(210, 250, 131, 23))
        self.gnrt_pass_btn.clicked.connect(self.generate_password)
        self.gnrt_pass_btn.setStyleSheet("color: rgb(51, 51, 51);\n"
"background-color: rgb(0, 123, 255);\n"
"border: 3px solid rgb(0, 123, 255);\n"
"border-radius:15px;\n"
"\n"
"")
        self.gnrt_pass_btn.setObjectName("gnrt_pass_btn")
        self.label_3 = QtWidgets.QLabel(self.passwordgenaratorpage)
        self.label_3.setGeometry(QtCore.QRect(140, 30, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.passwordgenaratorpage)
        self.lineEdit.setGeometry(QtCore.QRect(70, 410, 411, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.passwordgenaratorpage)
        self.label_4.setGeometry(QtCore.QRect(120, 320, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.passwordgenaratorpage)
        self.pass_viewpage = QtWidgets.QWidget()
        self.pass_viewpage.setObjectName("pass_viewpage")
        self.header = QtWidgets.QLabel(self.pass_viewpage)
        self.header.setGeometry(QtCore.QRect(180, 20, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.password_tabel = QtWidgets.QTableWidget(self.pass_viewpage)
        self.password_tabel.setGeometry(QtCore.QRect(10, 100, 621, 441))
        self.password_tabel.setObjectName("password_tabel")
        self.password_tabel.setColumnCount(3)
        self.password_tabel.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.password_tabel.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.password_tabel.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.password_tabel.setHorizontalHeaderItem(2, item)
        self.pushButton_3 = QtWidgets.QPushButton(self.pass_viewpage)
        self.pushButton_3.clicked.connect(self.refresh_table)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 550, 121, 23))
        self.pushButton_3.setStyleSheet("color: rgb(51, 51, 51);\n"
"background-color: rgb(0, 123, 255);\n"
"border: 3ppx solid rgb(0, 123, 255);\n"
"border-radius: 10px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.pass_viewpage)
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.theme = QtWidgets.QComboBox(self.settings)
        self.theme.setGeometry(QtCore.QRect(180, 160, 231, 31))
        self.theme.setObjectName("theme")
        self.theme.addItem("")
        self.theme.addItem("")
        self.theme.addItem("")
        self.theme.addItem("")
        self.theme.addItem("")
        self.theme.addItem("")
        self.theme_label = QtWidgets.QLabel(self.settings)
        self.theme_label.setGeometry(QtCore.QRect(200, 80, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.theme_label.setFont(font)
        self.theme_label.setAlignment(QtCore.Qt.AlignCenter)
        self.theme_label.setObjectName("theme_label")
        self.backup_btn = QtWidgets.QPushButton(self.settings)
        self.backup_btn.setGeometry(QtCore.QRect(70, 290, 151, 31))
        self.backup_btn.setStyleSheet("color: rgb(51, 51, 51);\n"
"background-color: rgb(0, 123, 255);\n"
"border: 3px solid rgb(0, 123, 255);\n"
"border-radius: 10px;")
        self.backup_btn.setObjectName("backup_btn")
        self.restr_btn = QtWidgets.QPushButton(self.settings)
        self.restr_btn.setGeometry(QtCore.QRect(330, 290, 151, 31))
        self.restr_btn.setStyleSheet("color: rgb(51, 51, 51);\n"
"background-color: rgb(0, 123, 255);\n"
"border: 3px solid rgb(0, 123, 255);\n"
"border-radius: 10px;")
        self.restr_btn.setObjectName("restr_btn")
        self.pushButton_2 = QtWidgets.QPushButton(self.settings)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 210, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.settings)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def save_password(self):
        website = self.website_name.text().strip()
        username = self.user_name.text().strip()
        password = self.passwords.text().strip()

        if website and username and password:
            password_list.append([website, username, password])
            QMessageBox.information(self.centralwidget, "Success", "Password saved successfully!")
            self.website_name.clear()
            self.user_name.clear()
            self.passwords.clear()
        else:
            QMessageBox.warning(self.centralwidget, "Error", "All fields are required!")

    def generate_password(self):
        strength = self.pass_strngth.currentText()
        password = self.create_password(strength)
        self.lineEdit.setText(password)

    def create_password(self, strength):
        length = int(self.pass_length.text())
        if strength == "Weak":
            chars = "abcdefghijklmnopqrstuvwxyz"
        elif strength == "medium":
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        else:
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        return ''.join(random.choice(chars) for _ in range(length))

    def refresh_table(self):
        self.password_tabel.setRowCount(0)
        for i, data in enumerate(password_list):
            self.password_tabel.insertRow(i)
            for j, field in enumerate(data):
                self.password_tabel.setItem(i, j, QTableWidgetItem(field))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.passkeeper_btn.setText(_translate("MainWindow", "Password Keeper"))
        self.passgenarator_btn.setText(_translate("MainWindow", "Password genarator"))
        self.viewpass_btn.setText(_translate("MainWindow", "view Passwords"))
        self.settings_btn.setText(_translate("MainWindow", "Settings"))
        self.wn_label.setText(_translate("MainWindow", "Website Name"))
        self.usr_n_label.setText(_translate("MainWindow", "User Name"))
        self.pass_label.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Add Password"))
        self.pass_len_label.setText(_translate("MainWindow", "Password length"))
        self.pass_strngth.setItemText(0, _translate("MainWindow", "Weak"))
        self.pass_strngth.setItemText(1, _translate("MainWindow", "medium"))
        self.pass_strngth.setItemText(2, _translate("MainWindow", "Strong"))
        self.pass_strn_label.setText(_translate("MainWindow", "Password strength"))
        self.gnrt_pass_btn.setText(_translate("MainWindow", "Genarate Password"))
        self.label_3.setText(_translate("MainWindow", "Password Genarator"))
        self.label_4.setText(_translate("MainWindow", "Genarated Password:"))
        self.header.setText(_translate("MainWindow", "View Password"))
        item = self.password_tabel.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.password_tabel.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Website"))
        item = self.password_tabel.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Password"))
        self.pushButton_3.setText(_translate("MainWindow", "Refresh Table"))
        self.theme.setItemText(0, _translate("MainWindow", "Default"))
        self.theme.setItemText(1, _translate("MainWindow", "Dark"))
        self.theme.setItemText(2, _translate("MainWindow", "Elegant Blue"))
        self.theme.setItemText(3, _translate("MainWindow", "Modern Purple"))
        self.theme.setItemText(4, _translate("MainWindow", "Forest Green"))
        self.theme.setItemText(5, _translate("MainWindow", "Sunset"))
        self.theme_label.setText(_translate("MainWindow", "Theme"))
        self.backup_btn.setText(_translate("MainWindow", "BackUp Data"))
        self.restr_btn.setText(_translate("MainWindow", "Restore Data"))
        self.pushButton_2.setText(_translate("MainWindow", "add theme"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
