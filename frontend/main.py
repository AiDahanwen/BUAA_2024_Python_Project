from login import *
from Modify_Person import *
from signup import *
from find_password import *
from add_task import *
from main_interface import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
import sys

user_now = ''


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win = None
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        # 消除边框
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        '''
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(0, 0)
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(QtCore.Qt.black)
        self.ui.frame.setGraphicsEffect(self.shadow)
        
        self.ui.pushButton_login.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.pushButton_register.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))
        self.ui.pushButton_L_sure.clicked.connect(lambda: self.login_in())
        '''
        self.ui.pushButton_L_signup.clicked.connect(lambda: self.sign_up())
        self.ui.pushButton_L_forget.clicked.connect(lambda: self.forget_password())

        self.show()

    '''
    def login_in(self):
        account = self.ui.lineEdit_L_account.text()
        password = self.ui.lineEdit_L_password.text()
        if account == 'admin' and password == '123456':
            self.win = MainWindow()
            self.close()
        else:
            print('账号或密码错误！')
    '''

    def sign_up(self):
        self.win = SignupWindow()

    def forget_password(self):
        self.win = FindWindow()


class SignupWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SignupWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton_S_ensure.clicked.connect(lambda: self.close())
        self.ui.label.adjustSize()
        self.ui.pushButton_S_send.adjustSize()
        self.show()


class FindWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FindWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton_F_ensure.clicked.connect(lambda: self.close())
        self.ui.pushButton_F_send.adjustSize()
        self.ui.label.adjustSize()
        self.show()


class AddTaskWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddTaskWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton_A_everyday.clicked.connect(lambda: self.everyday_task())
        self.ui.pushButton_A_ordinary.clicked.connect(lambda: self.ordinary_task())
        self.ui.label.adjustSize()
        self.show()

    def everyday_task(self):
        # 实现每日任务功能
        self.close()

    def ordinary_task(self):
        self.close()


class ModifyPersonWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Modify_Person()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton_P_modify.clicked.connect(self.finish_modify)
        self.show()

    def finish_modify(self):
        self.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win = None
        self.login = None
        self.ui = Ui_Main_interface()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        '''
        self.ui.pushButton_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_web.clicked.connect(self.go_web)
        self.ui.pushButton_me.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_logout.clicked.connect(self.log_out)
        '''
        self.ui.label.adjustSize()
        self.ui.label_2.adjustSize()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.listWidget.itemClicked.connect(lambda: self.change_page(self.ui.listWidget.currentRow()))
        self.ui.listWidget_2.itemClicked.connect(lambda: self.change_page(self.ui.listWidget_2.currentRow() + 3))
        self.ui.pushButton_M_addtask.clicked.connect(lambda: self.add_task())
        self.ui.pushButton_P_modify.clicked.connect(lambda: self.modify_person())
        self.show()

    '''
    def go_web(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.pushButton_bilibili.clicked.connect(lambda: webbrowser.open('https://www.bilibili.com/'))
        self.ui.pushButton_apple.clicked.connect(lambda: webbrowser.open('https://www.apple.com/'))
        self.ui.pushButton_CSDN.clicked.connect(lambda: webbrowser.open('https://www.csdn.net/'))
        self.ui.pushButton_tencent.clicked.connect(lambda: webbrowser.open('https://v.qq.com/'))
    '''

    def change_page(self, index):
        if index == 0:
            self.ui.stackedWidget.setCurrentIndex(1)
        elif index == 1:
            self.ui.stackedWidget.setCurrentIndex(2)
        elif index == 2:
            self.ui.stackedWidget.setCurrentIndex(3)
        elif index == 3:
            self.ui.stackedWidget.setCurrentIndex(4)
        elif index == 4:
            self.log_out()

    def add_task(self):
        self.win = AddTaskWindow()

    def modify_person(self):
        self.win = ModifyPersonWindow()

    def log_out(self):
        global user_now
        self.close()
        self.login = LoginWindow()
        user_now = ''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
