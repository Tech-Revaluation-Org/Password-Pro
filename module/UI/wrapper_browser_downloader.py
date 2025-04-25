from PyQt5.QtWidgets import QMainWindow
from module.UI.browser_install import BrowserDownloader  # or whatever class you have

class BrowserDownloaderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = BrowserDownloader()
        self.ui.setupUi(self)