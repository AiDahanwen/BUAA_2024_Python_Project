from PyQt5.QtCore import QObject, QUrl, pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QCursor
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QHBoxLayout, QCheckBox, QPushButton, \
    QLabel, QListWidgetItem
from PyQt5 import QtCore, Qt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt

from frontend.login_new import *
from frontend.Modify_Person import *
from frontend.signup import *
from frontend.find_password import *
from frontend.add_task import *
from frontend.main_interface import *
from frontend.free_time import *
from frontend.display_task import *
from frontend.calendar_task import *

from backend.daily_sentence import *
from backend.send_email_code import *
from backend.user_system import *
from backend.task_system import *

import sys
import res
import resource

user_now = "2895227477@qq.com"
morning = 0
afternoon = 0
night = 0


def transfer_vital(vital):
    if vital == TaskVital.TRIVIAL:
        return "不重要"
    elif vital == TaskVital.NORMAL:
        return "一般重要"
    else:
        return "特别重要"


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

    def mousePressEvent(self, event):  # 鼠标拖拽窗口移动
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))



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

    def mousePressEvent(self, event):  # 鼠标拖拽窗口移动
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


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
    def mousePressEvent(self, event):  # 鼠标拖拽窗口移动
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


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
        self.ui.pushButton_Add_ensure.clicked.connect(lambda: self.everyday_task()
        if self.ui.radioButton_Add_is_every.isChecked() else self.ordinary_task())

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
        task_type = self.ui.comboBox_Add_task_type.currentText()
        task_important = self.ui.comboBox_important.currentText()
        task_duration_time = self.ui.doubleSpinBox_duration.value()
        if task_name == "":
            self.ui.stackedWidget.setCurrentIndex(1)
        elif task_type == '请选择任务类型':
            self.ui.stackedWidget.setCurrentIndex(3)
        elif task_important == '请选择重要等级':
            self.ui.stackedWidget.setCurrentIndex(4)
        elif task_duration_time == 0:
            self.ui.stackedWidget.setCurrentIndex(5)
        elif self.ui.radioButton_Add_is_every.isChecked():
            task_begin_date = self.ui.dateEdit_every_begin_date.date().toPyDate()
            task_end_date = self.ui.dateEdit_every_end_date.date().toPyDate()
            task_begin_time = self.ui.timeEdit_every_begin_time.time().toPyTime()
            task_end_time = self.ui.timeEdit_every_end_time.time().toPyTime()
            if task_begin_date > task_end_date or task_begin_time > task_end_time:
                self.ui.stackedWidget.setCurrentIndex(2)
            else:
                daily_task = DailyTask(user_now, daily_task_tag=task_type
                                       , daily_task_title=task_name
                                       , daily_task_start_date=task_begin_date
                                       , daily_task_end_date=task_end_date
                                       , daily_task_start_time=task_begin_time
                                       , daily_task_end_time=task_end_time
                                       , daily_task_content=task_content
                                       , daily_task_vital=get_task_vital(task_important)
                                       , daily_task_duration_time=task_duration_time)

                return daily_task
        else:
            task_begin = self.ui.dateTimeEdit_ordinary_begin.dateTime().toPyDateTime()
            task_end = self.ui.dateTimeEdit_ordinary_end.dateTime().toPyDateTime()
            if task_begin > task_end:
                self.ui.stackedWidget.setCurrentIndex(2)
            else:
                ordinary_task = Task(user_now, task_vital=get_task_vital(task_important)
                                     , task_title=task_name
                                     , task_start_time=task_begin
                                     , task_end_time=task_end
                                     , task_content=task_content
                                     , task_tag=task_type
                                     , task_duration_time=task_duration_time)
                return ordinary_task
        return None

    def everyday_task(self):
        daily_task = self.check_input()
        if daily_task:
            add_daily_task(daily_task)
            self.close()

    def ordinary_task(self):
        task = self.check_input()
        if task:
            add_task(task)
            self.close()

    def mousePressEvent(self, event):  # 鼠标拖拽窗口移动
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


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
        global morning, afternoon, night
        morning = self.ui.doubleSpinBox_free_morning.value()
        afternoon = self.ui.doubleSpinBox_free_afternoon.value()
        night = self.ui.doubleSpinBox_free_night.value()
        # 保存空闲时间
        self.close()

    def mousePressEvent(self, event):  # 鼠标拖拽窗口移动
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


class CalendarTaskWindow(QMainWindow):
    def __init__(self, task):
        super().__init__()
        self.ui = Ui_CalendarTaskWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.label_calendar_name.setText(task.task_title)
        self.ui.label_calendar_tag.setText(task.task_tag)
        self.ui.label_calendar_important.setText(task.task_vital)
        self.ui.label_calendar_state.setText(task.task_status)

        if task.task_is_daily:
            self.ui.checkBox_calendar_is_daily.setChecked(True)
            self.ui.checkBox_calendar_is_daily.setEnabled(False)
            self.ui.stackedWidget_2.setCurrentIndex(1)

            daily = get_daily_task_object_of_user_id(user_now, task.task_id)[0]

            self.ui.label_calendar_daily_begin_date.setText(daily.daily_task_start_date.strftime('%Y-%m-%d'))
            self.ui.label_calendar_daily_begin_time.setText(daily.daily_task_start_time.strftime('%H:%M:%S'))
            self.ui.label_daily_end_date.setText(daily.daily_task_end_date.strftime('%Y-%m-%d'))
            self.ui.label_daily_end_time.setText(daily.daily_task_end_time.strftime('%H:%M:%S'))
        else:
            self.ui.checkBox_calendar_is_daily.setChecked(False)
            self.ui.checkBox_calendar_is_daily.setEnabled(False)
            self.ui.stackedWidget_2.setCurrentIndex(0)

            self.ui.label_ordinary_begin_time.setText(task.task_start_time.strftime('%Y-%m-%d %H:%M:%S'))
            self.ui.label_ordinary_end_time.setText(task.task_end_time.strftime('%Y-%m-%d %H:%M:%S'))

        self.show()


class DisplayTaskWindow(QMainWindow):
    def __init__(self, task):
        super().__init__()
        self.ui = Ui_DisplayTaskWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.lineEdit_display_taskname.setText(task.task_title)
        self.ui.comboBox_important.setCurrentIndex(self.transfer_vital(task.task_vital))
        self.ui.textEdit_task_content.setText(task.task_content)
        self.ui.comboBox_display_task_type.setCurrentIndex(task.task_tag)
        self.ui.progressBar_display_progress.setValue(task.task_elapsed_time / task.task_duration_time * 100)
        self.ui.label_dispaly_state.setText(task.task_status)
        self.ui.stackedWidget_2.setCurrentIndex(0)

        if task.task_is_daily:
            self.ui.checkBox_is_daily.setChecked(True)
            self.ui.checkBox_is_daily.setEnabled(False)
            self.ui.stackedWidget_2.setCurrentIndex(1)

            daily = get_daily_task_object_of_user_id(user_now, task.task_id)[0]

            self.ui.dateEdit_every_begin_date.setDate(daily.daily_task_start_date)
            self.ui.dateEdit_every_end_date.setDate(daily.daily_task_end_date)
            self.ui.timeEdit_every_begin_time.setTime(daily.daily_task_start_time)
            self.ui.timeEdit_every_end_time.setTime(daily.daily_task_end_time)

            # self.ui.dateEdit_every_begin_date.dateChanged.connect(lambda: self.modify_daily_begin_date())
            # self.ui.dateEdit_every_end_date.dateChanged.connect(lambda: self.modify_daily_end_date())
            # self.ui.timeEdit_every_begin_time.timeChanged.connect(lambda: self.modify_daily_begin_time())
            # self.ui.timeEdit_every_end_time.timeChanged.connect(lambda: self.modify_daily_end_time())

        else:
            self.ui.checkBox_is_daily.setChecked(False)
            self.ui.checkBox_is_daily.setEnabled(False)

            self.ui.dateTimeEdit_ordinary_begin.setDateTime(task.task_start_time)
            self.ui.dateTimeEdit_ordinary_end.setDateTime(task.task_end_time)

            # self.ui.dateTimeEdit_ordinary_begin.dateTimeChanged.connect(lambda: self.modify_ordinary_begin_time())
            # self.ui.dateTimeEdit_ordinary_end.dateTimeChanged.connect(lambda: self.modify_ordinary_end_time())
        self.ui.pushButton_display_ensure.clicked.connect(lambda: self.modify_task(task))
        self.show()

    def modify_task(self, task):


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

    def mousePressEvent(self, event):  # 鼠标拖拽窗口移动
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


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

    def mousePressEvent(self, event):  # 鼠标拖拽窗口移动
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


class CustomListItem_Todo(QWidget):
    def __init__(self, text, importance=TaskVital.TRIVIAL, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        self.button_1 = QCheckBox(self)
        self.button_2 = QPushButton(text, self)
        self.important_icon = QLabel(self)
        self.important_icon.setFixedSize(30, 30)

        if importance == TaskVital.TRIVIAL:
            icon_pixmap = QPixmap("../icons/橙色五角星.png")
        elif importance == TaskVital.NORMAL:
            icon_pixmap = QPixmap("../icons/黄色五角星.png")
        else:
            icon_pixmap = QPixmap("../icons/红色五角星.png")

        scaled_pixmap = icon_pixmap.scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.important_icon.setPixmap(scaled_pixmap)

        layout.addWidget(self.button_1)
        layout.addWidget(self.button_2)
        layout.addWidget(self.important_icon)
        self.setLayout(layout)


class CustomListItem_Schedule(QWidget):
    def __init__(self, period, name, importance=TaskVital.TRIVIAL, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        self.label_period = QLabel(period, self)
        self.pushButton_name = QPushButton(name, self)
        self.important_icon = QLabel(self)
        self.important_icon.setFixedSize(30, 30)

        if importance == TaskVital.TRIVIAL:
            icon_pixmap = QPixmap("../icons/橙色五角星.png")
        elif importance == TaskVital.NORMAL:
            icon_pixmap = QPixmap("../icons/黄色五角星.png")
        else:
            icon_pixmap = QPixmap("../icons/红色五角星.png")

        scaled_pixmap = icon_pixmap.scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.important_icon.setPixmap(scaled_pixmap)

        layout.addWidget(self.label_period, self.pushButton_name, self.important_icon)
        self.setLayout(layout)


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
        self.ui.pushButton_modify_avatar.clicked.connect(lambda: self.modify_avatar())

        self.ui.lineEdit_modify_motto.setText(get_user_info(user_now, 'signature'))
        self.ui.lineEdit_modify_name.setText(get_user_info(user_now, 'name'))
        self.ui.label_my_emali_address.setText(user_now)
        image_loader = ImageLoader(self.ui.label_user_avatar, self)
        image_loader.loadImage(get_user_info(user_now, 'avatar_url'))
        self.ui.lineEdit_modify_name.textChanged.connect(lambda: self.modify_name())
        self.ui.lineEdit_modify_motto.textChanged.connect(lambda: self.modify_motto())

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

    def todolist(self):
        task_list = get_tasks_of_user_with_status(user_now, TaskStatus.PENDING) + \
                    get_tasks_of_user_with_status(user_now, TaskStatus.UNDERWAY)
        for task in task_list:
            custom_item = CustomListItem_Todo(task.task_title, task)
            custom_item.button_1.clicked.connect(lambda: self.complete_task(task))
            custom_item.button_2.clicked.connect(lambda: self.display_task(task))
            list_item = QListWidgetItem(self.ui.listWidget_todolist)
            list_item.setSizeHint(custom_item.sizeHint())
            self.ui.listWidget_todolist.addItem(list_item)
            self.ui.listWidget_todolist.setItemWidget(list_item, custom_item)

    def add_task(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
        self.win = AddTaskWindow()
        self.todolist()

    def complete_task(self, task):

    def display_task(self, task):
        self.win = DisplayTaskWindow(task)

    def provide_free_time(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
        self.win = FreeTimeWindow()

    def schedule(self):
        self.ui.stackedWidget_3.setCurrentIndex(2)
        schedule_list = get_task_schedule_objects(user_now, morning, afternoon, night)
        for task in schedule_list:

    def calendar_click(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
        current_date = self.ui.calendarWidget.selectedDate().toPyDate()
        task_list = get_ordered_tasks_date(user_now, current_date)
        print_list(task_list)

    def modify_person(self):
        self.win = ModifyPersonWindow()

    def modify_name(self):
        new_name = self.ui.lineEdit_modify_name.text()
        reset_user_info(user_now, 'name', new_name)
        self.ui.label_user_name.setText(new_name)

    def modify_motto(self):
        new_motto = self.ui.lineEdit_modify_motto.text()
        reset_user_info(user_now, 'signature', new_motto)

    def modify_avatar(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "Images (*.png *.xpm *.jpg);;All Files (*)", options=options)
        if file_path:
            pixmap = QtGui.QPixmap(file_path)
            if not pixmap.isNull():
                self.ui.label_user_avatar.setPixmap(
                    pixmap.scaled(self.ui.label_user_avatar.width(), self.ui.label_user_avatar.height(),
                                  Qt.KeepAspectRatio, Qt.SmoothTransformation))
                modify_user_avatar(user_now, file_path)
                self.ui.label_avatar.setPixmap(
                    pixmap.scaled(self.ui.label_user_avatar.width(), self.ui.label_user_avatar.height(),
                                  Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def log_out(self):
        global user_now
        self.close()
        self.login = LoginWindow()
        user_now = ''

    def mousePressEvent(self, event):  # 鼠标拖拽窗口移动
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 鼠标拖拽窗口移动
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
