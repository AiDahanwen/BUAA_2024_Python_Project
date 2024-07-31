# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display_task.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DisplayTaskWindow(object):
    def setupUi(self, DisplayTaskWindow):
        DisplayTaskWindow.setObjectName("DisplayTaskWindow")
        DisplayTaskWindow.setEnabled(True)
        DisplayTaskWindow.resize(965, 859)
        self.centralwidget = QtWidgets.QWidget(DisplayTaskWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(120, 10, 811, 831))
        self.frame.setStyleSheet("QFrame#frame{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 60, 181, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.frame_left = QtWidgets.QFrame(self.frame)
        self.frame_left.setGeometry(QtCore.QRect(50, 120, 451, 381))
        self.frame_left.setStyleSheet("QFrame#frame_left{\n"
"background-color: rgba(255, 255, 255, 150);\n"
"font: 11pt \"微软雅黑\";\n"
"}\n"
"")
        self.frame_left.setObjectName("frame_left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_left)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_name = QtWidgets.QFrame(self.frame_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_name.sizePolicy().hasHeightForWidth())
        self.frame_name.setSizePolicy(sizePolicy)
        self.frame_name.setObjectName("frame_name")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_name)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_name)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_display_taskname = QtWidgets.QLineEdit(self.frame_name)
        self.lineEdit_display_taskname.setObjectName("lineEdit_display_taskname")
        self.horizontalLayout.addWidget(self.lineEdit_display_taskname)
        self.verticalLayout.addWidget(self.frame_name)
        self.frame_name_2 = QtWidgets.QFrame(self.frame_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_name_2.sizePolicy().hasHeightForWidth())
        self.frame_name_2.setSizePolicy(sizePolicy)
        self.frame_name_2.setObjectName("frame_name_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_name_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_name_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.textEdit_task_content = QtWidgets.QTextEdit(self.frame_name_2)
        self.textEdit_task_content.setStyleSheet("font: 11pt \"微软雅黑\";")
        self.textEdit_task_content.setObjectName("textEdit_task_content")
        self.horizontalLayout_3.addWidget(self.textEdit_task_content)
        self.verticalLayout.addWidget(self.frame_name_2)
        self.frame_process = QtWidgets.QFrame(self.frame_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_process.sizePolicy().hasHeightForWidth())
        self.frame_process.setSizePolicy(sizePolicy)
        self.frame_process.setObjectName("frame_process")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_process)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame_process)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.progressBar_display_progress = QtWidgets.QProgressBar(self.frame_process)
        self.progressBar_display_progress.setStyleSheet("font: 87 9pt \"Arial Black\";")
        self.progressBar_display_progress.setProperty("value", 24)
        self.progressBar_display_progress.setObjectName("progressBar_display_progress")
        self.horizontalLayout_6.addWidget(self.progressBar_display_progress)
        self.verticalLayout.addWidget(self.frame_process)
        self.frame_status = QtWidgets.QFrame(self.frame_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_status.sizePolicy().hasHeightForWidth())
        self.frame_status.setSizePolicy(sizePolicy)
        self.frame_status.setObjectName("frame_status")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_status)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_status)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_dispaly_state = QtWidgets.QLabel(self.frame_status)
        self.label_dispaly_state.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(0, 0, 0);")
        self.label_dispaly_state.setObjectName("label_dispaly_state")
        self.horizontalLayout_2.addWidget(self.label_dispaly_state)
        self.verticalLayout.addWidget(self.frame_status)
        self.frame_mini_and_close = QtWidgets.QFrame(self.frame)
        self.frame_mini_and_close.setGeometry(QtCore.QRect(650, 0, 158, 41))
        self.frame_mini_and_close.setMinimumSize(QtCore.QSize(158, 41))
        self.frame_mini_and_close.setStyleSheet("QPushButton:hover{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.frame_mini_and_close.setObjectName("frame_mini_and_close")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_mini_and_close)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton = QtWidgets.QPushButton(self.frame_mini_and_close)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton.setStyleSheet("border:none")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/24gl-minimization.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_8.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_mini_and_close)
        self.pushButton_2.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_2.setStyleSheet("border:none")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_8.addWidget(self.pushButton_2)
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(530, 120, 231, 151))
        self.label_15.setStyleSheet("background-color: rgb(35, 65, 76);\n"
"font: 12pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setGeometry(QtCore.QRect(510, 320, 241, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_16 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_12.addWidget(self.label_16)
        self.comboBox_important = QtWidgets.QComboBox(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.comboBox_important.setFont(font)
        self.comboBox_important.setObjectName("comboBox_important")
        self.comboBox_important.addItem("")
        self.comboBox_important.addItem("")
        self.comboBox_important.addItem("")
        self.horizontalLayout_12.addWidget(self.comboBox_important)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setGeometry(QtCore.QRect(510, 380, 241, 49))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_17 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_14.addWidget(self.label_17)
        self.comboBox_display_task_type = QtWidgets.QComboBox(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_display_task_type.sizePolicy().hasHeightForWidth())
        self.comboBox_display_task_type.setSizePolicy(sizePolicy)
        self.comboBox_display_task_type.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.comboBox_display_task_type.setFont(font)
        self.comboBox_display_task_type.setDuplicatesEnabled(True)
        self.comboBox_display_task_type.setProperty("placeholderText", "")
        self.comboBox_display_task_type.setObjectName("comboBox_display_task_type")
        self.comboBox_display_task_type.addItem("")
        self.comboBox_display_task_type.addItem("")
        self.comboBox_display_task_type.addItem("")
        self.comboBox_display_task_type.addItem("")
        self.comboBox_display_task_type.addItem("")
        self.horizontalLayout_14.addWidget(self.comboBox_display_task_type)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setGeometry(QtCore.QRect(510, 438, 251, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_35 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_29.addWidget(self.label_35)
        self.checkBox_is_daily = QtWidgets.QCheckBox(self.frame_8)
        self.checkBox_is_daily.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.checkBox_is_daily.setFont(font)
        self.checkBox_is_daily.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_is_daily.setCheckable(True)
        self.checkBox_is_daily.setChecked(False)
        self.checkBox_is_daily.setObjectName("checkBox_is_daily")
        self.horizontalLayout_29.addWidget(self.checkBox_is_daily)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget_2.setGeometry(QtCore.QRect(50, 540, 711, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
        self.stackedWidget_2.setMinimumSize(QtCore.QSize(311, 88))
        self.stackedWidget_2.setStyleSheet("\n"
"background-color: rgba(255, 255, 255, 150);\n"
"border-radius:20px;\n"
"")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.layoutWidget = QtWidgets.QWidget(self.page_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 671, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(309, 36))
        self.frame_2.setStyleSheet("")
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(60, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border:none;")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.dateTimeEdit_ordinary_begin = QtWidgets.QDateTimeEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit_ordinary_begin.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit_ordinary_begin.setSizePolicy(sizePolicy)
        self.dateTimeEdit_ordinary_begin.setMinimumSize(QtCore.QSize(234, 40))
        self.dateTimeEdit_ordinary_begin.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(170, 170, 170);")
        self.dateTimeEdit_ordinary_begin.setObjectName("dateTimeEdit_ordinary_begin")
        self.horizontalLayout_9.addWidget(self.dateTimeEdit_ordinary_begin)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(309, 36))
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(60, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.dateTimeEdit_ordinary_end = QtWidgets.QDateTimeEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit_ordinary_end.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit_ordinary_end.setSizePolicy(sizePolicy)
        self.dateTimeEdit_ordinary_end.setMinimumSize(QtCore.QSize(234, 40))
        self.dateTimeEdit_ordinary_end.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(170, 170, 170);")
        self.dateTimeEdit_ordinary_end.setObjectName("dateTimeEdit_ordinary_end")
        self.horizontalLayout_10.addWidget(self.dateTimeEdit_ordinary_end)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.stackedWidget_2.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.layoutWidget_2 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 11, 671, 131))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.layoutWidget_2)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setContentsMargins(2, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.dateEdit_every_begin_date = QtWidgets.QDateEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_every_begin_date.sizePolicy().hasHeightForWidth())
        self.dateEdit_every_begin_date.setSizePolicy(sizePolicy)
        self.dateEdit_every_begin_date.setMinimumSize(QtCore.QSize(86, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateEdit_every_begin_date.setFont(font)
        self.dateEdit_every_begin_date.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(170, 170, 170);")
        self.dateEdit_every_begin_date.setObjectName("dateEdit_every_begin_date")
        self.horizontalLayout_11.addWidget(self.dateEdit_every_begin_date)
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(84, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.timeEdit_every_begin_time = QtWidgets.QTimeEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_every_begin_time.sizePolicy().hasHeightForWidth())
        self.timeEdit_every_begin_time.setSizePolicy(sizePolicy)
        self.timeEdit_every_begin_time.setMinimumSize(QtCore.QSize(56, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.timeEdit_every_begin_time.setFont(font)
        self.timeEdit_every_begin_time.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(170, 170, 170);")
        self.timeEdit_every_begin_time.setObjectName("timeEdit_every_begin_time")
        self.horizontalLayout_11.addWidget(self.timeEdit_every_begin_time)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.layoutWidget_2)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setContentsMargins(2, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        self.dateEdit_every_end_date = QtWidgets.QDateEdit(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_every_end_date.sizePolicy().hasHeightForWidth())
        self.dateEdit_every_end_date.setSizePolicy(sizePolicy)
        self.dateEdit_every_end_date.setMinimumSize(QtCore.QSize(86, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateEdit_every_end_date.setFont(font)
        self.dateEdit_every_end_date.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(170, 170, 170);")
        self.dateEdit_every_end_date.setObjectName("dateEdit_every_end_date")
        self.horizontalLayout_13.addWidget(self.dateEdit_every_end_date)
        self.label_14 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(84, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.timeEdit_every_end_time = QtWidgets.QTimeEdit(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_every_end_time.sizePolicy().hasHeightForWidth())
        self.timeEdit_every_end_time.setSizePolicy(sizePolicy)
        self.timeEdit_every_end_time.setMinimumSize(QtCore.QSize(56, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.timeEdit_every_end_time.setFont(font)
        self.timeEdit_every_end_time.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"color: rgb(170, 170, 170);")
        self.timeEdit_every_end_time.setObjectName("timeEdit_every_end_time")
        self.horizontalLayout_13.addWidget(self.timeEdit_every_end_time)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.stackedWidget_2.addWidget(self.page_3)
        self.pushButton_display_ensure = QtWidgets.QPushButton(self.frame)
        self.pushButton_display_ensure.setGeometry(QtCore.QRect(54, 710, 701, 41))
        self.pushButton_display_ensure.setStyleSheet("\n"
"background-color: rgb(35, 63, 74);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"微软雅黑\";\n"
"border-radius:15px;\n"
"")
        self.pushButton_display_ensure.setObjectName("pushButton_display_ensure")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 811, 41))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-right-radius:20px;\n"
"border-top-left-radius:20px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(501, 320, 261, 181))
        self.label_8.setStyleSheet("background-color: rgba(255, 255, 255, 150);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 280, 211, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border:none")
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget_wrong = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget_wrong.setGeometry(QtCore.QRect(99, 770, 621, 41))
        self.stackedWidget_wrong.setStyleSheet("background-color:rgba(0, 0, 0, 0)")
        self.stackedWidget_wrong.setObjectName("stackedWidget_wrong")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget_wrong.addWidget(self.page)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_18 = QtWidgets.QLabel(self.page_4)
        self.label_18.setGeometry(QtCore.QRect(10, 10, 591, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.stackedWidget_wrong.addWidget(self.page_4)
        self.label_8.raise_()
        self.label.raise_()
        self.frame_left.raise_()
        self.label_15.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.frame_8.raise_()
        self.stackedWidget_2.raise_()
        self.pushButton_display_ensure.raise_()
        self.label_5.raise_()
        self.pushButton_3.raise_()
        self.frame_mini_and_close.raise_()
        self.stackedWidget_wrong.raise_()
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 14, 811, 821))
        self.label_7.setStyleSheet("border-image: url(:/pictures/pictures/login_background.jpg);\n"
"border-radius:20px;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.frame.raise_()
        DisplayTaskWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DisplayTaskWindow)
        self.statusbar.setObjectName("statusbar")
        DisplayTaskWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DisplayTaskWindow)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_wrong.setCurrentIndex(1)
        self.pushButton.clicked.connect(DisplayTaskWindow.showMinimized) # type: ignore
        self.pushButton_2.clicked.connect(DisplayTaskWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DisplayTaskWindow)

    def retranslateUi(self, DisplayTaskWindow):
        _translate = QtCore.QCoreApplication.translate
        DisplayTaskWindow.setWindowTitle(_translate("DisplayTaskWindow", "MainWindow"))
        self.label.setText(_translate("DisplayTaskWindow", "任务详情"))
        self.label_2.setText(_translate("DisplayTaskWindow", "任务名称   "))
        self.label_3.setText(_translate("DisplayTaskWindow", "任务内容   "))
        self.textEdit_task_content.setHtml(_translate("DisplayTaskWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_6.setText(_translate("DisplayTaskWindow", "任务进度   "))
        self.label_4.setText(_translate("DisplayTaskWindow", "任务状态"))
        self.label_dispaly_state.setText(_translate("DisplayTaskWindow", "已完成"))
        self.label_15.setText(_translate("DisplayTaskWindow", "未添加任务图片"))
        self.label_16.setText(_translate("DisplayTaskWindow", "重要程度"))
        self.comboBox_important.setItemText(0, _translate("DisplayTaskWindow", "不重要"))
        self.comboBox_important.setItemText(1, _translate("DisplayTaskWindow", "一般重要"))
        self.comboBox_important.setItemText(2, _translate("DisplayTaskWindow", "特别重要"))
        self.label_17.setText(_translate("DisplayTaskWindow", "任务类型"))
        self.comboBox_display_task_type.setItemText(0, _translate("DisplayTaskWindow", "学习"))
        self.comboBox_display_task_type.setItemText(1, _translate("DisplayTaskWindow", "运动"))
        self.comboBox_display_task_type.setItemText(2, _translate("DisplayTaskWindow", "生活"))
        self.comboBox_display_task_type.setItemText(3, _translate("DisplayTaskWindow", "休闲娱乐"))
        self.comboBox_display_task_type.setItemText(4, _translate("DisplayTaskWindow", "其他"))
        self.label_35.setText(_translate("DisplayTaskWindow", "是否是每日任务     "))
        self.checkBox_is_daily.setText(_translate("DisplayTaskWindow", "是"))
        self.label_9.setText(_translate("DisplayTaskWindow", "开始时间："))
        self.label_10.setText(_translate("DisplayTaskWindow", "截止时间："))
        self.label_11.setText(_translate("DisplayTaskWindow", "开始日期："))
        self.label_12.setText(_translate("DisplayTaskWindow", "  每日开始时间："))
        self.label_13.setText(_translate("DisplayTaskWindow", "截止日期："))
        self.label_14.setText(_translate("DisplayTaskWindow", "  每日截止时间："))
        self.pushButton_display_ensure.setText(_translate("DisplayTaskWindow", "确认"))
        self.pushButton_3.setText(_translate("DisplayTaskWindow", "修改图片"))
        self.label_18.setText(_translate("DisplayTaskWindow", "截止时间不能早于当前时间！"))
import frontend.res_rc
