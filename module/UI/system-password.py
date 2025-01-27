from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Setting up the UI
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(310, 10, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        #Title of the window
        self.title.setFont(font)
        self.title.setObjectName("title")

        #List of saved passwords
        self.pass_list = QtWidgets.QListWidget(self.centralwidget)
        self.pass_list.setGeometry(QtCore.QRect(40, 80, 711, 261))
        self.pass_list.setObjectName("pass_list")

        #Button to show the password
        self.show_pass_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_pass_btn.setGeometry(QtCore.QRect(300, 350, 161, 31))
        self.show_pass_btn.setObjectName("show_pass_btn")
        self.tp_label = QtWidgets.QLabel(self.centralwidget)
        self.tp_label.setGeometry(QtCore.QRect(300, 390, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        #Transfer Password Label
        self.tp_label.setFont(font)
        self.tp_label.setObjectName("tp_label")
        self.sb_label = QtWidgets.QLabel(self.centralwidget)
        self.sb_label.setGeometry(QtCore.QRect(30, 450, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        #Source Browser Label
        self.sb_label.setFont(font)
        self.sb_label.setObjectName("sb_label")
        self.tb_label = QtWidgets.QLabel(self.centralwidget)
        self.tb_label.setGeometry(QtCore.QRect(20, 520, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        #Target Browser Label
        self.tb_label.setFont(font)
        self.tb_label.setObjectName("tb_label")

        #Source Browser ComboBox
        self.src_brwser = QtWidgets.QComboBox(self.centralwidget)
        self.src_brwser.setGeometry(QtCore.QRect(200, 470, 161, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.src_brwser.setFont(font)
        self.src_brwser.setObjectName("src_brwser")
        self.src_brwser.addItem("")
        self.src_brwser.addItem("")
        self.src_brwser.addItem("")
        self.src_brwser.addItem("")

        #Target Browser ComboBox
        self.trgt_brwser = QtWidgets.QComboBox(self.centralwidget)
        self.trgt_brwser.setGeometry(QtCore.QRect(190, 540, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.trgt_brwser.setFont(font)
        self.trgt_brwser.setObjectName("trgt_brwser")
        self.trgt_brwser.addItem("")
        self.trgt_brwser.addItem("")
        self.trgt_brwser.addItem("")
        self.trgt_brwser.addItem("")

        #Transfer Password Button
        self.trnsfr_pass_btn = QtWidgets.QPushButton(self.centralwidget)
        self.trnsfr_pass_btn.setGeometry(QtCore.QRect(440, 500, 161, 31))
        self.trnsfr_pass_btn.setObjectName("trnsfr_pass_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Saved Password"))
        self.show_pass_btn.setText(_translate("MainWindow", "Show Password"))
        self.tp_label.setText(_translate("MainWindow", "Transfer Password"))
        self.sb_label.setText(_translate("MainWindow", "Source Browser:"))
        self.tb_label.setText(_translate("MainWindow", "Target  Browser:"))
        self.src_brwser.setItemText(0, _translate("MainWindow", "Google Chrome"))
        self.src_brwser.setItemText(1, _translate("MainWindow", "Microsoft Edge"))
        self.src_brwser.setItemText(2, _translate("MainWindow", "Mozilla FireFox"))
        self.src_brwser.setItemText(3, _translate("MainWindow", "Brave"))
        self.trgt_brwser.setItemText(0, _translate("MainWindow", "Google Chrome"))
        self.trgt_brwser.setItemText(1, _translate("MainWindow", "Microsoft Edge"))
        self.trgt_brwser.setItemText(2, _translate("MainWindow", "Mozilla FireFox"))
        self.trgt_brwser.setItemText(3, _translate("MainWindow", "Brave"))
        self.trnsfr_pass_btn.setText(_translate("MainWindow", "Transfer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())