import shutil
import os
from PyQt5 import QtWidgets, QtGui, QtCore

# Paths where browsers store bookmarks
BOOKMARK_PATHS = {
    "Google Chrome": os.path.expanduser("~") + "/AppData/Local/Google/Chrome/User Data/Default/Bookmarks",
    "Mozilla Firefox": os.path.expanduser("~") + "/AppData/Roaming/Mozilla/Firefox/Profiles/",
    "Microsoft Edge": os.path.expanduser("~") + "/AppData/Local/Microsoft/Edge/User Data/Default/Bookmarks",
    "Opera": os.path.expanduser("~") + "/AppData/Roaming/Opera Software/Opera Stable/Bookmarks",
    "Brave": os.path.expanduser("~") + "/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/Bookmarks",
}

class BookmarkTransferApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Bookmark Transfer")
        self.setGeometry(100, 100, 400, 250)
        self.setStyleSheet("background-color: #f8f9fa;")

        self.title_label = QtWidgets.QLabel("Transfer Bookmarks", self)
        self.title_label.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setStyleSheet("color: #333;")

        self.source_label = QtWidgets.QLabel("Source Browser:")
        self.source_browser = QtWidgets.QComboBox()
        self.source_browser.addItems(BOOKMARK_PATHS.keys())

        self.dest_label = QtWidgets.QLabel("Destination Browser:")
        self.dest_browser = QtWidgets.QComboBox()
        self.dest_browser.addItems(BOOKMARK_PATHS.keys())

        self.transfer_button = QtWidgets.QPushButton("Transfer Bookmarks")
        self.transfer_button.setStyleSheet("background-color: #007bff; color: white; padding: 8px; border-radius: 5px;")
        self.transfer_button.clicked.connect(self.transfer_bookmarks)

        self.status_label = QtWidgets.QLabel("")
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setStyleSheet("color: green;")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.source_label)
        layout.addWidget(self.source_browser)
        layout.addWidget(self.dest_label)
        layout.addWidget(self.dest_browser)
        layout.addWidget(self.transfer_button)
        layout.addWidget(self.status_label)
        self.setLayout(layout)

    def transfer_bookmarks(self):
        """Transfers bookmarks from the source browser to the destination browser."""
        src_browser = self.source_browser.currentText()
        dest_browser = self.dest_browser.currentText()

        if src_browser == dest_browser:
            self.status_label.setText("Source and destination cannot be the same!")
            self.status_label.setStyleSheet("color: red;")
            return

        src_path = BOOKMARK_PATHS.get(src_browser)
        dest_path = BOOKMARK_PATHS.get(dest_browser)

        if not os.path.exists(src_path):
            self.status_label.setText(f"Error: No bookmarks found for {src_browser}.")
            self.status_label.setStyleSheet("color: red;")
            return

        # If destination bookmark file exists, create a backup
        if os.path.exists(dest_path):
            backup_path = dest_path + ".backup"
            shutil.copy(dest_path, backup_path)

        try:
            shutil.copy(src_path, dest_path)
            self.status_label.setText(f"Bookmarks transferred from {src_browser} to {dest_browser} successfully!")
            self.status_label.setStyleSheet("color: green;")
        except Exception as e:
            self.status_label.setText(f"Failed to transfer: {str(e)}")
            self.status_label.setStyleSheet("color: red;")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = BookmarkTransferApp()
    window.show()
    sys.exit(app.exec_())
