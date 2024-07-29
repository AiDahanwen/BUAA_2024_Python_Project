# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'free_time.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FreeTimeWindow(object):
    def setupUi(self, FreeTimeWindow):
        FreeTimeWindow.setObjectName("FreeTimeWindow")
        FreeTimeWindow.resize(994, 752)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FreeTimeWindow.sizePolicy().hasHeightForWidth())
        FreeTimeWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(FreeTimeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_whole = QtWidgets.QFrame(self.centralwidget)
        self.frame_whole.setGeometry(QtCore.QRect(200, 40, 471, 641))
        self.frame_whole.setStyleSheet("QFrame#frame_whole{\n"
"border-radius:20px;\n"
"    border-image: url(:/pictures/pictures/login_background.jpg);\n"
"}")
        self.frame_whole.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_whole.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_whole.setObjectName("frame_whole")
        self.label_4 = QtWidgets.QLabel(self.frame_whole)
        self.label_4.setGeometry(QtCore.QRect(30, 60, 221, 51))
        self.label_4.setMinimumSize(QtCore.QSize(211, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.pushButton_free_ensure = QtWidgets.QPushButton(self.frame_whole)
        self.pushButton_free_ensure.setGeometry(QtCore.QRect(60, 520, 351, 31))
        self.pushButton_free_ensure.setStyleSheet("background-color: rgb(31, 68, 53);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"微软雅黑\";")
        self.pushButton_free_ensure.setObjectName("pushButton_free_ensure")
        self.frame = QtWidgets.QFrame(self.frame_whole)
        self.frame.setGeometry(QtCore.QRect(50, 130, 371, 81))
        self.frame.setMinimumSize(QtCore.QSize(231, 51))
        self.frame.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMinimumSize(QtCore.QSize(269, 22))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setMinimumSize(QtCore.QSize(269, 21))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.layoutWidget = QtWidgets.QWidget(self.frame_whole)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 280, 371, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.doubleSpinBox_free_morning = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_free_morning.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_free_morning.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.doubleSpinBox_free_morning.setFont(font)
        self.doubleSpinBox_free_morning.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.doubleSpinBox_free_morning.setDecimals(1)
        self.doubleSpinBox_free_morning.setSingleStep(0.5)
        self.doubleSpinBox_free_morning.setObjectName("doubleSpinBox_free_morning")
        self.horizontalLayout.addWidget(self.doubleSpinBox_free_morning)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.doubleSpinBox_free_afternoon = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_free_afternoon.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_free_afternoon.setSizePolicy(sizePolicy)
        self.doubleSpinBox_free_afternoon.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.doubleSpinBox_free_afternoon.setDecimals(1)
        self.doubleSpinBox_free_afternoon.setSingleStep(0.5)
        self.doubleSpinBox_free_afternoon.setObjectName("doubleSpinBox_free_afternoon")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_free_afternoon)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.doubleSpinBox_free_night = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_free_night.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_free_night.setSizePolicy(sizePolicy)
        self.doubleSpinBox_free_night.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.doubleSpinBox_free_night.setDecimals(1)
        self.doubleSpinBox_free_night.setSingleStep(0.5)
        self.doubleSpinBox_free_night.setObjectName("doubleSpinBox_free_night")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_free_night)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_7 = QtWidgets.QLabel(self.frame_whole)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 471, 41))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:20px;\n"
"border-top-right-radius:20px;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_whole)
        self.label_8.setGeometry(QtCore.QRect(30, 120, 411, 501))
        self.label_8.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"border-radius:20px;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.frame_close_and_mini = QtWidgets.QFrame(self.frame_whole)
        self.frame_close_and_mini.setGeometry(QtCore.QRect(370, 0, 101, 41))
        self.frame_close_and_mini.setObjectName("frame_close_and_mini")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_close_and_mini)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_minimize = QtWidgets.QPushButton(self.frame_close_and_mini)
        self.pushButton_minimize.setStyleSheet("QPushButton#pushButton_minimize{\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"}")
        self.pushButton_minimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/24gl-minimization.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_minimize.setIcon(icon)
        self.pushButton_minimize.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_minimize.setObjectName("pushButton_minimize")
        self.horizontalLayout_4.addWidget(self.pushButton_minimize)
        self.pushButton_close = QtWidgets.QPushButton(self.frame_close_and_mini)
        self.pushButton_close.setStyleSheet("QPushButton#pushButton_close{\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"}")
        self.pushButton_close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon1)
        self.pushButton_close.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_4.addWidget(self.pushButton_close)
        self.stackedWidget_wrong = QtWidgets.QStackedWidget(self.frame_whole)
        self.stackedWidget_wrong.setGeometry(QtCore.QRect(50, 560, 371, 41))
        self.stackedWidget_wrong.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.stackedWidget_wrong.setObjectName("stackedWidget_wrong")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget_wrong.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(30, 20, 311, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(40, 92, 69);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.stackedWidget_wrong.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(30, 20, 301, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(56, 117, 83);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.stackedWidget_wrong.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_11 = QtWidgets.QLabel(self.page_4)
        self.label_11.setGeometry(QtCore.QRect(30, 10, 311, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(49, 97, 75);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.stackedWidget_wrong.addWidget(self.page_4)
        self.label_12 = QtWidgets.QLabel(self.frame_whole)
        self.label_12.setGeometry(QtCore.QRect(50, 220, 371, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(50, 114, 78);")
        self.label_12.setObjectName("label_12")
        self.label_8.raise_()
        self.label_4.raise_()
        self.pushButton_free_ensure.raise_()
        self.frame.raise_()
        self.layoutWidget.raise_()
        self.label_7.raise_()
        self.frame_close_and_mini.raise_()
        self.stackedWidget_wrong.raise_()
        self.label_12.raise_()
        FreeTimeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FreeTimeWindow)
        self.statusbar.setObjectName("statusbar")
        FreeTimeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FreeTimeWindow)
        self.stackedWidget_wrong.setCurrentIndex(1)
        self.pushButton_close.clicked.connect(FreeTimeWindow.close) # type: ignore
        self.pushButton_minimize.clicked.connect(FreeTimeWindow.showMinimized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(FreeTimeWindow)

    def retranslateUi(self, FreeTimeWindow):
        _translate = QtCore.QCoreApplication.translate
        FreeTimeWindow.setWindowTitle(_translate("FreeTimeWindow", "MainWindow"))
        self.label_4.setText(_translate("FreeTimeWindow", "空闲时长"))
        self.pushButton_free_ensure.setText(_translate("FreeTimeWindow", "确认"))
        self.label_5.setText(_translate("FreeTimeWindow", "请在下方填写今日的空闲时长，"))
        self.label_6.setText(_translate("FreeTimeWindow", "以小时为单位( •̀ ω •́ )✧"))
        self.label.setText(_translate("FreeTimeWindow", "上午："))
        self.label_2.setText(_translate("FreeTimeWindow", "下午："))
        self.label_3.setText(_translate("FreeTimeWindow", "晚上："))
        self.label_9.setText(_translate("FreeTimeWindow", "上午空闲时间不能超过最大空闲时间！"))
        self.label_10.setText(_translate("FreeTimeWindow", "下午空闲时间不能超过最大空闲时间！"))
        self.label_11.setText(_translate("FreeTimeWindow", "晚上空闲时间不能超过最大空闲时间！"))
        self.label_12.setText(_translate("FreeTimeWindow", "上午：06：00-12：00；下午：12：00-18：00；\n"
"晚上：18：00-23：30"))
import res_rc
