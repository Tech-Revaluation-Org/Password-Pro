from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import random
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Database setup
        self.conn = sqlite3.connect('passwords.db')
        self.create_table()

        # Sidebar
        self.sidebar = QtWidgets.QFrame(self.centralwidget)
        self.sidebar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar.setObjectName("sidebar")
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(10, 10, 10, 10)

        # Sidebar Buttons with Icons
        self.passkeeper_btn = QPushButton("Password Keeper", self.sidebar)
        self.passgenarator_btn = QPushButton("Password Generator", self.sidebar)
        self.viewpass_btn = QPushButton("View Passwords", self.sidebar)
        self.settings_btn = QPushButton("Settings", self.sidebar)

        # Add icons to buttons
        self.passkeeper_btn.setIcon(QIcon("icons/keeper.png"))
        self.passgenarator_btn.setIcon(QIcon("icons/generator.png"))
        self.viewpass_btn.setIcon(QIcon("icons/view.png"))
        self.settings_btn.setIcon(QIcon("icons/settings.png"))

        # Add buttons to sidebar layout
        for button in [self.passkeeper_btn, self.passgenarator_btn, self.viewpass_btn, self.settings_btn]:
            button.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); border: None; border-radius: 5px; padding: 10px;")
            self.sidebar_layout.addWidget(button)

        self.sidebar_layout.addStretch()  # Push buttons to the top

        # Stacked Widget
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.stackedWidget.setObjectName("stackedWidget")

        # Password Keeper Page
        self.passwordkeperpage = self.create_password_keeper_page()
        self.stackedWidget.addWidget(self.passwordkeperpage)

        # Password Generator Page
        self.passwordgenaratorpage = self.create_password_generator_page()
        self.stackedWidget.addWidget(self.passwordgenaratorpage)

        # Password View Page
        self.pass_viewpage = self.create_password_view_page()
        self.stackedWidget.addWidget(self.pass_viewpage)

        # Settings Page
        self.settings = self.create_settings_page()
        self.stackedWidget.addWidget(self.settings)

        # Main Layout
        main_layout = QHBoxLayout(self.centralwidget)
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        # Connect buttons to change pages
        self.passkeeper_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.passgenarator_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.viewpass_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.settings_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                website TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def create_password_keeper_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        self.wn_label = QLabel("Website Name")
        self.website_name = QLineEdit()
        self.user_name = QLineEdit()
        self.usr_n_label = QLabel("User  Name")
        self.pass_label = QLabel("Password")
        self.passwords = QLineEdit()
        self.pushButton = QPushButton("Add Password")
        self.crack_time_label = QLabel("Estimated Crack Time: ")

        # Set styles
        for widget in [self.website_name, self.user_name, self.passwords]:
            widget.setStyleSheet("color: rgb(51, 51, 51); border: 2px solid #DDDDDD; border-radius: 5px; padding: 10px;")

        self.pushButton.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); border: None; border-radius: 5px; padding: 10px;")
        self.pushButton.clicked.connect(self.save_password)

        layout.addWidget(self.wn_label)
        layout.addWidget(self.website_name)
        layout.addWidget(self.usr_n_label)
        layout.addWidget(self.user_name)
        layout.addWidget(self.pass_label)
        layout.addWidget(self.passwords)
        layout.addWidget(self.pushButton)
        layout.addWidget(self.crack_time_label)

        return page

    def create_password_generator_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        self.pass_len_label = QLabel("Password Length")
        self.pass_length = QLineEdit()
        self.pass_strngth = QComboBox()
        self.pass_strngth.addItems(["Weak", "Medium", "Strong"])
        self.pass_strn_label = QLabel("Password Strength")
        self.gnrt_pass_btn = QPushButton("Generate Password")
        self.lineEdit = QLineEdit()
        self.label_4 = QLabel("Generated Password:")
        self.crack_time_gen_label = QLabel("Estimated Crack Time: ")

        # Set styles
        for widget in [self.pass_length, self.lineEdit]:
            widget.setStyleSheet("color: rgb(51, 51, 51); border: 2px solid #DDDDDD; border-radius: 5px; padding: 10px;")

        self.gnrt_pass_btn.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); border: None; border-radius: 5px; padding: 10px;")
        self.gnrt_pass_btn.clicked.connect(self.generate_password)

        layout.addWidget(self.pass_len_label)
        layout.addWidget(self.pass_length)
        layout.addWidget(self.pass_strn_label)
        layout.addWidget(self.pass_strngth)
        layout.addWidget(self.gnrt_pass_btn)
        layout.addWidget(self.label_4)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.crack_time_gen_label)

        return page

    def create_password_view_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        self.header = QLabel("View Passwords")
        self.password_tabel = QTableWidget()
        self.password_tabel.setColumnCount(3)
        self.password_tabel.setHorizontalHeaderLabels(["Website", "Username", "Password"])
        self.password_tabel.setRowCount(0)

        self.pushButton_3 = QPushButton("Refresh Table")
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); border: None; border-radius: 5px; padding: 10px;")
        self.pushButton_3.clicked.connect(self.refresh_table)

        layout.addWidget(self.header)
        layout.addWidget(self.password_tabel)
        layout.addWidget(self.pushButton_3)

        return page

    def create_settings_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        self.theme_label = QLabel("Theme")
        self.theme = QComboBox()
        self.theme.addItems(["Default", "Dark", "Elegant Blue", "Modern Purple", "Forest Green", "Sunset"])
        self.theme.currentIndexChanged.connect(self.change_theme)
        self.backup_btn = QPushButton("Backup Data")
        self.restr_btn = QPushButton("Restore Data")

        # Set styles
        for button in [self.backup_btn, self.restr_btn]:
            button.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); border: None; border-radius: 5px; padding: 10px;")

        layout.addWidget(self.theme_label)
        layout.addWidget(self.theme)
        layout.addWidget(self.backup_btn)
        layout.addWidget(self.restr_btn)

        return page

    def save_password(self):
        website = self.website_name.text().strip()
        username = self.user_name.text().strip()
        password = self.passwords.text().strip()

        if website and username and password:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)", (website, username, password))
            self.conn.commit()
            QMessageBox.information(self.centralwidget, "Success", "Password saved successfully!")
            self.website_name.clear()
            self.user_name.clear()
            self.passwords.clear()
            self.update_crack_time(password)  # Update crack time for saved password
        else:
            QMessageBox.warning(self.centralwidget, "Error", "All fields are required!")

    def generate_password(self):
        strength = self.pass_strngth.currentText()
        password = self.create_password(strength)
        self.lineEdit.setText(password)
        self.update_crack_time(password)  # Update crack time for generated password

    def create_password(self, strength):
        length = int(self.pass_length.text())
        if strength == "Weak":
            chars = "abcdefghijklmnopqrstuvwxyz"
        elif strength == "Medium":
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        else:
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        return ''.join(random.choice(chars) for _ in range(length))

    def refresh_table(self):
        self.password_tabel.setRowCount(0)
        cursor = self.conn.cursor()
        cursor.execute("SELECT website, username, password FROM passwords")
        for i, (website, username, password) in enumerate(cursor.fetchall()):
            self.password_tabel.insertRow(i)
            self.password_tabel.setItem(i, 0, QTableWidgetItem(website))
            self.password_tabel.setItem(i, 1, QTableWidgetItem(username))
            self.password_tabel.setItem(i, 2, QTableWidgetItem(password))

    def change_theme(self):
        theme = self.theme.currentText()
        if theme == "Default":
            self.set_default_theme()
        elif theme == "Dark":
            self.set_dark_theme()
        elif theme == "Elegant Blue":
            self.set_elegant_blue_theme()
        elif theme == "Modern Purple":
            self.set_modern_purple_theme()
        elif theme == "Forest Green":
            self.set_forest_green_theme()
        elif theme == "Sunset":
            self.set_sunset_theme()

    def set_default_theme(self):
        self.set_style("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")

    def set_dark_theme(self):
        self.set_style("background-color: rgb(30, 30, 30); color: rgb(255, 255, 255);")

    def set_elegant_blue_theme(self):
        self.set_style("background-color: rgb(0, 123, 255); color: rgb(255, 255, 255);")

    def set_modern_purple_theme(self):
        self.set_style("background-color: rgb(128, 0, 128); color: rgb(255, 255, 255);")

    def set_forest_green_theme(self):
        self.set_style("background-color: rgb(34, 139, 34); color: rgb(255, 255, 255);")

    def set_sunset_theme(self):
        self.set_style("background-color: rgb(255, 94, 77); color: rgb(255, 255, 255);")

    def set_style(self, style):
        self.centralwidget.setStyleSheet(style)
        self.sidebar.setStyleSheet(style)
        for button in [self.passkeeper_btn, self.passgenarator_btn, self.viewpass_btn, self.settings_btn]:
            button.setStyleSheet(style + "border: None; border-radius: 5px; padding: 10px;")
        self.stackedWidget.setStyleSheet(style)

    def update_crack_time(self, password):
        crack_time = self.calculate_crack_time(password)
        self.crack_time_label.setText(f"Estimated Crack Time: {crack_time}")

    def calculate_crack_time(self, password):
        length = len(password)
        if password.isdigit():  # Numeric password
            total_combinations = 10 ** length
        else:
            # Define character sets
            lower = 26
            upper = 26
            digits = 10
            special = 10

            # Determine the character set used
            char_set = lower  # Start with lowercase
            if any(c.isupper() for c in password):
                char_set += upper
            if any(c.isdigit() for c in password):
                char_set += digits
            if any(c in "!@#$%^&*()" for c in password):
                char_set += special

            # Calculate total combinations
            total_combinations = char_set ** length

        # Define cracking speed (1 billion guesses per second)
        cracking_speed = 1_000_000_000

        # Calculate crack time in seconds
        crack_time_seconds = total_combinations / cracking_speed

        # Convert to more understandable units
        if crack_time_seconds < 60:
            return f"{crack_time_seconds:.2f} seconds"
        elif crack_time_seconds < 3600:
            return f"{(crack_time_seconds / 60):.2f} minutes"
        elif crack_time_seconds < 86400:
            return f"{(crack_time_seconds / 3600):.2f} hours"
        elif crack_time_seconds < 31536000:
            return f"{(crack_time_seconds / 86400):.2f} days"
        else:
            return f"{(crack_time_seconds / 31536000):.2f} years"

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Manager"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
