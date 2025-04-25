from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import os
import subprocess

class BrowserDownloaderWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.goggle_label = QtWidgets.QLabel(self.centralwidget)
        self.goggle_label.setGeometry(QtCore.QRect(40, 150, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.goggle_label.setFont(font)
        self.goggle_label.setAlignment(QtCore.Qt.AlignCenter)
        self.goggle_label.setObjectName("goggle_label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 240, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.goggle_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.goggle_label_2.setGeometry(QtCore.QRect(300, 150, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.goggle_label_2.setFont(font)
        self.goggle_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.goggle_label_2.setObjectName("goggle_label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 240, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.goggle_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.goggle_label_3.setGeometry(QtCore.QRect(560, 150, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.goggle_label_3.setFont(font)
        self.goggle_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.goggle_label_3.setObjectName("goggle_label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.download_google_chrome)
        self.pushButton_2.clicked.connect(self.download_bing_browser)
        self.pushButton_3.clicked.connect(self.download_firefox)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.goggle_label.setText(_translate("MainWindow", "Google"))
        self.pushButton.setText(_translate("MainWindow", "Download"))
        self.pushButton_2.setText(_translate("MainWindow", "Download"))
        self.goggle_label_2.setText(_translate("MainWindow", "Bing"))
        self.pushButton_3.setText(_translate("MainWindow", "Download"))
        self.goggle_label_3.setText(_translate("MainWindow", "FireFox"))
    
    def download_and_install(self, url, filename):
        try:
            # Download file
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            chunk_size = 1024
            progress = 0

            with open(filename, "wb") as file:
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    progress += len(data)
                    print(f"Downloading: {progress * 100 // total_size}%")

            # Run installer
            subprocess.run([filename], shell=True)
            QtWidgets.QMessageBox.information(
                None, "Success", f"{filename} downloaded and installer started!"
            )
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Error", f"Failed to download: {str(e)}")

    def download_google_chrome(self):
        url = "https://dl.google.com/chrome/install/standalone/ChromeSetup.exe"
        filename = "ChromeSetup.exe"
        self.download_and_install(url, filename)

    def download_bing_browser(self):
        url = "https://bing.example.com/BingSetup.exe" 
        filename = "BingSetup.exe"
        self.download_and_install(url, filename)

    def download_firefox(self):
        url = "https://download.mozilla.org/?product=firefox-latest&os=win&lang=en-US"
        filename = "FirefoxSetup.exe"
        self.download_and_install(url, filename)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = BrowserDownloaderWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
