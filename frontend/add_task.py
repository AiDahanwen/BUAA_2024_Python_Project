# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_task.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddTaskWindow(object):
    def setupUi(self, AddTaskWindow):
        AddTaskWindow.setObjectName("AddTaskWindow")
        AddTaskWindow.resize(711, 703)
        self.centralwidget = QtWidgets.QWidget(AddTaskWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(140, 70, 451, 631))
        self.frame.setMinimumSize(QtCore.QSize(431, 531))
        self.frame.setStyleSheet("#frame{\n"
"    border-radius:15px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 0, 141, 41))
        self.label.setMinimumSize(QtCore.QSize(111, 41))
        self.label.setStyleSheet("font: 75 20pt \"微软雅黑\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 60, 421, 411))
        self.frame_2.setStyleSheet("QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_Add_task_name = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit_Add_task_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_Add_task_name.setSizePolicy(sizePolicy)
        self.lineEdit_Add_task_name.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_Add_task_name.setText("")
        self.lineEdit_Add_task_name.setObjectName("lineEdit_Add_task_name")
        self.verticalLayout.addWidget(self.lineEdit_Add_task_name)
        self.textEdit_Add_task_content = QtWidgets.QTextEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.textEdit_Add_task_content.sizePolicy().hasHeightForWidth())
        self.textEdit_Add_task_content.setSizePolicy(sizePolicy)
        self.textEdit_Add_task_content.setObjectName("textEdit_Add_task_content")
        self.verticalLayout.addWidget(self.textEdit_Add_task_content)
        self.textEdit_Add_task_photo = QtWidgets.QTextEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textEdit_Add_task_photo.sizePolicy().hasHeightForWidth())
        self.textEdit_Add_task_photo.setSizePolicy(sizePolicy)
        self.textEdit_Add_task_photo.setObjectName("textEdit_Add_task_photo")
        self.verticalLayout.addWidget(self.textEdit_Add_task_photo)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.radioButton_Add_is_every = QtWidgets.QRadioButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_Add_is_every.sizePolicy().hasHeightForWidth())
        self.radioButton_Add_is_every.setSizePolicy(sizePolicy)
        self.radioButton_Add_is_every.setObjectName("radioButton_Add_is_every")
        self.horizontalLayout_10.addWidget(self.radioButton_Add_is_every)
        self.verticalLayout.addWidget(self.frame_4)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
        self.stackedWidget_2.setMinimumSize(QtCore.QSize(311, 88))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.layoutWidget = QtWidgets.QWidget(self.page_2)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 421, 80))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_21 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setMinimumSize(QtCore.QSize(309, 36))
        self.frame_21.setStyleSheet("")
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(60, 21))
        self.label_4.setStyleSheet("border:none;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.dateTimeEdit_ordinary_begin = QtWidgets.QDateTimeEdit(self.frame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit_ordinary_begin.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit_ordinary_begin.setSizePolicy(sizePolicy)
        self.dateTimeEdit_ordinary_begin.setMinimumSize(QtCore.QSize(234, 25))
        self.dateTimeEdit_ordinary_begin.setObjectName("dateTimeEdit_ordinary_begin")
        self.horizontalLayout_5.addWidget(self.dateTimeEdit_ordinary_begin)
        self.verticalLayout_3.addWidget(self.frame_21)
        self.frame_3 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(309, 36))
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(60, 21))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.dateTimeEdit_ordinary_end = QtWidgets.QDateTimeEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit_ordinary_end.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit_ordinary_end.setSizePolicy(sizePolicy)
        self.dateTimeEdit_ordinary_end.setMinimumSize(QtCore.QSize(234, 25))
        self.dateTimeEdit_ordinary_end.setObjectName("dateTimeEdit_ordinary_end")
        self.horizontalLayout_6.addWidget(self.dateTimeEdit_ordinary_end)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.stackedWidget_2.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 1, 421, 81))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame1 = QtWidgets.QFrame(self.layoutWidget1)
        self.frame1.setObjectName("frame1")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame1)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(60, 30))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.dateEdit_every_begin_date = QtWidgets.QDateEdit(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_every_begin_date.sizePolicy().hasHeightForWidth())
        self.dateEdit_every_begin_date.setSizePolicy(sizePolicy)
        self.dateEdit_every_begin_date.setMinimumSize(QtCore.QSize(86, 25))
        self.dateEdit_every_begin_date.setObjectName("dateEdit_every_begin_date")
        self.horizontalLayout_11.addWidget(self.dateEdit_every_begin_date)
        self.label_11 = QtWidgets.QLabel(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(84, 30))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.timeEdit_every_begin_time = QtWidgets.QTimeEdit(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_every_begin_time.sizePolicy().hasHeightForWidth())
        self.timeEdit_every_begin_time.setSizePolicy(sizePolicy)
        self.timeEdit_every_begin_time.setMinimumSize(QtCore.QSize(56, 25))
        self.timeEdit_every_begin_time.setObjectName("timeEdit_every_begin_time")
        self.horizontalLayout_11.addWidget(self.timeEdit_every_begin_time)
        self.verticalLayout_2.addWidget(self.frame1)
        self.frame2 = QtWidgets.QFrame(self.layoutWidget1)
        self.frame2.setObjectName("frame2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame2)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_10 = QtWidgets.QLabel(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(60, 30))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_13.addWidget(self.label_10)
        self.dateEdit_every_end_date = QtWidgets.QDateEdit(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_every_end_date.sizePolicy().hasHeightForWidth())
        self.dateEdit_every_end_date.setSizePolicy(sizePolicy)
        self.dateEdit_every_end_date.setMinimumSize(QtCore.QSize(86, 25))
        self.dateEdit_every_end_date.setObjectName("dateEdit_every_end_date")
        self.horizontalLayout_13.addWidget(self.dateEdit_every_end_date)
        self.label_12 = QtWidgets.QLabel(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(84, 30))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        self.timeEdit_every_end_time = QtWidgets.QTimeEdit(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_every_end_time.sizePolicy().hasHeightForWidth())
        self.timeEdit_every_end_time.setSizePolicy(sizePolicy)
        self.timeEdit_every_end_time.setMinimumSize(QtCore.QSize(56, 25))
        self.timeEdit_every_end_time.setObjectName("timeEdit_every_end_time")
        self.horizontalLayout_13.addWidget(self.timeEdit_every_end_time)
        self.verticalLayout_2.addWidget(self.frame2)
        self.stackedWidget_2.addWidget(self.page_3)
        self.verticalLayout.addWidget(self.stackedWidget_2)
        self.frame3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame3.sizePolicy().hasHeightForWidth())
        self.frame3.setSizePolicy(sizePolicy)
        self.frame3.setObjectName("frame3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame3)
        self.horizontalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.comboBox_important = QtWidgets.QComboBox(self.frame3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_important.sizePolicy().hasHeightForWidth())
        self.comboBox_important.setSizePolicy(sizePolicy)
        self.comboBox_important.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_important.setObjectName("comboBox_important")
        self.comboBox_important.addItem("")
        self.comboBox_important.addItem("")
        self.comboBox_important.addItem("")
        self.comboBox_important.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_important)
        self.verticalLayout.addWidget(self.frame3)
        self.comboBox_Add_task_type = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_Add_task_type.sizePolicy().hasHeightForWidth())
        self.comboBox_Add_task_type.setSizePolicy(sizePolicy)
        self.comboBox_Add_task_type.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_Add_task_type.setPlaceholderText("")
        self.comboBox_Add_task_type.setDuplicatesEnabled(True)
        self.comboBox_Add_task_type.setObjectName("comboBox_Add_task_type")
        self.comboBox_Add_task_type.addItem("")
        self.comboBox_Add_task_type.addItem("")
        self.comboBox_Add_task_type.addItem("")
        self.comboBox_Add_task_type.addItem("")
        self.comboBox_Add_task_type.addItem("")
        self.comboBox_Add_task_type.addItem("")
        self.verticalLayout.addWidget(self.comboBox_Add_task_type)
        self.frame4 = QtWidgets.QFrame(self.frame)
        self.frame4.setGeometry(QtCore.QRect(310, 0, 111, 32))
        self.frame4.setStyleSheet("QPushButton:hover{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.frame4.setObjectName("frame4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame4)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_3.setStyleSheet("border:none;")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resource/icons/24gl-minimization.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame4)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_4.setStyleSheet("border:none;")
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resource/icons/Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.frame5 = QtWidgets.QFrame(self.frame)
        self.frame5.setGeometry(QtCore.QRect(40, 480, 329, 95))
        self.frame5.setStyleSheet("QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.frame5.setObjectName("frame5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_Add_ensure = QtWidgets.QPushButton(self.frame5)
        self.pushButton_Add_ensure.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_Add_ensure.setObjectName("pushButton_Add_ensure")
        self.verticalLayout_4.addWidget(self.pushButton_Add_ensure, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame5)
        self.stackedWidget.setMinimumSize(QtCore.QSize(311, 41))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_task_void = QtWidgets.QWidget()
        self.page_task_void.setObjectName("page_task_void")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_task_void)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.page_task_void)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.stackedWidget.addWidget(self.page_task_void)
        self.page_later_time = QtWidgets.QWidget()
        self.page_later_time.setObjectName("page_later_time")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_later_time)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.page_later_time)
        self.label_3.setMinimumSize(QtCore.QSize(293, 23))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.stackedWidget.addWidget(self.page_later_time)
        self.page_task_type = QtWidgets.QWidget()
        self.page_task_type.setObjectName("page_task_type")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.page_task_type)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.page_task_type)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.stackedWidget.addWidget(self.page_task_type)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.page_4)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        AddTaskWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddTaskWindow)
        self.statusbar.setObjectName("statusbar")
        AddTaskWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddTaskWindow)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(4)
        self.pushButton_3.clicked.connect(AddTaskWindow.showMinimized) # type: ignore
        self.pushButton_4.clicked.connect(AddTaskWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AddTaskWindow)

    def retranslateUi(self, AddTaskWindow):
        _translate = QtCore.QCoreApplication.translate
        AddTaskWindow.setWindowTitle(_translate("AddTaskWindow", "MainWindow"))
        self.label.setText(_translate("AddTaskWindow", "新建任务"))
        self.lineEdit_Add_task_name.setPlaceholderText(_translate("AddTaskWindow", "任务名称："))
        self.textEdit_Add_task_content.setPlaceholderText(_translate("AddTaskWindow", "任务内容："))
        self.textEdit_Add_task_photo.setPlaceholderText(_translate("AddTaskWindow", "上传图片："))
        self.label_8.setText(_translate("AddTaskWindow", "是否是每日任务："))
        self.radioButton_Add_is_every.setText(_translate("AddTaskWindow", "是"))
        self.label_4.setText(_translate("AddTaskWindow", "开始时间："))
        self.label_5.setText(_translate("AddTaskWindow", "截止时间："))
        self.label_9.setText(_translate("AddTaskWindow", "开始日期："))
        self.label_11.setText(_translate("AddTaskWindow", "每日开始时间："))
        self.label_10.setText(_translate("AddTaskWindow", "截止日期："))
        self.label_12.setText(_translate("AddTaskWindow", "每日截止时间："))
        self.comboBox_important.setItemText(0, _translate("AddTaskWindow", "请选择重要等级"))
        self.comboBox_important.setItemText(1, _translate("AddTaskWindow", "不重要"))
        self.comboBox_important.setItemText(2, _translate("AddTaskWindow", "一般重要"))
        self.comboBox_important.setItemText(3, _translate("AddTaskWindow", "特别重要"))
        self.comboBox_Add_task_type.setItemText(0, _translate("AddTaskWindow", "请选择任务类型"))
        self.comboBox_Add_task_type.setItemText(1, _translate("AddTaskWindow", "学习"))
        self.comboBox_Add_task_type.setItemText(2, _translate("AddTaskWindow", "运动"))
        self.comboBox_Add_task_type.setItemText(3, _translate("AddTaskWindow", "生活"))
        self.comboBox_Add_task_type.setItemText(4, _translate("AddTaskWindow", "休闲娱乐"))
        self.comboBox_Add_task_type.setItemText(5, _translate("AddTaskWindow", "其他"))
        self.pushButton_Add_ensure.setText(_translate("AddTaskWindow", "确认"))
        self.label_2.setText(_translate("AddTaskWindow", "任务名称不能为空！"))
        self.label_3.setText(_translate("AddTaskWindow", "开始时间/日期不能晚于截止时间/日期！"))
        self.label_6.setText(_translate("AddTaskWindow", "请选择任务类型！"))
        self.label_7.setText(_translate("AddTaskWindow", "任务重要等级不能为空！"))
import resource_rc
