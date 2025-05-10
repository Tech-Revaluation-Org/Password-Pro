from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from module.Windows.password_manager_window import PasswordManagerWindow
from module.Windows.browser_downloader_window import BrowserDownloaderWindow
from module.Windows.bookmark_transfer_window import BookmarkTransferApp
from module.UI.bookmark_transfer import BookmarkTransferApp
from module.Windows.system_password_window import SystemPasswordWindow

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("PasswordPro - Dashboard")
        self.setGeometry(500, 200, 400, 300)

        self.label = QLabel("Choose a Feature:")
        self.pm_btn = QPushButton("Password Manager")
        self.bd_btn = QPushButton("Browser Downloader")
        self.bt_btn = QPushButton("Bookmark Transfer")
        self.sp_btn = QPushButton("System Passwords")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.pm_btn)
        layout.addWidget(self.bd_btn)
        layout.addWidget(self.bt_btn)
        layout.addWidget(self.sp_btn)
        self.setLayout(layout)

        self.pm_btn.clicked.connect(self.open_password_manager)
        self.bd_btn.clicked.connect(self.open_browser_downloader)
        self.bt_btn.clicked.connect(self.open_bookmark_transfer)
        self.sp_btn.clicked.connect(self.open_system_passwords)

    def open_password_manager(self):
        self.pm_win = PasswordManagerWindow()
        self.pm_win.show()

    def open_browser_downloader(self):
        self.bd_win = BrowserDownloaderWindow()
        self.bd_win.show()

    def open_bookmark_transfer(self):
        self.bt_win = BookmarkTransferApp()
        self.bt_win.show()

    def open_system_passwords(self):
        self.sp_win = SystemPasswordWindow()
        self.sp_win.show()

    def closeEvent(self, event):
        event.accept()
        self.close()
