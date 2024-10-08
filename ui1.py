from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
import sys

class Ui_MainWindow_Start(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("UPT")


        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.btn_start = QtWidgets.QPushButton("Розпочати",self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(328, 490, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_start.setFont(font)
        self.btn_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_start.setCheckable(False)
        self.btn_start.setObjectName("btn_start")


        self.lb_name = QtWidgets.QLabel("Universal Personal Tutor",self.centralwidget)
        self.lb_name.setGeometry(QtCore.QRect(240, 80, 308, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lb_name.setFont(font)
        self.lb_name.setObjectName("lb_name")


        self.lb_text1 = QtWidgets.QLabel("Програма розроблена лише в цілях навчання", self.centralwidget)
        self.lb_text1.setEnabled(True)
        self.lb_text1.setGeometry(QtCore.QRect(150, 160, 526, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_text1.setFont(font)
        self.lb_text1.setObjectName("lb__text1")


        self.lb_text2 = QtWidgets.QLabel("Не потрібна сприймати серйозно все що видає програма", self.centralwidget)
        self.lb_text2.setEnabled(True)
        self.lb_text2.setGeometry(QtCore.QRect(80, 270, 662, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_text2.setFont(font)
        self.lb_text2.setObjectName("lb_text2")


        self.lb_text3 = QtWidgets.QLabel("Всі курси використовувати лише в цілях загального розвитку", self.centralwidget)
        self.lb_text3.setEnabled(True)
        self.lb_text3.setGeometry(QtCore.QRect(50, 390, 709, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_text3.setFont(font)
        self.lb_text3.setObjectName("lb_text3")


        self.lb_in_name = QtWidgets.QLabel("Введіть Ваше ім\'я", self.centralwidget)
        self.lb_in_name.setEnabled(True)
        self.lb_in_name.setGeometry(QtCore.QRect(80, 190, 202, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_in_name.setFont(font)
        self.lb_in_name.setObjectName("lb_in_name")


        self.lb_in_age = QtWidgets.QLabel("Введіть Ваш вік", self.centralwidget)
        self.lb_in_age.setEnabled(True)
        self.lb_in_age.setGeometry(QtCore.QRect(80, 260, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_in_age.setFont(font)
        self.lb_in_age.setObjectName("lb_in_age")


        self.lb_in_course = QtWidgets.QLabel("Введіть назву курсу", self.centralwidget)
        self.lb_in_course.setEnabled(True)
        self.lb_in_course.setGeometry(QtCore.QRect(80, 330, 227, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_in_course.setFont(font)
        self.lb_in_course.setObjectName("lb_in_course")


        self.le_name = QtWidgets.QLineEdit(self.centralwidget)
        self.le_name.setEnabled(True)
        self.le_name.setGeometry(QtCore.QRect(320, 190, 291, 31))
        self.le_name.setObjectName("le_name")


        self.le_age = QtWidgets.QLineEdit(self.centralwidget)
        self.le_age.setEnabled(True)
        self.le_age.setGeometry(QtCore.QRect(320, 260, 291, 31))
        self.le_age.setObjectName("le_age")


        self.le_course = QtWidgets.QLineEdit(self.centralwidget)
        self.le_course.setEnabled(True)
        self.le_course.setGeometry(QtCore.QRect(320, 330, 291, 31))
        self.le_course.setObjectName("le_corse")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")


        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Start()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())