from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

class Ui_MainWindow_Main(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1343, 808)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle("UPT")


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.btn_day_1 = QtWidgets.QPushButton("1", self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_day_1.setFont(font)
        self.btn_day_1.setObjectName("btn_day_1")
        self.btn_day_1.setFixedSize(93, 28)


        self.btn_day_2 = QtWidgets.QPushButton("2", self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_day_2.setFont(font)
        self.btn_day_2.setObjectName("btn_day_2")
        self.btn_day_2.setFixedSize(93, 28)


        self.btn_day_3 = QtWidgets.QPushButton("3", self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_day_3.setFont(font)
        self.btn_day_3.setObjectName("btn_day_3")
        self.btn_day_3.setFixedSize(93, 28)


        self.btn_day_4 = QtWidgets.QPushButton("4", self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_day_4.setFont(font)
        self.btn_day_4.setObjectName("btn_day_4")
        self.btn_day_4.setFixedSize(93, 28)


        self.btn_day_5 = QtWidgets.QPushButton("5", self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_day_5.setFont(font)
        self.btn_day_5.setObjectName("btn_day_5")
        self.btn_day_5.setFixedSize(93, 28)


        self.lb_num_day = QtWidgets.QLabel("", self.centralwidget)
        self.lb_num_day.setObjectName("lb_num_day")
        self.lb_num_day.setFixedSize(90, 30)


        self.lb_text1 = QtWidgets.QLabel("Теоретичні відомості", self.centralwidget)
        self.lb_text1.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_text1.setObjectName("lb_text1")
        self.lb_text1.setFixedSize(1321, 30)


        self.tb_theory = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb_theory.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tb_theory.setObjectName("tb_theory")
        self.tb_theory.setFixedSize(1301, 311)


        self.lb_text2 = QtWidgets.QLabel("Практичні завдання", self.centralwidget)
        self.lb_text2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_text2.setObjectName("lb_text2")
        self.lb_text2.setFixedSize(1301, 30)


        self.te_answer = QtWidgets.QTextEdit(self.centralwidget)
        self.te_answer.setObjectName("te_answer")
        self.te_answer.setText("Відповідь:")
        self.te_answer.setFixedSize(621, 171)


        self.tb_task = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb_task.setObjectName("tb_task")
        self.tb_task.setText("Завдання:")
        self.tb_task.setFixedSize(621, 171)


        self.btn_send = QtWidgets.QPushButton("Надіслати завдання", self.centralwidget)
        self.btn_send.setObjectName("btn_send")
        self.btn_send.setFixedSize(249, 39)

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Розміщення елементів
        main_layout = QVBoxLayout(self.centralwidget)
        main_layout.addStretch(5)
        #кнопки днів
        buttons_days = QHBoxLayout()
        buttons_days.addStretch(1)
        buttons_days.addWidget(self.lb_num_day, alignment=QtCore.Qt.AlignCenter)
        buttons_days.addStretch(9)
        buttons_days.addWidget(self.btn_day_1, alignment=QtCore.Qt.AlignCenter)
        buttons_days.addStretch(1)
        buttons_days.addWidget(self.btn_day_2, alignment=QtCore.Qt.AlignCenter)
        buttons_days.addStretch(1)
        buttons_days.addWidget(self.btn_day_3, alignment=QtCore.Qt.AlignCenter)
        buttons_days.addStretch(1)
        buttons_days.addWidget(self.btn_day_4, alignment=QtCore.Qt.AlignCenter)
        buttons_days.addStretch(1)
        buttons_days.addWidget(self.btn_day_5, alignment=QtCore.Qt.AlignCenter)
        buttons_days.addStretch(14)
        main_layout.addLayout(buttons_days)
        main_layout.addStretch(1)

        main_layout.addStretch(1)
        main_layout.addWidget(self.lb_text1, alignment=QtCore.Qt.AlignCenter)
        main_layout.addStretch(1)
        main_layout.addWidget(self.tb_theory, alignment=QtCore.Qt.AlignCenter)
        main_layout.addStretch(1)
        main_layout.addWidget(self.lb_text2, alignment=QtCore.Qt.AlignCenter)
        main_layout.addStretch(1)

        practical_layout = QHBoxLayout()
        practical_layout.addWidget(self.tb_task, alignment=QtCore.Qt.AlignCenter)
        practical_layout.addWidget(self.te_answer, alignment=QtCore.Qt.AlignCenter)

        main_layout.addLayout(practical_layout)
        main_layout.addStretch(3)
        main_layout.addWidget(self.btn_send, alignment=QtCore.Qt.AlignCenter)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        




# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow_Main()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
