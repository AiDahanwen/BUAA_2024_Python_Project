from PyQt5.QtCore import QObject, QUrl, pyqtSlot
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore

from frontend.login_new import *
from frontend.Modify_Person import *
from frontend.signup import *
from frontend.find_password import *
from frontend.add_task import *
from frontend.main_interface import *
from frontend.free_time import *

from backend.daily_sentence import *
from backend.send_email_code import *
from backend.user_system import *
from backend.task_system import *

import sys

user_now = "2895227477@qq.com"


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win = None
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        # 消除边框
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.stackedWidget_2.setCurrentIndex(0)

        self.ui.pushButton_L_signup.clicked.connect(lambda: self.sign_up())
        self.ui.pushButton_L_forget.clicked.connect(lambda: self.forget_password())
        self.ui.pushButton_L_login.clicked.connect(lambda: self.login_in())

        # 每日一句功能
        self.ui.label_L_daily_sentence.setText(get_sentence()[0])

        self.show()

    def login_in(self):
        account = self.ui.lineEdit_L_account.text()
        password = self.ui.lineEdit_L_password.text()
        # 下面需要三个判断：账号是否为空，密码是否为空，账号密码是否正确
        # 页面跳转：登录成功后跳转到主界面
        if account == '' or password == '':
            self.ui.stackedWidget_2.setCurrentIndex(1)
        elif not is_valid_email(account):
            self.ui.stackedWidget_2.setCurrentIndex(4)
        elif not is_user_email_exist(account):
            self.ui.stackedWidget_2.setCurrentIndex(2)
        elif not is_user_password_correct(account, password):
            self.ui.stackedWidget_2.setCurrentIndex(3)
        else:
            global user_now
            user_now = account
            self.close()
            self.win = MainWindow()
        # 注意返回登陆的账号信息

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

        self.ui.stackedWidget.setCurrentIndex(0)
        # 发送验证ma
        self.check = ''
        self.ui.pushButton_S_send.clicked.connect(lambda: self.send_check())
        self.ui.pushButton_S_ensure.clicked.connect(lambda: self.signup_in())

        self.ui.stackedWidget.adjustSize()
        self.ui.label.adjustSize()
        self.ui.pushButton_S_send.adjustSize()

        self.show()

    def send_check(self):
        email_address = self.ui.lineEdit_S_email_address.text()
        # 发送验证码
        if not is_valid_email(email_address):
            self.ui.stackedWidget.setCurrentIndex(1)
        elif is_user_email_exist(email_address):
            self.ui.stackedWidget.setCurrentIndex(6)
        else:
            check = send_email_code(email_address)
            if not check:
                self.ui.stackedWidget.setCurrentIndex(4)
            else:
                self.check = check

    def signup_in(self):
        check = self.ui.lineEdit_S_check.text()
        new_account = self.ui.lineEdit_S_account.text()
        new_email = self.ui.lineEdit_S_email_address.text()
        new_password = self.ui.lineEdit_S_password1.text()
        new_password2 = self.ui.lineEdit_S_password2.text()
        # 注册新用户
        if not is_valid_email(new_email):
            self.ui.stackedWidget.setCurrentIndex(1)
        elif is_user_email_exist(new_email):
            self.ui.stackedWidget.setCurrentIndex(6)
        elif new_account == '' or new_password == '':
            self.ui.stackedWidget.setCurrentIndex(5)
        elif new_password != new_password2:
            self.ui.stackedWidget.setCurrentIndex(3)
        else:
            if self.check == '':
                self.ui.stackedWidget.setCurrentIndex(4)
            elif check == self.check:
                add_user(new_account, new_email, new_password)
                self.close()
            else:
                self.ui.stackedWidget.setCurrentIndex(2)


class FindWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FindWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.check = ''

        self.ui.pushButton_F_send.clicked.connect(lambda: self.send_check())
        self.ui.pushButton_F_ensure.clicked.connect(lambda: self.find_password())

        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.pushButton_F_send.adjustSize()
        self.ui.label.adjustSize()

        self.show()

    def send_check(self):
        email_address = self.ui.lineEdit_F_email_address.text()
        if not is_valid_email(email_address):
            self.ui.stackedWidget.setCurrentIndex(1)
        elif not is_user_email_exist(email_address):
            self.ui.stackedWidget.setCurrentIndex(6)
        else:
            check = send_email_code(email_address)
            if not check:
                self.ui.stackedWidget.setCurrentIndex(4)
            else:
                self.check = check

    def find_password(self):
        check = self.ui.lineEdit_F_check.text()
        new_email = self.ui.lineEdit_F_email_address.text()
        new_password = self.ui.lineEdit_F_password1.text()
        new_password2 = self.ui.lineEdit_F_password2.text()
        # 注册新用户
        if not is_valid_email(new_email):
            self.ui.stackedWidget.setCurrentIndex(1)
        elif not is_user_email_exist(new_email):
            self.ui.stackedWidget.setCurrentIndex(6)
        elif new_password == '' or new_password2 == '':
            self.ui.stackedWidget.setCurrentIndex(5)
        elif new_password != new_password2:
            self.ui.stackedWidget.setCurrentIndex(3)
        else:
            if self.check == '':
                self.ui.stackedWidget.setCurrentIndex(4)
            elif check == self.check:
                reset_user_password(new_email, new_password)
                self.close()
            else:
                self.ui.stackedWidget.setCurrentIndex(2)


class AddTaskWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddTaskWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.stackedWidget_2.adjustSize()
        self.ui.stackedWidget.adjustSize()

        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.dateTimeEdit_ordinary_begin.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.dateTimeEdit_ordinary_end.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.dateEdit_every_begin_date.setDate(QtCore.QDate.currentDate())
        self.ui.dateEdit_every_end_date.setDate(QtCore.QDate.currentDate())
        self.ui.timeEdit_every_begin_time.setTime(QtCore.QTime.currentTime())
        self.ui.timeEdit_every_end_time.setTime(QtCore.QTime.currentTime())

        self.ui.radioButton_Add_is_every.clicked.connect(lambda: self.every_or_ordinary())

        self.ui.label.adjustSize()
        self.show()

    def every_or_ordinary(self):
        if self.ui.radioButton_Add_is_every.isChecked():
            self.ui.stackedWidget_2.setCurrentIndex(1)
        else:
            self.ui.stackedWidget_2.setCurrentIndex(0)

    def check_input(self):
        task_name = self.ui.lineEdit_Add_task_name.text()
        task_content = self.ui.textEdit_Add_task_content.toPlainText()
        # task_begin = self.ui.dateTimeEdit_Add_begin.dateTime().toPyDateTime()
        # task_end = self.ui.dateTimeEdit_Add_end.dateTime().toPyDateTime()
        task_type = self.ui.comboBox_Add_task_type.currentText()
        task_is_important = self.ui.radioButton_Add_is_important.isChecked()
        if task_name == '':
            self.ui.stackedWidget.setCurrentIndex(1)
        # elif task_begin > task_end:
        #     self.ui.stackedWidget.setCurrentIndex(2)
        elif task_type == '请选择任务类型':
            self.ui.stackedWidget.setCurrentIndex(3)
        else:
            task = Task(user_now)
            task.title = task_name
            task.content = task_content
            # task.start_time = task_begin
            # task.deadline = task_end
            task.tag = task_type
            task.is_vital = task_is_important
            return task
        return None

    def everyday_task(self):
        task = self.check_input()
        if task:
            task.is_daily = True
            add_task(task)
            self.close()

    def ordinary_task(self):
        task = self.check_input()
        if task:
            task.is_daily = False
            add_task(task)
            self.close()


class FreeTimeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FreeTimeWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.show()
        self.ui.pushButton_free_ensure.clicked.connect(lambda: self.free_time())

    def free_time(self):
        morning = self.ui.doubleSpinBox_free_morning.value()
        afternoon = self.ui.doubleSpinBox_free_afternoon.value()
        night = self.ui.doubleSpinBox_free_night.value()
        # 保存空闲时间
        self.close()


class ModifyPersonWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Modify_Person()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.check = ''
        self.ui.pushButton_modify_send.clicked.connect(lambda: self.send_check())
        self.ui.pushButton_modify_ensure.clicked.connect(lambda: self.modify_password())

        self.ui.stackedWidget.setCurrentIndex(0)

        self.show()

    def send_check(self):
        email_address = self.ui.lineEdit_modify_email_address.text()
        # 发送验证码
        if not is_valid_email(email_address):
            self.ui.stackedWidget.setCurrentIndex(1)
        elif not is_user_email_exist(email_address):
            self.ui.stackedWidget.setCurrentIndex(6)
        else:
            check = send_email_code(email_address)
            if not check:
                self.ui.stackedWidget.setCurrentIndex(4)
            else:
                self.check = check

    def modify_password(self):
        check = self.ui.lineEdit_modify_check.text()
        new_email = self.ui.lineEdit_modify_email_address.text()
        new_password = self.ui.lineEdit_modify_password1.text()
        new_password2 = self.ui.lineEdit_modify_password2.text()

        if not is_valid_email(new_email):
            self.ui.stackedWidget.setCurrentIndex(1)
        elif not is_user_email_exist(new_email):
            self.ui.stackedWidget.setCurrentIndex(6)
        elif new_password == '' or new_password2 == '':
            self.ui.stackedWidget.setCurrentIndex(5)
        elif new_password != new_password2:
            self.ui.stackedWidget.setCurrentIndex(3)
        else:
            if self.check == '':
                self.ui.stackedWidget.setCurrentIndex(4)
            elif check == self.check:
                reset_user_password(new_email, new_password)
                self.close()
            else:
                self.ui.stackedWidget.setCurrentIndex(2)
        self.close()


class ImageLoader(QObject):
    def __init__(self, label, parent=None):
        super().__init__(parent)
        self.label = label
        self.manager = QNetworkAccessManager(self)

    @pyqtSlot(QNetworkReply)
    def replyFinished(self, reply):
        if reply.error() == QNetworkReply.NoError:
            # 读取图片数据
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(reply.readAll())

            # 显示图片
            if not pixmap.isNull():
                self.label.setPixmap(pixmap)
                self.label.setScaledContents(True)  # 如果需要，使图片自动缩放以适应QLabel的大小

        reply.deleteLater()

    def loadImage(self, url):
        request = QNetworkRequest(QUrl(url))
        self.manager.get(request)
        self.manager.finished.connect(self.replyFinished)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win = None
        self.login = None
        self.ui = Ui_Main_interface()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.label_adjust_size()

        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.stackedWidget_3.setCurrentIndex(0)
        self.ui.stackedWidget_4.setCurrentIndex(0)

        image_loader = ImageLoader(self.ui.label_avatar, self)
        image_loader.loadImage(get_user_info(user_now, 'avatar_url'))  # 替换为你的图片URL
        self.ui.label_user_name.setText(get_user_info(user_now, 'name'))

        # self.todolist()
        self.ui.listWidget.itemClicked.connect(lambda: self.change_page(self.ui.listWidget.currentRow()))
        self.ui.listWidget_2.itemClicked.connect(lambda: self.change_page(self.ui.listWidget_2.currentRow() + 3))
        self.ui.pushButton_M_addtask.clicked.connect(lambda: self.add_task())
        self.ui.pushButton_P_modify_password.clicked.connect(lambda: self.modify_person())
        self.ui.pushButton_M_schedule.clicked.connect(lambda: self.schedule())
        self.ui.pushButton_M_freetime.clicked.connect(lambda: self.provide_free_time())
        self.ui.calendarWidget.clicked.connect(lambda: self.calendar_click())

        self.ui.lineEdit_modify_motto.setText(get_user_info(user_now, 'signature'))
        self.ui.lineEdit_modify_name.setText(get_user_info(user_now, 'name'))
        self.ui.label_my_emali_address.setText(user_now)

        self.show()

    def label_adjust_size(self):
        self.ui.label.adjustSize()
        self.ui.label_avatar.adjustSize()
        self.ui.label_12.adjustSize()
        self.ui.label_11.adjustSize()
        self.ui.label_10.adjustSize()
        self.ui.label_9.adjustSize()
        self.ui.label_4.adjustSize()
        self.ui.pushButton_M_schedule.adjustSize()

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

    # def todolist(self):
    #     data = get_tasks_date(user_now, datetime.today().now())  # list of task
    #     for i in data:
    #         item = QtWidgets.QListWidgetItem(i)

    def add_task(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
        self.win = AddTaskWindow()

    def provide_free_time(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
        self.win = FreeTimeWindow()

    def schedule(self):
        self.ui.stackedWidget_3.setCurrentIndex(2)
        task_list = get_ordered_tasks_date(user_now, datetime.today())
        print_list(task_list)
        # 调度当日任务

    def calendar_click(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
        date = self.ui.calendarWidget.selectedDate().toPyDate()
        task_list = get_ordered_tasks_date(user_now, date)
        print_list(task_list)

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
