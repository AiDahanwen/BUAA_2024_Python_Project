# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'free_time.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FreeTimeWindow(object):
    def setupUi(self, FreeTimeWindow):
        FreeTimeWindow.setObjectName("FreeTimeWindow")
        FreeTimeWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FreeTimeWindow.sizePolicy().hasHeightForWidth())
        FreeTimeWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(FreeTimeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(170, 50, 271, 331))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 10, 211, 41))
        self.label_4.setMinimumSize(QtCore.QSize(211, 41))
        self.label_4.setStyleSheet("font: 75 20pt \"微软雅黑\";")
        self.label_4.setObjectName("label_4")
        self.pushButton_free_ensure = QtWidgets.QPushButton(self.frame)
        self.pushButton_free_ensure.setGeometry(QtCore.QRect(100, 280, 75, 23))
        self.pushButton_free_ensure.setObjectName("pushButton_free_ensure")
        self.frame1 = QtWidgets.QFrame(self.frame)
        self.frame1.setGeometry(QtCore.QRect(0, 60, 271, 61))
        self.frame1.setMinimumSize(QtCore.QSize(231, 51))
        self.frame1.setObjectName("frame1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame1)
        self.label_5.setMinimumSize(QtCore.QSize(269, 22))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame1)
        self.label_6.setMinimumSize(QtCore.QSize(269, 21))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 130, 191, 141))
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
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.doubleSpinBox_free_morning = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_free_morning.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_free_morning.setSizePolicy(sizePolicy)
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
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.doubleSpinBox_free_afternoon = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_free_afternoon.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_free_afternoon.setSizePolicy(sizePolicy)
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
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.doubleSpinBox_free_night = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_free_night.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_free_night.setSizePolicy(sizePolicy)
        self.doubleSpinBox_free_night.setDecimals(1)
        self.doubleSpinBox_free_night.setSingleStep(0.5)
        self.doubleSpinBox_free_night.setObjectName("doubleSpinBox_free_night")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_free_night)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        FreeTimeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FreeTimeWindow)
        self.statusbar.setObjectName("statusbar")
        FreeTimeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FreeTimeWindow)
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
