from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import assistant_details
from input_module import *
import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc

os.system("CLS")
global i,o
i=""
o=""

global MainWindow

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(453, 652)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(150, 550, 150, 50))


        # user
        # self.button3 = QtWidgets.QPushButton(self.centralwidget)
        # self.button3.setGeometry(QtCore.QRect(50, 100, 500, 100))
        # user = b
        # assistant = button4
        # speck=button2

        # assistant
        self.button4 = QtWidgets.QLineEdit(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(0, 255, 400, 100))

        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.button2.setFont(font)
        self.button2.setAutoFillBackground(False)
        self.button2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button2.setAutoDefault(False)
        self.button2.setDefault(False)
        self.button2.setFlat(False)
        self.button2.setObjectName("button2")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(-30, 0, 481, 71))
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(400, 35, 500, 100))
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(0, 190, 500, 100))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(24)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label1.setFont(font)
        self.label1.setAutoFillBackground(False)
        self.label1.setTextFormat(QtCore.Qt.AutoText)
        self.label1.setScaledContents(False)
        self.label1.setObjectName("label1")

        # self.label = QtWidgets.QLabel(self.centralwidget)
        # self.label.setGeometry(QtCore.QRect(0, 0, 451, 481))
        # self.label.setText("")
        # self.label.setPixmap(QtGui.QPixmap("jpg2png/VA2.png"))
        # self.label.setScaledContents(True)
        # self.label.setObjectName("label")


        font1 = QtGui.QFont()
        font1.setFamily("Calibri")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(40)

        self.label2.setFont(font1)
        self.label2.setAutoFillBackground(False)
        self.label2.setTextFormat(QtCore.Qt.AutoText)
        self.label2.setScaledContents(False)
        self.label2.setObjectName("label2")

        font2 = QtGui.QFont()
        font2.setFamily("Calibri")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(20)
        self.label3.setFont(font1)
        self.label3.setAutoFillBackground(False)
        self.label3.setTextFormat(QtCore.Qt.AutoText)
        self.label3.setScaledContents(False)
        self.label3.setObjectName("label3")

        # text box
        # self.button3.setFont(font2)
        # self.button3.setAutoFillBackground(False)
        # self.button3.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.button3.setAutoDefault(False)
        # self.button3.setDefault(False)
        # self.button3.setFlat(False)
        # self.button3.setObjectName("button3")

        self.button4.setFont(font2)

        self.button4.setAutoFillBackground(False)
        self.button4.setStyleSheet("border :1px solid ;")


        font3 = QtGui.QFont()
        font3.setFamily("Calibri")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(20)
        self.button4.setFont(font3)
        self.b = QtWidgets.QLineEdit(self.centralwidget)
        self.b.setGeometry(QtCore.QRect(50, 100, 500, 100))
        self.b.setStyleSheet("border :1px solid ;")
        self.b.setFont(font3)

        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(14)

        # self.label.raise_()
        self.label1.raise_()
        self.button2.raise_()
        # self.button3.raise_()
        self.button4.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 453, 22))
        self.menubar.setObjectName("menubar")
        self.menuFILE = QtWidgets.QMenu(self.menubar)
        self.menuFILE.setObjectName("menuFILE")
        self.menuEDIT = QtWidgets.QMenu(self.menubar)
        self.menuEDIT.setObjectName("menuEDIT")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFILE.menuAction())
        self.menubar.addAction(self.menuEDIT.menuAction())


        
        self.button2.clicked.connect(self.taking_input)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        global i,o
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VOICE ASSISTANT"))
        self.button2.setText(_translate("MainWindow", "SPEAK"))
        self.label1.setText(_translate("MainWindow", "               B.R.A.V.O"))
        self.label2.setText(_translate("MainWindow", "User"))
        self.label3.setText(_translate("MainWindow", "Assistant"))



    def taking_input(self):
        global i, o, MainWindow
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VOICE ASSISTANT"))
        #from input_module import take_input,App
        from process_module import process
        from output_module import give_output
        from database import speak_is_on
        i = take_input(self)
        # self.button3.setText(_translate("MainWindow", i))
        self.b.setText(_translate("MainWindow", i))

        o = process(self,i)
        if o=='0':
            o="Sorry, Could not recognize the command."
        self.button4.setText(_translate("MainWindow", o))
        give_output(o)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
