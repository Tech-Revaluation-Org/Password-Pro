from PyQt5.QtWidgets import QMainWindow
from module.UI.password_manager import Ui_MainWindow

class PasswordManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
