from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Main(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1343, 808)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.btn_day_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_day_1.setGeometry(QtCore.QRect(380, 40, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_day_1.setFont(font)
        self.btn_day_1.setObjectName("btn_day_1")


        self.btn_day_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_day_2.setGeometry(QtCore.QRect(500, 40, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_day_2.setFont(font)
        self.btn_day_2.setObjectName("btn_day_2")


        self.btn_day_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_day_3.setGeometry(QtCore.QRect(620, 40, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_day_3.setFont(font)
        self.btn_day_3.setObjectName("btn_day_3")


        self.btn_day_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_day_4.setGeometry(QtCore.QRect(740, 40, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_day_4.setFont(font)
        self.btn_day_4.setObjectName("btn_day_4")


        self.btn_day_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_day_5.setGeometry(QtCore.QRect(860, 40, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_day_5.setFont(font)
        self.btn_day_5.setObjectName("btn_day_5")


        self.lb_num_day = QtWidgets.QLabel(self.centralwidget)
        self.lb_num_day.setGeometry(QtCore.QRect(30, 40, 90, 30))
        self.lb_num_day.setObjectName("lb_num_day")


        self.lb_theme = QtWidgets.QLabel(self.centralwidget)
        self.lb_theme.setGeometry(QtCore.QRect(480, 130, 55, 16))
        self.lb_theme.setText("")
        self.lb_theme.setObjectName("lb_theme")


        self.lb_text1 = QtWidgets.QLabel(self.centralwidget)
        self.lb_text1.setGeometry(QtCore.QRect(10, 100, 1321, 30))
        self.lb_text1.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_text1.setObjectName("lb_text1")


        self.tb_theory = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb_theory.setGeometry(QtCore.QRect(20, 140, 1301, 311))
        self.tb_theory.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tb_theory.setObjectName("tb_theory")


        self.lb_text2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_text2.setGeometry(QtCore.QRect(20, 470, 1301, 30))
        self.lb_text2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_text2.setObjectName("lb_text2")


        self.te_answer = QtWidgets.QTextEdit(self.centralwidget)
        self.te_answer.setGeometry(QtCore.QRect(700, 520, 621, 171))
        self.te_answer.setObjectName("te_answer")


        self.tb_task = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb_task.setGeometry(QtCore.QRect(20, 520, 621, 171))
        self.tb_task.setObjectName("tb_task")


        self.btn_send = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send.setGeometry(QtCore.QRect(550, 710, 249, 39))
        self.btn_send.setObjectName("btn_send")

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UPT"))
        self.btn_day_1.setText(_translate("MainWindow", "1"))
        self.btn_day_2.setText(_translate("MainWindow", "2"))
        self.btn_day_3.setText(_translate("MainWindow", "3"))
        self.btn_day_4.setText(_translate("MainWindow", "4"))
        self.btn_day_5.setText(_translate("MainWindow", "5"))
        self.lb_num_day.setText(_translate("MainWindow", ""))
        self.lb_text1.setText(_translate("MainWindow", "Теоретичні відомості"))
        self.lb_text2.setText(_translate("MainWindow", "Практичні завдання"))
        self.tb_task.setText("Завдання:")
        self.te_answer.setText("Відповідь:")
        self.btn_send.setText(_translate("MainWindow", "Надіслати завдання"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
