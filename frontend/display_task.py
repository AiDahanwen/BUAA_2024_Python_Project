# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display_task.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DisplayTaskWindow(object):
    def setupUi(self, DisplayTaskWindow):
        DisplayTaskWindow.setObjectName("DisplayTaskWindow")
        DisplayTaskWindow.resize(800, 652)
        self.centralwidget = QtWidgets.QWidget(DisplayTaskWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(150, 30, 491, 551))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 10, 151, 41))
        self.label.setStyleSheet("font: 75 20pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.frame1 = QtWidgets.QFrame(self.frame)
        self.frame1.setGeometry(QtCore.QRect(30, 50, 441, 491))
        self.frame1.setObjectName("frame1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame2 = QtWidgets.QFrame(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy)
        self.frame2.setObjectName("frame2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_display_taskname = QtWidgets.QLineEdit(self.frame2)
        self.lineEdit_display_taskname.setObjectName("lineEdit_display_taskname")
        self.horizontalLayout.addWidget(self.lineEdit_display_taskname)
        self.verticalLayout.addWidget(self.frame2)
        self.frame3 = QtWidgets.QFrame(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame3.sizePolicy().hasHeightForWidth())
        self.frame3.setSizePolicy(sizePolicy)
        self.frame3.setObjectName("frame3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.frame3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.comboBox_important = QtWidgets.QComboBox(self.frame3)
        self.comboBox_important.setObjectName("comboBox_important")
        self.comboBox_important.addItem("")
        self.comboBox_important.addItem("")
        self.comboBox_important.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_important)
        self.verticalLayout.addWidget(self.frame3)
        self.frame4 = QtWidgets.QFrame(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame4.sizePolicy().hasHeightForWidth())
        self.frame4.setSizePolicy(sizePolicy)
        self.frame4.setObjectName("frame4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.textEdit_task_content = QtWidgets.QTextEdit(self.frame4)
        self.textEdit_task_content.setObjectName("textEdit_task_content")
        self.horizontalLayout_3.addWidget(self.textEdit_task_content)
        self.verticalLayout.addWidget(self.frame4)
        self.frame5 = QtWidgets.QFrame(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame5.sizePolicy().hasHeightForWidth())
        self.frame5.setSizePolicy(sizePolicy)
        self.frame5.setObjectName("frame5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.comboBox_display_task_type = QtWidgets.QComboBox(self.frame5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_display_task_type.sizePolicy().hasHeightForWidth())
        self.comboBox_display_task_type.setSizePolicy(sizePolicy)
        self.comboBox_display_task_type.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_display_task_type.setPlaceholderText("")
        self.comboBox_display_task_type.setDuplicatesEnabled(True)
        self.comboBox_display_task_type.setObjectName("comboBox_display_task_type")
        self.comboBox_display_task_type.addItem("")
        self.comboBox_display_task_type.addItem("")
        self.comboBox_display_task_type.addItem("")
        self.comboBox_display_task_type.addItem("")
        self.comboBox_display_task_type.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_display_task_type)
        self.verticalLayout.addWidget(self.frame5)
        self.frame6 = QtWidgets.QFrame(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame6.sizePolicy().hasHeightForWidth())
        self.frame6.setSizePolicy(sizePolicy)
        self.frame6.setObjectName("frame6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame6)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.progressBar_display_progress = QtWidgets.QProgressBar(self.frame6)
        self.progressBar_display_progress.setProperty("value", 24)
        self.progressBar_display_progress.setObjectName("progressBar_display_progress")
        self.horizontalLayout_6.addWidget(self.progressBar_display_progress)
        self.verticalLayout.addWidget(self.frame6)
        self.frame7 = QtWidgets.QFrame(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame7.sizePolicy().hasHeightForWidth())
        self.frame7.setSizePolicy(sizePolicy)
        self.frame7.setObjectName("frame7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame7)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_dispaly_state = QtWidgets.QLabel(self.frame7)
        self.label_dispaly_state.setText("")
        self.label_dispaly_state.setObjectName("label_dispaly_state")
        self.horizontalLayout_2.addWidget(self.label_dispaly_state)
        self.verticalLayout.addWidget(self.frame7)
        self.frame8 = QtWidgets.QFrame(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame8.sizePolicy().hasHeightForWidth())
        self.frame8.setSizePolicy(sizePolicy)
        self.frame8.setObjectName("frame8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.frame8)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.radioButton_display_isimportant = QtWidgets.QRadioButton(self.frame8)
        self.radioButton_display_isimportant.setObjectName("radioButton_display_isimportant")
        self.horizontalLayout_7.addWidget(self.radioButton_display_isimportant)
        self.verticalLayout.addWidget(self.frame8)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame1)
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
        self.label_9.setStyleSheet("border:none;")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.dateTimeEdit_ordinary_begin = QtWidgets.QDateTimeEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit_ordinary_begin.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit_ordinary_begin.setSizePolicy(sizePolicy)
        self.dateTimeEdit_ordinary_begin.setMinimumSize(QtCore.QSize(234, 25))
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
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.dateTimeEdit_ordinary_end = QtWidgets.QDateTimeEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit_ordinary_end.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit_ordinary_end.setSizePolicy(sizePolicy)
        self.dateTimeEdit_ordinary_end.setMinimumSize(QtCore.QSize(234, 25))
        self.dateTimeEdit_ordinary_end.setObjectName("dateTimeEdit_ordinary_end")
        self.horizontalLayout_10.addWidget(self.dateTimeEdit_ordinary_end)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.stackedWidget_2.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.layoutWidget_2 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 1, 421, 101))
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
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.dateEdit_every_begin_date = QtWidgets.QDateEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_every_begin_date.sizePolicy().hasHeightForWidth())
        self.dateEdit_every_begin_date.setSizePolicy(sizePolicy)
        self.dateEdit_every_begin_date.setMinimumSize(QtCore.QSize(86, 25))
        self.dateEdit_every_begin_date.setObjectName("dateEdit_every_begin_date")
        self.horizontalLayout_11.addWidget(self.dateEdit_every_begin_date)
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(84, 30))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.timeEdit_every_begin_time = QtWidgets.QTimeEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_every_begin_time.sizePolicy().hasHeightForWidth())
        self.timeEdit_every_begin_time.setSizePolicy(sizePolicy)
        self.timeEdit_every_begin_time.setMinimumSize(QtCore.QSize(56, 25))
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
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        self.dateEdit_every_end_date = QtWidgets.QDateEdit(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_every_end_date.sizePolicy().hasHeightForWidth())
        self.dateEdit_every_end_date.setSizePolicy(sizePolicy)
        self.dateEdit_every_end_date.setMinimumSize(QtCore.QSize(86, 25))
        self.dateEdit_every_end_date.setObjectName("dateEdit_every_end_date")
        self.horizontalLayout_13.addWidget(self.dateEdit_every_end_date)
        self.label_14 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(84, 30))
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.timeEdit_every_end_time = QtWidgets.QTimeEdit(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_every_end_time.sizePolicy().hasHeightForWidth())
        self.timeEdit_every_end_time.setSizePolicy(sizePolicy)
        self.timeEdit_every_end_time.setMinimumSize(QtCore.QSize(56, 25))
        self.timeEdit_every_end_time.setObjectName("timeEdit_every_end_time")
        self.horizontalLayout_13.addWidget(self.timeEdit_every_end_time)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.stackedWidget_2.addWidget(self.page_3)
        self.verticalLayout.addWidget(self.stackedWidget_2)
        self.frame9 = QtWidgets.QFrame(self.frame)
        self.frame9.setGeometry(QtCore.QRect(330, -10, 158, 51))
        self.frame9.setMinimumSize(QtCore.QSize(158, 25))
        self.frame9.setStyleSheet("QPushButton:hover{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.frame9.setObjectName("frame9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame9)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton = QtWidgets.QPushButton(self.frame9)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_8.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame9)
        self.pushButton_2.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_8.addWidget(self.pushButton_2)
        DisplayTaskWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DisplayTaskWindow)
        self.statusbar.setObjectName("statusbar")
        DisplayTaskWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DisplayTaskWindow)
        self.stackedWidget_2.setCurrentIndex(1)
        self.pushButton.clicked.connect(DisplayTaskWindow.showMinimized) # type: ignore
        self.pushButton_2.clicked.connect(DisplayTaskWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DisplayTaskWindow)

    def retranslateUi(self, DisplayTaskWindow):
        _translate = QtCore.QCoreApplication.translate
        DisplayTaskWindow.setWindowTitle(_translate("DisplayTaskWindow", "MainWindow"))
        self.label.setText(_translate("DisplayTaskWindow", "任务详情"))
        self.label_2.setText(_translate("DisplayTaskWindow", "任务名称"))
        self.label_8.setText(_translate("DisplayTaskWindow", "重要程度"))
        self.comboBox_important.setItemText(0, _translate("DisplayTaskWindow", "不重要"))
        self.comboBox_important.setItemText(1, _translate("DisplayTaskWindow", "一般重要"))
        self.comboBox_important.setItemText(2, _translate("DisplayTaskWindow", "特别重要"))
        self.label_3.setText(_translate("DisplayTaskWindow", "任务内容"))
        self.label_5.setText(_translate("DisplayTaskWindow", "任务类型"))
        self.comboBox_display_task_type.setItemText(0, _translate("DisplayTaskWindow", "学习"))
        self.comboBox_display_task_type.setItemText(1, _translate("DisplayTaskWindow", "运动"))
        self.comboBox_display_task_type.setItemText(2, _translate("DisplayTaskWindow", "生活"))
        self.comboBox_display_task_type.setItemText(3, _translate("DisplayTaskWindow", "休闲娱乐"))
        self.comboBox_display_task_type.setItemText(4, _translate("DisplayTaskWindow", "其他"))
        self.label_6.setText(_translate("DisplayTaskWindow", "任务进度"))
        self.label_4.setText(_translate("DisplayTaskWindow", "任务状态"))
        self.label_7.setText(_translate("DisplayTaskWindow", "是否是每日任务"))
        self.radioButton_display_isimportant.setText(_translate("DisplayTaskWindow", "RadioButton"))
        self.label_9.setText(_translate("DisplayTaskWindow", "开始时间："))
        self.label_10.setText(_translate("DisplayTaskWindow", "截止时间："))
        self.label_11.setText(_translate("DisplayTaskWindow", "开始日期："))
        self.label_12.setText(_translate("DisplayTaskWindow", "每日开始时间："))
        self.label_13.setText(_translate("DisplayTaskWindow", "截止日期："))
        self.label_14.setText(_translate("DisplayTaskWindow", "每日截止时间："))
        self.pushButton.setText(_translate("DisplayTaskWindow", "最小化"))
        self.pushButton_2.setText(_translate("DisplayTaskWindow", "关闭"))