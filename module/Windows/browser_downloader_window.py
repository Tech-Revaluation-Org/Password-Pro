from PyQt5.QtWidgets import QMainWindow
from module.UI.browser_install import BrowserDownloaderWindow as BDW_UI  # Renamed to avoid name clash

class BrowserDownloaderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = BDW_UI()
        self.ui.setupUi(self)
