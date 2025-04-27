from PyQt5.QtWidgets import QMainWindow
from module.UI.bookmark_transfer import BookmarkTransferApp

class BookmarkTransferWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = BookmarkTransferApp()
        self.ui.init_ui(self)
