import datetime

from PyQt5.QtCore import QObject, QUrl, pyqtSlot, QPropertyAnimation, QRect, QLocale, QCoreApplication
import sys
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5 import Qt
from PyQt5.QtCore import QObject, QUrl, pyqtSlot, QPropertyAnimation, QRect
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QTextCharFormat, QColor, QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QFrame
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QCheckBox, \
    QPushButton, \
    QLabel, QListWidgetItem
from PyQt5.QtWidgets import QMainWindow

from backend.daily_sentence import *
from backend.send_email_code import *
from backend.task_system import *
from frontend.Modify_Person import *
from frontend.add_task import *
from frontend.calendar_task import *
from frontend.display_task import *
from frontend.find_password import *
from frontend.free_time import *
from frontend.login_new import *
from frontend.main_interface import *
from frontend.signup import *

user_now = "2895227477@qq.com"
text_set_flag = False
main_window = None

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


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

        self.m_flag = False

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
            global user_now, main_window
            user_now = account
            store_local_user_email_password(account, password)
            self.close()
            self.win = MainWindow()
            main_window = self.win
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

        self.m_flag = False

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

        self.m_flag = False

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
        self.photo_path = None

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

        self.ui.pushButton_Add_task_photo.clicked.connect(lambda: self.upload_photos())
        self.ui.radioButton_Add_is_every.clicked.connect(lambda: self.every_or_ordinary())
        self.ui.pushButton_Add_ensure.clicked.connect(lambda: self.everyday_task()
        if self.ui.radioButton_Add_is_every.isChecked() else self.ordinary_task())

        self.ui.label.adjustSize()

        self.m_flag = False
        self.show()

    def upload_photos(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "Images (*.png *.xpm *.jpg);;All Files (*)",
                                                   options=options)
        if file_path:
            pixmap = QtGui.QPixmap(file_path)
            if not pixmap.isNull():
                self.photo_path = file_path

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
        task_duration_time = timedelta(hours=self.ui.doubleSpinBox_duration.value())
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
            modify_daily_task_pic_url(daily_task, self.photo_path)
            add_daily_task(daily_task)
            print("have added everyday task")
            main_window.todolist()
            main_window.urgent_list()
            self.close()

    def ordinary_task(self):
        task = self.check_input()
        if task:
            modify_task_pic_url(task, self.photo_path)
            add_task(task)
            print("have added ordinary task")
            main_window.todolist()
            print("will print urgent_list")
            main_window.urgent_list()
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

        self.ui.stackedWidget_wrong.setCurrentIndex(0)

        self.m_flag = False

        free_time = get_free_time(user_now)
        self.ui.doubleSpinBox_free_morning.setValue(free_time[0])
        self.ui.doubleSpinBox_free_afternoon.setValue(free_time[1])
        self.ui.doubleSpinBox_free_night.setValue(free_time[2])

        self.show()
        self.ui.pushButton_free_ensure.clicked.connect(lambda: self.free_time())

    def free_time(self):
        morning = self.ui.doubleSpinBox_free_morning.value()
        afternoon = self.ui.doubleSpinBox_free_afternoon.value()
        night = self.ui.doubleSpinBox_free_night.value()
        print(morning, afternoon, night)
        if morning > 6:
            self.ui.stackedWidget_wrong.setCurrentIndex(1)
        elif afternoon > 6:
            self.ui.stackedWidget_wrong.setCurrentIndex(2)
        elif night > 5.5:
            self.ui.stackedWidget_wrong.setCurrentIndex(3)
        else:
            set_free_time(user_now, morning, afternoon, night)
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

        # 改变日历风格
        self.setLocale(QLocale(QLocale.Chinese))
        self.setNavigationBarVisible(False)
        self.setSelectionMode(QCalendarWidget.SingleSelection)
        format = QTextCharFormat()
        format.setForeground(QColor(51, 51, 51))
        format.setBackground(QColor(247, 247, 247))
        format.setFontFamily("Microsoft YaHei")
        format.setFontPointSize(9)
        format.setFontWeight(QFont.Medium)

        self.ui.label_calendar_name.setText(task.task_title)
        self.ui.label_calendar_tag.setText(task.task_tag)
        self.ui.label_calendar_important.setText(task.task_vital)
        self.ui.label_calendar_state.setText(task.task_status)

        if task.task_is_daily:
            self.ui.checkBox_calendar_is_daily.setChecked(True)
            self.ui.checkBox_calendar_is_daily.setEnabled(False)
            self.ui.stackedWidget_2.setCurrentIndex(1)

            daily = get_daily_task_object(user_now, task.task_id)[0]

            self.ui.label_calendar_daily_begin_date.setText(
                daily.daily_task_start_date.strftime('%Y-%m-%d'))
            self.ui.label_calendar_daily_begin_time.setText(
                daily.daily_task_start_time.strftime('%H:%M:%S'))
            self.ui.label_daily_end_date.setText(daily.daily_task_end_date.strftime('%Y-%m-%d'))
            self.ui.label_daily_end_time.setText(daily.daily_task_end_time.strftime('%H:%M:%S'))

        else:
            self.ui.checkBox_calendar_is_daily.setChecked(False)
            self.ui.checkBox_calendar_is_daily.setEnabled(False)
            self.ui.stackedWidget_2.setCurrentIndex(0)

            self.ui.label_ordinary_begin_time.setText(
                task.task_start_time.strftime('%Y-%m-%d %H:%M:%S'))
            self.ui.label_ordinary_end_time.setText(
                task.task_end_time.strftime('%Y-%m-%d %H:%M:%S'))

        self.m_flag = False
        self.show()


class DisplayTaskWindow(QMainWindow):
    def __init__(self, task):
        super().__init__()
        self.ui = Ui_DisplayTaskWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.new_file_path = None

        self.ui.lineEdit_display_taskname.setText(task.task_title)
        self.ui.comboBox_important.setCurrentText(transfer_vital(task.task_vital))
        self.ui.textEdit_task_content.setText(task.task_content)
        self.ui.comboBox_display_task_type.setCurrentText(task.task_tag)
        self.ui.progressBar_display_progress.setValue(int(
            task.task_elapsed_time / task.task_duration_time * 100))
        self.ui.label_dispaly_state.setText(task.task_status)
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.pushButton_3.clicked.connect(lambda: self.update_photo())

        if task.task_is_daily:
            self.ui.checkBox_is_daily.setChecked(True)
            self.ui.checkBox_is_daily.setEnabled(False)
            self.ui.stackedWidget_2.setCurrentIndex(1)

            daily = get_daily_task_object(user_now, task.daily_task_id)[0]

            if daily.daily_task_pic_url:
                image_loader = ImageLoader(self.ui.label_15, self)
                image_loader.loadImage(daily.daily_task_pic_url)  # 替换为你的图片URL
            self.ui.dateEdit_every_begin_date.setDate(daily.daily_task_start_date)
            self.ui.dateEdit_every_end_date.setDate(daily.daily_task_end_date)
            self.ui.timeEdit_every_begin_time.setTime(daily.daily_task_start_time)
            self.ui.timeEdit_every_end_time.setTime(daily.daily_task_end_time)

            self.ui.dateEdit_every_begin_date.dateChanged.connect(
                lambda: self.modify_daily_begin_date(daily))
            self.ui.dateEdit_every_end_date.dateChanged.connect(
                lambda: self.modify_daily_end_date(daily))
            self.ui.timeEdit_every_begin_time.timeChanged.connect(
                lambda: self.modify_daily_begin_time(daily))
            self.ui.timeEdit_every_end_time.timeChanged.connect(
                lambda: self.modify_daily_end_time(daily))

            self.ui.pushButton_display_ensure.clicked.connect(lambda: self.modify_task(daily=daily))

        else:
            self.ui.checkBox_is_daily.setChecked(False)
            self.ui.checkBox_is_daily.setEnabled(False)

            self.ui.dateTimeEdit_ordinary_begin.setDateTime(task.task_start_time)
            self.ui.dateTimeEdit_ordinary_end.setDateTime(task.task_end_time)
            if task.task_pic_url:
                image_loader = ImageLoader(self.ui.label_15, self)
                image_loader.loadImage(task.task_pic_url)  # 替换为你的图片URL
            self.ui.dateTimeEdit_ordinary_begin.dateTimeChanged.connect(
                lambda: self.modify_ordinary_begin_time(task))
            self.ui.dateTimeEdit_ordinary_end.dateTimeChanged.connect(
                lambda: self.modify_ordinary_end_time(task))

            self.ui.pushButton_display_ensure.clicked.connect(lambda: self.modify_task(task=task))

        self.m_flag = False
        self.show()

    def modify_daily_begin_date(self, daily):
        daily.daily_task_start_date = self.ui.dateEdit_every_begin_date.date().toPyDate()

    def modify_daily_end_date(self, daily):
        daily.daily_task_end_date = self.ui.dateEdit_every_end_date.date().toPyDate()

    def modify_daily_begin_time(self, daily):
        daily.daily_task_start_time = self.ui.timeEdit_every_begin_time.time().toPyTime()

    def modify_daily_end_time(self, daily):
        daily.daily_task_end_time = self.ui.timeEdit_every_end_time.time().toPyTime()

    def modify_ordinary_begin_time(self, task):
        task.task_start_time = self.ui.dateTimeEdit_ordinary_begin.dateTime().toPyDateTime()

    def modify_ordinary_end_time(self, task):
        task.task_end_time = self.ui.dateTimeEdit_ordinary_end.dateTime().toPyDateTime()

    def update_photo(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "Images (*.png *.xpm *.jpg);;All Files (*)",
                                                   options=options)
        if file_path:
            pixmap = QtGui.QPixmap(file_path)
            if not pixmap.isNull():
                self.new_file_path = file_path
                self.ui.label_15.setPixmap(
                    pixmap.scaled(self.ui.label_15.width(), self.ui.label_15.height(),
                                  Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def modify_task(self, task=None, daily=None):
        if self.ui.checkBox_is_daily.isChecked():
            self.close()
            if self.new_file_path:
                daily.daily_task_pic_url = self.new_file_path
                modify_daily_task_pic_url(daily, self.new_file_path)
            reset_daily_task(daily)
        else:
            if self.new_file_path:
                task.task_pic_url = self.new_file_path
                modify_task_pic_url(task, self.new_file_path)
            self.close()
            reset_task(task)

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

        self.m_flag = False
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
    def __init__(self, task, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        self.button_1 = QPushButton("完成", self)
        self.button_2 = QPushButton(task.task_title, self)
        self.important_icon = QLabel(self)
        self.important_icon.setFixedSize(30, 30)
        if task.task_status == TaskStatus.COMPLETED:
            self.button_1.setChecked(True)

        if task.task_vital == TaskVital.TRIVIAL:
            icon_pixmap = QPixmap("frontend/icons/yellow.png")
        elif task.task_vital == TaskVital.NORMAL:
            icon_pixmap = QPixmap("frontend/icons/orange.png")
        else:
            icon_pixmap = QPixmap("frontend/icons/red.png")

        scaled_pixmap = icon_pixmap.scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.important_icon.setPixmap(scaled_pixmap)

        self.button_1.clicked.connect(lambda: main_window.complete_task(task))
        self.button_2.clicked.connect(lambda: main_window.display_task(task))
        layout.addWidget(self.button_1)
        layout.addWidget(self.button_2)
        layout.addWidget(self.important_icon)
        self.setLayout(layout)


class CustomListItem_Schedule(QWidget):
    def __init__(self, task_schedule, period=False, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        self.label_period = QLabel(str(task_schedule.task_time_period), self)
        self.label_duration = QLabel(str(task_schedule.task_time), self)
        self.checkbox_complete = QCheckBox(self)
        self.pushButton_name = QPushButton(task_schedule.task.task_title, self)
        self.important_icon = QLabel(self)
        self.important_icon.setFixedSize(30, 30)
        importance = task_schedule.task.task_vital

        if importance == TaskVital.TRIVIAL:
            icon_pixmap = QPixmap("frontend/icons/yellow.png")
        elif importance == TaskVital.NORMAL:
            icon_pixmap = QPixmap("frontend/icons/orange.png")
        else:
            icon_pixmap = QPixmap("frontend/icons/red.png")

        scaled_pixmap = icon_pixmap.scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.important_icon.setPixmap(scaled_pixmap)

        self.pushButton_name.clicked.connect(lambda: main_window.display_task(task_schedule.task))
        self.checkbox_complete.clicked.connect(
            lambda: main_window.complete_schedule_task(task_schedule, self.checkbox_complete))
        layout.addWidget(self.label_period)
        layout.addWidget(self.checkbox_complete)
        layout.addWidget(self.pushButton_name)
        layout.addWidget(self.label_duration)
        layout.addWidget(self.important_icon)
        self.setLayout(layout)


class CustomListItem_Calendar(QWidget):
    def __init__(self, task, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        self.pushButton_name = QPushButton(task.task_title, self)
        self.label_state = QLabel(task.task_status, self)
        self.important_icon = QLabel(self)
        self.important_icon.setFixedSize(30, 30)
        importance = task.task_vital
        if importance == TaskVital.TRIVIAL:
            icon_pixmap = QPixmap("frontend/icons/yellow.png")
        elif importance == TaskVital.NORMAL:
            icon_pixmap = QPixmap("frontend/icons/orange.png")
        else:
            icon_pixmap = QPixmap("frontend/icons/red.png")

        scaled_pixmap = icon_pixmap.scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.important_icon.setPixmap(scaled_pixmap)

        self.pushButton_name.clicked.connect(lambda: main_window.display_task(task))
        layout.addWidget(self.pushButton_name)
        layout.addWidget(self.label_state)
        layout.addWidget(self.important_icon)
        self.setLayout(layout)


class CustomListItem_urgent(QWidget):
    def __init__(self, task, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        self.pushButton_name = QPushButton(task.task_title, self)
        self.label_ddl = QLabel(task.task_end_time.strftime("%Y-%m-%d %H:%M:%S"), self)

        self.important_icon = QLabel(self)
        self.important_icon.setFixedSize(30, 30)
        importance = task.task_vital
        if importance == TaskVital.TRIVIAL:
            icon_pixmap = QPixmap("frontend/icons/yellow.png")
        elif importance == TaskVital.NORMAL:
            icon_pixmap = QPixmap("frontend/icons/orange.png")
        else:
            icon_pixmap = QPixmap("frontend/icons/red.png")
        scaled_pixmap = icon_pixmap.scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.important_icon.setPixmap(scaled_pixmap)

        self.pushButton_name.clicked.connect(lambda: main_window.display_task(task))
        layout.addWidget(self.pushButton_name)
        layout.addWidget(self.label_ddl)
        layout.addWidget(self.important_icon)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    # 表示此时早上好等语句有没有set
    text_set_flag = False

    def __init__(self):
        super().__init__()
        global text_set_flag
        text_set_flag = False

        # 检测屏幕分辨率
        # self.desktop = QApplication.desktop()
        # self.screenRect = self.desktop.screenGeometry()
        # self.screenheight = self.screenRect.height()
        # self.screenwidth = self.screenRect.width()
        #
        # self.height = int(self.screenheight)
        # self.width = int(self.screenwidth)
        #
        # self.resize(self.width, self.height)

        self.win = None
        self.login = None
        self.ui = Ui_Main_interface()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.label_adjust_size()

        self.m_flag = False

        self.ui.stackedWidget.setCurrentIndex(0)
        task_list = get_tasks_of_user_with_status(user_now,
                                                  TaskStatus.PENDING) + get_tasks_of_user_with_status(
            user_now, TaskStatus.UNDERWAY)
        if len(task_list) == 0:
            self.ui.stackedWidget_2.setCurrentIndex(0)
        else:
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.todolist()
        free_time_list = get_free_time(user_now)
        if free_time_list[0] == 0 and free_time_list[1] == 0 and free_time_list[2] == 0:
            self.ui.stackedWidget_3.setCurrentIndex(0)
        else:
            self.ui.stackedWidget_3.setCurrentIndex(1)
        # 注意此处需要修改，schedule的提示语
        self.ui.stackedWidget_4.setCurrentIndex(1)
        urgent_list = get_tasks_objects_urgent(user_now)
        if len(urgent_list) == 0:
            self.ui.stackedWidget_urgent.setCurrentIndex(0)
        else:
            self.ui.stackedWidget_urgent.setCurrentIndex(1)
            self.urgent_list()

        image_loader = ImageLoader(self.ui.label_avatar, self)
        image_loader.loadImage(get_user_info(user_now, 'avatar_url'))  # 替换为你的图片URL
        self.ui.label_user_name.setText(get_user_info(user_now, 'name'))
        self.ui.label_sentence.setText(get_user_info(user_now, 'signature'))

        self.ui.listWidget.itemClicked.connect(
            lambda: self.change_page(self.ui.listWidget.currentRow()))
        self.ui.listWidget_2.itemClicked.connect(
            lambda: self.change_page(self.ui.listWidget_2.currentRow() + 3))
        self.ui.pushButton_M_addtask.clicked.connect(lambda: self.add_task())
        self.ui.pushButton_P_modify_password.clicked.connect(lambda: self.modify_person())
        self.ui.pushButton_M_schedule.clicked.connect(lambda: self.schedule())
        self.ui.pushButton_M_freetime.clicked.connect(lambda: self.provide_free_time())
        self.ui.calendarWidget.clicked.connect(lambda: self.calendar_click())
        self.ui.pushButton_modify_avatar.clicked.connect(lambda: self.modify_avatar())

        self.ui.label_Sta_accumulate_sumofnum.setText(
            "任务个数：" + str(get_complete_task_sum(user_now)))
        work_time_sum = get_work_time_sum(user_now)
        self.ui.label_Sta_accumulate_sumoftime.setText(
            "时长总数：" + f'{work_time_sum.days * 24 + work_time_sum.seconds // 3600}小时 {work_time_sum.seconds // 60 % 60}分钟')
        self.ui.label_Sta_accumulate_averagetime.setText(
            "日均时长：" + str(get_average_work_time(user_now)))
        self.ui.label_Sta_everyday_sumofnum.setText(
            "任务个数：" + str(get_complete_task_sum_in_date(user_now, date.today())))
        work_time = get_work_time(user_now)
        self.ui.label_Sta_everyday_sumoftime.setText(
            "时长总数：" + f'{work_time.days * 24 + work_time.seconds // 3600}小时 {work_time.seconds // 60 % 60}分钟')

        self.ui.lineEdit_modify_motto.setText(get_user_info(user_now, 'signature'))
        self.ui.lineEdit_modify_name.setText(get_user_info(user_now, 'name'))
        self.ui.label_my_emali_address.setText(user_now)
        image_loader = ImageLoader(self.ui.label_user_avatar, self)
        image_loader.loadImage(get_user_info(user_now, 'avatar_url'))
        self.ui.lineEdit_modify_name.textChanged.connect(lambda: self.modify_name())
        self.ui.lineEdit_modify_motto.textChanged.connect(lambda: self.modify_motto())

        self.ui.frame_20.setFrameShape(QFrame.StyledPanel)
        self.ui.frame_20.setFixedSize(self.ui.frame_20.width(), self.ui.frame_20.height())
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout = QHBoxLayout()
        layout.addWidget(self.canvas)
        self.ui.frame_20.setLayout(layout)
        self.plot_task_num()

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showtime)

        timer.start()

        # 用于控制左边listWidget地行间距
        self.ui.listWidget.setSpacing(15)
        self.ui.listWidget_2.setSpacing(10)

        # 用于控制电子木鱼
        moralities = str(get_user_info(user_now, 'moralities'))
        self.ui.label_merits.setText(moralities)

        self.ui.frame_24.setVisible(False)
        self.ui.pushButton_modify_avatar.clicked.connect(lambda: self.modify_avatar())
        self.ui.pushButton_2.clicked.connect(lambda: self.do_muyu_anim())
        self.ui.pushButton_2.clicked.connect(lambda: self.moralities_add())

        self.show()

    # 显示当前时间
    def showtime(self):
        global text_set_flag
        datetime = QtCore.QDateTime.currentDateTime()
        # print("datetime")
        text = datetime.toString('yyyy-MM-dd HH:mm:ss')
        # print(text)
        self.ui.label_time.setText(text)
        # self.retranslateUi(self)
        # QtCore.QMetaObject.connectSlotsByName(self)
        current_time = text.split(' ')[1]
        current_hour = current_time.split(':')[0]
        if text_set_flag == False:
            if 0 <= int(current_hour) < 6:
                night_text_list = ["夜深了，休息一下吧！辛苦啦！", "深夜还在奋斗，respect",
                                   "这个点登录，是在为明天做计划吗？"]
                night_text = night_text_list.pop(random.randint(0, len(night_text_list) - 1))
                self.ui.label.setText(night_text)
                text_set_flag = True
            elif int(current_hour) < 12:
                morning_text_list = ["早上好，今天要做些什么呢？", "早上好~欢迎开启美好的一天☀",
                                     "又是新的一天啦 加油！"]
                morning_text = morning_text_list.pop(random.randint(0, len(morning_text_list) - 1))
                self.ui.label.setText(morning_text)
                text_set_flag = True
            elif int(current_hour) < 19:
                self.ui.label.setText("下午好，要来杯下午茶吗？")
                text_set_flag = True
            else:
                self.ui.label.setText("晚上好，今晚的月亮好漂亮")
                text_set_flag = True

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
        self.ui.listWidget_todolist.clear()
        task_list = get_tasks_of_user_with_status(user_now, TaskStatus.PENDING) + \
                    get_tasks_of_user_with_status(user_now, TaskStatus.UNDERWAY)
        if len(task_list) == 0:
            self.ui.stackedWidget_2.setCurrentIndex(0)
        else:
            for task in task_list:
                custom_item = CustomListItem_Todo(task)
                custom_item.button_1.setStyleSheet("QPushButton{\n"
                                                   "background-color: rgb(41, 74, 82);\n"
                                                   "color: rgb(255, 255, 255);\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    padding-left:5px;\n"
                                                   "    padding-top:5px;\n"
                                                   "}")
                list_item = QListWidgetItem(self.ui.listWidget_todolist)
                list_item.setSizeHint(custom_item.sizeHint())
                self.ui.listWidget_todolist.addItem(list_item)
                self.ui.listWidget_todolist.setItemWidget(list_item, custom_item)

    def urgent_list(self):
        self.ui.listWidget_urgent.clear()
        urgent_list = get_tasks_objects_urgent(user_now)
        print(len(urgent_list))
        if len(urgent_list) == 0:
            self.ui.stackedWidget_urgent.setCurrentIndex(0)
        else:
            self.ui.stackedWidget_urgent.setCurrentIndex(1)
            for task in urgent_list:
                custom_item = CustomListItem_urgent(task)
                list_item = QListWidgetItem(self.ui.listWidget_urgent)
                list_item.setSizeHint(custom_item.sizeHint())
                self.ui.listWidget_urgent.addItem(list_item)
                self.ui.listWidget_urgent.setItemWidget(list_item, custom_item)

    def plot_task_num(self):
        self.figure.clear()
        y = get_week_report_of_user(user_now)
        x = [i for i in range(7)]
        ax = self.figure.add_subplot(111)
        ax.plot(x, y, color='green')
        ax.set_xticks(x)
        ax.set_xticklabels(['周一', '周二', '周三', '周四', '周五', '周六', '周日'])
        ax.set_xlabel('日期')
        ax.set_ylabel('任务个数')
        self.canvas.draw()

    def add_task(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
        self.win = AddTaskWindow()

    def complete_task(self, task):
        task_is_complete(task)
        self.todolist()
        self.urgent_list()
        self.schedule()
        self.ui.label_Sta_accumulate_sumofnum.setText(
            "任务个数：" + str(get_complete_task_sum(user_now)))
        work_time_sum = get_work_time_sum(user_now)
        self.ui.label_Sta_accumulate_sumoftime.setText(
            "时长总数：" + f'{work_time_sum.days * 24 + work_time_sum.seconds // 3600}小时 {work_time_sum.seconds // 60 % 60}分钟')
        self.ui.label_Sta_accumulate_averagetime.setText(
            "日均时长：" + str(get_average_work_time(user_now)))
        self.ui.label_Sta_everyday_sumofnum.setText(
            "任务个数：" + str(get_complete_task_sum_in_date(user_now, date.today())))
        work_time = get_work_time(user_now)
        self.ui.label_Sta_everyday_sumoftime.setText(
            "时长总数：" + f'{work_time.days * 24 + work_time.seconds // 3600}小时 {work_time.seconds // 60 % 60}分钟')
        self.plot_task_num()

    def display_task(self, task):
        self.win = DisplayTaskWindow(task)

    def provide_free_time(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
        self.win = FreeTimeWindow()

    def schedule(self):
        self.ui.listWidget_schedule.clear()
        free_time = get_free_time(user_now)
        schedule_list = get_task_schedule_objects(user_now, free_time[0], free_time[1], free_time[2])
        if len(schedule_list) == 0:
            self.ui.stackedWidget_3.setCurrentIndex(3)
        else:
            self.ui.stackedWidget_3.setCurrentIndex(2)
            now_period = schedule_list[0].task_time_period
            count = 0
            for task_schedule in schedule_list:
                if task_schedule.task_time_period == now_period:
                    count += 1
                    if count == 1:
                        custom_item = CustomListItem_Schedule(task_schedule, True)
                    else:
                        custom_item = CustomListItem_Schedule(task_schedule, False)
                else:
                    now_period = task_schedule.task_time_period
                    count = 1
                    custom_item = CustomListItem_Schedule(task_schedule, True)
                list_item = QListWidgetItem(self.ui.listWidget_schedule)
                list_item.setSizeHint(custom_item.sizeHint())
                self.ui.listWidget_schedule.addItem(list_item)
                self.ui.listWidget_schedule.setItemWidget(list_item, custom_item)

    def complete_schedule_task(self, task_schedule, checkbox):
        add_work_time(task_schedule.task, task_schedule.task_time)
        checkbox.setChecked(True)
        checkbox.setEnabled(False)
        self.todolist()
        self.urgent_list()
        self.ui.label_Sta_accumulate_sumofnum.setText(
            "任务个数：" + str(get_complete_task_sum(user_now)))
        work_time_sum = get_work_time_sum(user_now)
        self.ui.label_Sta_accumulate_sumoftime.setText(
            "时长总数：" + f'{work_time_sum.days * 24 + work_time_sum.seconds // 3600}小时 {work_time_sum.seconds // 60 % 60}分钟')
        self.ui.label_Sta_accumulate_averagetime.setText(
            "日均时长：" + str(get_average_work_time(user_now)))
        self.ui.label_Sta_everyday_sumofnum.setText(
            "任务个数：" + str(get_complete_task_sum_in_date(user_now, date.today())))
        work_time = get_work_time(user_now)
        self.ui.label_Sta_everyday_sumoftime.setText(
            "时长总数：" + f'{work_time.days * 24 + work_time.seconds // 3600}小时 {work_time.seconds // 60 % 60}分钟')
        self.plot_task_num()

    def calendar_click(self):
        self.ui.listWidget_calender.clear()
        current_date = self.ui.calendarWidget.selectedDate().toPyDate()
        task_list = get_ordered_tasks_date(user_now, current_date)
        if len(task_list) == 0:
            self.ui.stackedWidget_4.setCurrentIndex(0)
        else:
            self.ui.stackedWidget_4.setCurrentIndex(2)
            for task in task_list:
                custom_item = CustomListItem_Calendar(task)
                list_item = QListWidgetItem(self.ui.listWidget_calender)
                list_item.setSizeHint(custom_item.sizeHint())
                self.ui.listWidget_calender.addItem(list_item)
                self.ui.listWidget_calender.setItemWidget(list_item, custom_item)

    def modify_person(self):
        self.win = ModifyPersonWindow()

    def modify_name(self):
        new_name = self.ui.lineEdit_modify_name.text()
        reset_user_info(user_now, 'name', new_name)
        self.ui.label_user_name.setText(new_name)

    def modify_motto(self):
        new_motto = self.ui.lineEdit_modify_motto.text()
        reset_user_info(user_now, 'signature', new_motto)
        self.ui.label_sentence.setText(new_motto)

    def modify_avatar(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "Images (*.png *.xpm *.jpg);;All Files (*)",
                                                   options=options)
        if file_path:
            pixmap = QtGui.QPixmap(file_path)
            if not pixmap.isNull():
                self.ui.label_user_avatar.setPixmap(
                    pixmap.scaled(self.ui.label_user_avatar.width(),
                                  self.ui.label_user_avatar.height(),
                                  Qt.KeepAspectRatio, Qt.SmoothTransformation))
                modify_user_avatar(user_now, file_path)
                self.ui.label_avatar.setPixmap(
                    pixmap.scaled(self.ui.label_user_avatar.width(),
                                  self.ui.label_user_avatar.height(),
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

    def do_muyu_anim(self):
        self.ui.frame_24.setVisible(True)

        self.anim_move = QPropertyAnimation(self.ui.frame_24, b"geometry")
        self.anim_move.setDuration(300)
        self.anim_move.setStartValue(QRect(160, 120, 120, 41))
        self.anim_move.setEndValue(QRect(170, 20, 120, 41))
        self.anim_move.finished.connect(self.check_animation_finished)
        self.anim_move.start()
        # morality = get_user_info(user_now, 'moralities')
        # morality += 1
        # reset_user_info(user_now, 'moralities', morality)
        # self.ui.label_merits.setText(str(morality))

    def check_animation_finished(self):
        if self.ui.frame_24.geometry() == QRect(170, 20, 120, 41):
            self.ui.frame_24.setVisible(False)

        # self.anim_disappear = QPropertyAnimation(self.ui.frame_24, b"windowOpacity")
        # self.anim_disappear.setDuration(20)
        # self.anim_disappear.setStartValue(1)
        # self.anim_disappear.setEndValue(0)
        # self.anim_disappear.start()
        # print("窗口渐隐")
        # for i in range(80, 0, -1):
        #     opacity = i/100
        #     print("opacity:", opacity)
        #     self.ui.frame_24.setStyleSheet("background-color:rgba(")
        #     self.ui.frame_24.repaint()
        #     QApplication.processEvents()
        #     sleep(0.05)

    def moralities_add(self):
        morality = get_user_info(user_now, 'moralities')
        morality += 1
        reset_user_info(user_now, 'moralities', morality)
        self.ui.label_merits.setText(str(morality))


if __name__ == '__main__':
    QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    # main_window = MainWindow()
    window = LoginWindow()
    sys.exit(app.exec_())
