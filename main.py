from PyQt5.QtWidgets import QApplication
from Dashboard import Dashboard

if __name__ == "__main__":
    app = QApplication([])
    window = Dashboard()
    window.show()
    app.exec_()