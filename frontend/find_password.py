# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'find_password.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FindWindow(object):
    def setupUi(self, FindWindow):
        FindWindow.setObjectName("FindWindow")
        FindWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(FindWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(220, 100, 401, 441))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(361, 381))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 20, 135, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(135, 31))
        self.label.setStyleSheet("font: 20pt \"Agency FB\";")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(61, 71, 231, 291))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(231, 291))
        self.frame_2.setStyleSheet("QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_F_email_address = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_F_email_address.sizePolicy().hasHeightForWidth())
        self.lineEdit_F_email_address.setSizePolicy(sizePolicy)
        self.lineEdit_F_email_address.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_F_email_address.setText("")
        self.lineEdit_F_email_address.setObjectName("lineEdit_F_email_address")
        self.verticalLayout.addWidget(self.lineEdit_F_email_address)
        self.lineEdit_F_check = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_F_check.sizePolicy().hasHeightForWidth())
        self.lineEdit_F_check.setSizePolicy(sizePolicy)
        self.lineEdit_F_check.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_F_check.setObjectName("lineEdit_F_check")
        self.verticalLayout.addWidget(self.lineEdit_F_check)
        self.lineEdit_F_password1 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_F_password1.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_F_password1.setObjectName("lineEdit_F_password1")
        self.verticalLayout.addWidget(self.lineEdit_F_password1)
        self.lineEdit_F_password2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_F_password2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_F_password2.setObjectName("lineEdit_F_password2")
        self.verticalLayout.addWidget(self.lineEdit_F_password2)
        self.pushButton_F_ensure = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_F_ensure.setObjectName("pushButton_F_ensure")
        self.verticalLayout.addWidget(self.pushButton_F_ensure, 0, QtCore.Qt.AlignHCenter)
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setGeometry(QtCore.QRect(310, 0, 91, 41))
        self.frame_10.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_10)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/24gl-minimization.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/Close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_F_send = QtWidgets.QPushButton(self.frame)
        self.pushButton_F_send.setGeometry(QtCore.QRect(290, 90, 75, 30))
        self.pushButton_F_send.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_F_send.setStyleSheet("QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.pushButton_F_send.setObjectName("pushButton_F_send")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(60, 360, 231, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(231, 31))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_3)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 229, 30))
        self.stackedWidget.setMinimumSize(QtCore.QSize(229, 30))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_void = QtWidgets.QWidget()
        self.page_void.setObjectName("page_void")
        self.stackedWidget.addWidget(self.page_void)
        self.page_email_format_error = QtWidgets.QWidget()
        self.page_email_format_error.setObjectName("page_email_format_error")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_email_format_error)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.page_email_format_error)
        self.label_2.setMinimumSize(QtCore.QSize(211, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.stackedWidget.addWidget(self.page_email_format_error)
        self.page_check_invalid = QtWidgets.QWidget()
        self.page_check_invalid.setObjectName("page_check_invalid")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_check_invalid)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.page_check_invalid)
        self.label_3.setMinimumSize(QtCore.QSize(211, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.stackedWidget.addWidget(self.page_check_invalid)
        self.page_code_inconsistent = QtWidgets.QWidget()
        self.page_code_inconsistent.setObjectName("page_code_inconsistent")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_code_inconsistent)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.page_code_inconsistent)
        self.label_4.setMinimumSize(QtCore.QSize(211, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.stackedWidget.addWidget(self.page_code_inconsistent)
        self.page_check_error = QtWidgets.QWidget()
        self.page_check_error.setObjectName("page_check_error")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page_check_error)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.page_check_error)
        self.label_5.setMinimumSize(QtCore.QSize(211, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.stackedWidget.addWidget(self.page_check_error)
        self.page_not_blank = QtWidgets.QWidget()
        self.page_not_blank.setObjectName("page_not_blank")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.page_not_blank)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.page_not_blank)
        self.label_6.setMinimumSize(QtCore.QSize(211, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.stackedWidget.addWidget(self.page_not_blank)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(211, 30))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.stackedWidget.addWidget(self.page)
        FindWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FindWindow)
        self.statusbar.setObjectName("statusbar")
        FindWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FindWindow)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(FindWindow)

    def retranslateUi(self, FindWindow):
        _translate = QtCore.QCoreApplication.translate
        FindWindow.setWindowTitle(_translate("FindWindow", "MainWindow"))
        self.label.setText(_translate("FindWindow", "找回密码"))
        self.lineEdit_F_email_address.setPlaceholderText(_translate("FindWindow", "邮箱："))
        self.lineEdit_F_check.setPlaceholderText(_translate("FindWindow", "验证码："))
        self.lineEdit_F_password1.setPlaceholderText(_translate("FindWindow", "密码："))
        self.lineEdit_F_password2.setPlaceholderText(_translate("FindWindow", "确认密码："))
        self.pushButton_F_ensure.setText(_translate("FindWindow", "确认"))
        self.pushButton_F_send.setText(_translate("FindWindow", "发送验证码"))
        self.label_2.setText(_translate("FindWindow", "邮箱格式错误！"))
        self.label_3.setText(_translate("FindWindow", "验证码输入错误！"))
        self.label_4.setText(_translate("FindWindow", "两次密码输入不一致！"))
        self.label_5.setText(_translate("FindWindow", "验证码发送失败，请重试！"))
        self.label_6.setText(_translate("FindWindow", "密码不能为空！"))
        self.label_7.setText(_translate("FindWindow", "此邮箱未注册！"))
import res_rc
