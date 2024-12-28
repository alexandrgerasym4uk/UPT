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

        self.btn_start = QtWidgets.QPushButton("Розпочати", self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_start.setFont(font)
        self.btn_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_start.setCheckable(False)
        self.btn_start.setObjectName("btn_start")
        self.btn_start.setFixedSize(161, 61)

        self.btn_continue = QtWidgets.QPushButton("Продовжити", self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_continue.setFont(font)
        self.btn_continue.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_continue.setCheckable(False)
        self.btn_continue.setObjectName("btn_continue")
        self.btn_continue.setFixedSize(161, 61)

        self.btn_key_get = QtWidgets.QPushButton("Отримати ключ", self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_key_get.setFont(font)
        self.btn_key_get.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_key_get.setCheckable(False)
        self.btn_key_get.setObjectName("btn_key_get")
        self.btn_key_get.setFixedSize(200, 61)

        self.btn_key = QtWidgets.QPushButton("Ввести ключ", self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_key.setFont(font)
        self.btn_key.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_key.setCheckable(False)
        self.btn_key.setObjectName("btn_key")
        self.btn_key.setFixedSize(200, 61)

        self.lb_text_key = QtWidgets.QLabel(
            "Для початку перейдіть на сайт та отримайте ключ", self.centralwidget
        )
        self.lb_text_key.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_text_key.setFont(font)
        self.lb_text_key.setObjectName("lb_text_key")
        self.lb_text_key.setFixedSize(600, 30)

        self.lb_in_key = QtWidgets.QLabel("Введіть Ваш ключ", self.centralwidget)
        self.lb_in_key.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_in_key.setFont(font)
        self.lb_in_key.setObjectName("lb_in_key")
        self.lb_in_key.setFixedSize(220, 30)

        self.le_key = QtWidgets.QLineEdit(self.centralwidget)
        self.le_key.setEnabled(True)
        self.le_key.setObjectName("le_key")
        self.le_key.setFixedSize(291, 31)

        self.lb_name = QtWidgets.QLabel("Universal Personal Tutor", self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lb_name.setFont(font)
        self.lb_name.setObjectName("lb_name")
        self.lb_name.setFixedSize(308, 30)

        self.lb_text1 = QtWidgets.QLabel(
            "Програма розроблена лише в цілях навчання", self.centralwidget
        )
        self.lb_text1.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_text1.setFont(font)
        self.lb_text1.setObjectName("lb__text1")
        self.lb_text1.setFixedSize(526, 30)

        self.lb_text2 = QtWidgets.QLabel(
            "Не потрібна сприймати серйозно все що видає програма", self.centralwidget
        )
        self.lb_text2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_text2.setFont(font)
        self.lb_text2.setObjectName("lb_text2")
        self.lb_text2.setFixedSize(662, 30)

        self.lb_text3 = QtWidgets.QLabel(
            "Всі курси використовувати лише в цілях загального розвитку",
            self.centralwidget,
        )
        self.lb_text3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_text3.setFont(font)
        self.lb_text3.setObjectName("lb_text3")
        self.lb_text3.setFixedSize(709, 30)

        self.lb_in_name = QtWidgets.QLabel("Введіть Ваше ім'я", self.centralwidget)
        self.lb_in_name.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_in_name.setFont(font)
        self.lb_in_name.setObjectName("lb_in_name")
        self.lb_in_name.setFixedSize(202, 30)

        self.lb_in_age = QtWidgets.QLabel("Введіть Ваш вік", self.centralwidget)
        self.lb_in_age.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_in_age.setFont(font)
        self.lb_in_age.setObjectName("lb_in_age")
        self.lb_in_age.setFixedSize(180, 30)

        self.lb_in_course = QtWidgets.QLabel("Введіть назву курсу", self.centralwidget)
        self.lb_in_course.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_in_course.setFont(font)
        self.lb_in_course.setObjectName("lb_in_course")
        self.lb_in_course.setFixedSize(227, 30)

        self.le_name = QtWidgets.QLineEdit(self.centralwidget)
        self.le_name.setEnabled(True)
        self.le_name.setObjectName("le_name")
        self.le_name.setFixedSize(291, 31)

        self.le_age = QtWidgets.QLineEdit(self.centralwidget)
        self.le_age.setEnabled(True)
        self.le_age.setObjectName("le_age")
        self.le_age.setFixedSize(291, 31)

        self.le_course = QtWidgets.QLineEdit(self.centralwidget)
        self.le_course.setEnabled(True)
        self.le_course.setObjectName("le_corse")
        self.le_course.setFixedSize(291, 31)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")

        name_layout = QHBoxLayout()
        name_layout.addStretch(15)
        name_layout.addWidget(self.lb_in_name, alignment=QtCore.Qt.AlignCenter)
        name_layout.addWidget(self.le_name, alignment=QtCore.Qt.AlignCenter)
        name_layout.addStretch(15)

        age_layout = QHBoxLayout()
        age_layout.addStretch(15)
        age_layout.addWidget(self.lb_in_age, alignment=QtCore.Qt.AlignCenter)
        age_layout.addWidget(self.le_age, alignment=QtCore.Qt.AlignCenter)
        age_layout.addStretch(15)

        key_layout = QHBoxLayout()
        key_layout.addStretch(15)
        key_layout.addWidget(self.lb_in_key, alignment=QtCore.Qt.AlignCenter)
        key_layout.addWidget(self.le_key, alignment=QtCore.Qt.AlignCenter)
        key_layout.addStretch(15)

        course_layout = QHBoxLayout()
        course_layout.addStretch(15)
        course_layout.addWidget(self.lb_in_course, alignment=QtCore.Qt.AlignCenter)
        course_layout.addWidget(self.le_course, alignment=QtCore.Qt.AlignCenter)
        course_layout.addStretch(15)

        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch(5)
        buttons_layout.addWidget(self.btn_start, alignment=QtCore.Qt.AlignCenter)
        buttons_layout.addWidget(self.btn_continue, alignment=QtCore.Qt.AlignCenter)
        buttons_layout.addStretch(5)

        main_layout = QVBoxLayout(self.centralwidget)
        main_layout.addWidget(self.lb_name, alignment=QtCore.Qt.AlignCenter)
        main_layout.addWidget(self.lb_text_key, alignment=QtCore.Qt.AlignCenter)
        main_layout.addWidget(self.btn_key_get, alignment=QtCore.Qt.AlignCenter)
        main_layout.addWidget(self.lb_text1, alignment=QtCore.Qt.AlignCenter)
        main_layout.addLayout(key_layout)
        main_layout.addLayout(name_layout)
        main_layout.addWidget(self.lb_text2, alignment=QtCore.Qt.AlignCenter)
        main_layout.addLayout(age_layout)
        main_layout.addWidget(self.lb_text3, alignment=QtCore.Qt.AlignCenter)
        main_layout.addLayout(course_layout)
        main_layout.addWidget(self.btn_key, alignment=QtCore.Qt.AlignCenter)
        main_layout.addLayout(buttons_layout)

        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Start()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
