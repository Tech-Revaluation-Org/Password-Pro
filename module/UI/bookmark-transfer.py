from PyQt5 import QtWidgets, QtGui, QtCore

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
        self.source_browser.addItems(["Google Chrome", "Mozilla Firefox", "Microsoft Edge", "Opera", "Brave"])

        self.dest_label = QtWidgets.QLabel("Destination Browser:")
        self.dest_browser = QtWidgets.QComboBox()
        self.dest_browser.addItems(["Google Chrome", "Mozilla Firefox", "Microsoft Edge", "Opera", "Brave"])

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = BookmarkTransferApp()
    window.show()
    sys.exit(app.exec_())
