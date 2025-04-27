from PyQt5.QtWidgets import QMainWindow
from module.UI.system_password import sys_ui

class SystemPasswordWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = sys_ui()
        self.ui.setupUi(self)
