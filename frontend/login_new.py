# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(922, 624)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 10, 761, 501))
        self.frame.setMinimumSize(QtCore.QSize(761, 501))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"QPushButton{\n"
"    border:none;\n"
"}\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setStyleSheet("border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_8)
        self.frame_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(380, 374))
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(1, -6, 381, 381))
        self.label_6.setStyleSheet("background-color:rgb(92, 132, 194);\n"
"image:url(images/login.jpg)")
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_L_daily_sentence = QtWidgets.QLabel(self.frame_4)
        self.label_L_daily_sentence.setGeometry(QtCore.QRect(23, 391, 341, 91))
        self.label_L_daily_sentence.setMinimumSize(QtCore.QSize(341, 91))
        self.label_L_daily_sentence.setObjectName("label_L_daily_sentence")
        self.verticalLayout_2.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setStyleSheet("")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.frame_2 = QtWidgets.QFrame(self.frame_9)
        self.frame_2.setGeometry(QtCore.QRect(10, 140, 350, 350))
        self.frame_2.setMinimumSize(QtCore.QSize(350, 350))
        self.frame_2.setStyleSheet("#frame_2{\n"
"    background-color: rgb(91, 130, 192);\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("background-color:none\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_L_account = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_L_account.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_L_account.setStyleSheet("border:1px solid gray;\n"
"border-radius:10px;")
        self.lineEdit_L_account.setText("")
        self.lineEdit_L_account.setObjectName("lineEdit_L_account")
        self.verticalLayout_3.addWidget(self.lineEdit_L_account)
        self.lineEdit_L_password = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_L_password.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_L_password.setStyleSheet("border:1px solid gray;\n"
"border-radius:10px;")
        self.lineEdit_L_password.setText("")
        self.lineEdit_L_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_L_password.setObjectName("lineEdit_L_password")
        self.verticalLayout_3.addWidget(self.lineEdit_L_password)
        self.pushButton_L_forget = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_L_forget.setStyleSheet("QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.pushButton_L_forget.setObjectName("pushButton_L_forget")
        self.verticalLayout_3.addWidget(self.pushButton_L_forget, 0, QtCore.Qt.AlignRight)
        self.pushButton_L_login = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_L_login.setObjectName("pushButton_L_login")
        self.verticalLayout_3.addWidget(self.pushButton_L_login, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_L_signup = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_L_signup.setObjectName("pushButton_L_signup")
        self.verticalLayout_3.addWidget(self.pushButton_L_signup, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_3)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
        self.stackedWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget_2.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.page_4)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.stackedWidget_2.addWidget(self.page_4)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.stackedWidget_2.addWidget(self.page)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.page_5)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.stackedWidget_2.addWidget(self.page_5)
        self.verticalLayout.addWidget(self.stackedWidget_2)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setGeometry(QtCore.QRect(260, 0, 121, 41))
        self.frame_10.setStyleSheet("background-color:rgb(81, 118, 172);\n"
"QPushButton{\n"
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
        self.label = QtWidgets.QLabel(self.frame_9)
        self.label.setGeometry(QtCore.QRect(30, 90, 341, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(251, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 20pt \"微软雅黑\";\n"
"background-color:rgba(0, 0, 0, 0);")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.frame_9)
        self.label_5.setGeometry(QtCore.QRect(1, -6, 381, 391))
        self.label_5.setStyleSheet("background-color:rgb(92, 132, 194)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.frame_2.raise_()
        self.frame_10.raise_()
        self.label.raise_()
        self.horizontalLayout_2.addWidget(self.frame_9)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        self.stackedWidget_2.setCurrentIndex(4)
        self.pushButton_2.clicked.connect(LoginWindow.close) # type: ignore
        self.pushButton.clicked.connect(LoginWindow.showMinimized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.label_L_daily_sentence.setText(_translate("LoginWindow", "此处放每日一句"))
        self.lineEdit_L_account.setPlaceholderText(_translate("LoginWindow", " 用户名/邮箱："))
        self.lineEdit_L_password.setPlaceholderText(_translate("LoginWindow", " 密码："))
        self.pushButton_L_forget.setText(_translate("LoginWindow", "忘记密码？"))
        self.pushButton_L_login.setText(_translate("LoginWindow", "登录"))
        self.pushButton_L_signup.setText(_translate("LoginWindow", "注册"))
        self.label_3.setText(_translate("LoginWindow", "用户名/邮箱或密码不能为空！"))
        self.label_4.setText(_translate("LoginWindow", "不存在此用户名/邮箱，请注册！"))
        self.label_2.setText(_translate("LoginWindow", "密码错误！"))
        self.label_7.setText(_translate("LoginWindow", "邮箱格式错误！"))
        self.label.setText(_translate("LoginWindow", "Welcome Back! :)"))
import res_rc