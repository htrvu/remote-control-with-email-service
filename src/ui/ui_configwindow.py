# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_configwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfigWindow(object):
    def setupUi(self, ConfigWindow):
        ConfigWindow.setObjectName("ConfigWindow")
        ConfigWindow.resize(800, 600)
        ConfigWindow.setMinimumSize(QtCore.QSize(800, 600))
        ConfigWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icons/contact.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ConfigWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ConfigWindow)
        self.centralwidget.setStyleSheet("QPushButton {\n"
"    outline: none !important; \n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 16px;\n"
"    color: #333;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("QStackedWidget QWidget#homePage, QStackedWidget QWidget#insPage, QStackedWidget QWidget#configPage, QStackedWidget QWidget#aboutPage {\n"
"background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #C9D6FF,  stop:1 #E2E2E2);\n"
"}\n"
"/* stop:0 #acb6e5,  stop:1 #86fde8 */")
        self.stackedWidget.setObjectName("stackedWidget")
        self.homePage = QtWidgets.QWidget()
        self.homePage.setStyleSheet("")
        self.homePage.setObjectName("homePage")
        self.label = QtWidgets.QLabel(self.homePage)
        self.label.setGeometry(QtCore.QRect(0, 42, 800, 81))
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 36px;\n"
"color: #2d1299;\n"
"font-weight: bold;")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.homePage)
        self.widget.setGeometry(QtCore.QRect(275, 200, 250, 331))
        self.widget.setStyleSheet("QPushButton {\n"
"    background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #2d1299,  stop:1 #2980b9);\n"
"    padding: 10px 8px 12px 8px;\n"
"    font-size: 24px;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #8e2de2,  stop:1 #4a00e0);\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.insBtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.insBtn.setFont(font)
        self.insBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.insBtn.setStyleSheet("")
        self.insBtn.setObjectName("insBtn")
        self.verticalLayout_2.addWidget(self.insBtn)
        self.configBtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.configBtn.setFont(font)
        self.configBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.configBtn.setStyleSheet("")
        self.configBtn.setObjectName("configBtn")
        self.verticalLayout_2.addWidget(self.configBtn)
        self.aboutBtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.aboutBtn.setFont(font)
        self.aboutBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aboutBtn.setObjectName("aboutBtn")
        self.verticalLayout_2.addWidget(self.aboutBtn)
        self.runBtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.runBtn.setFont(font)
        self.runBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.runBtn.setObjectName("runBtn")
        self.verticalLayout_2.addWidget(self.runBtn)
        self.exitBtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.exitBtn.setFont(font)
        self.exitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitBtn.setObjectName("exitBtn")
        self.verticalLayout_2.addWidget(self.exitBtn)
        self.label_11 = QtWidgets.QLabel(self.homePage)
        self.label_11.setGeometry(QtCore.QRect(370, 122, 60, 50))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("remote_logo.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.homePage)
        self.label_12.setGeometry(QtCore.QRect(0, 550, 800, 31))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("font-size: 18px;\n"
"color: #2d1299;\n"
"font-weight: bold;")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.stackedWidget.addWidget(self.homePage)
        self.insPage = QtWidgets.QWidget()
        self.insPage.setObjectName("insPage")
        self.label_2 = QtWidgets.QLabel(self.insPage)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 800, 51))
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-size: 30px;\n"
"color: #2d1299;\n"
"font-weight: bold;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.insBack = QtWidgets.QPushButton(self.insPage)
        self.insBack.setGeometry(QtCore.QRect(300, 535, 200, 28))
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        self.insBack.setFont(font)
        self.insBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.insBack.setStyleSheet("QPushButton {\n"
"font-size: 20px;\n"
"color: #2d1299;\n"
"background-color: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #8e2de2;\n"
"}")
        self.insBack.setObjectName("insBack")
        self.insWidget = QtWidgets.QWidget(self.insPage)
        self.insWidget.setGeometry(QtCore.QRect(100, 99, 600, 421))
        self.insWidget.setStyleSheet("QWidget#insWidget {\n"
"    background-color: #fff;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 18px;\n"
"}")
        self.insWidget.setObjectName("insWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.insWidget)
        self.verticalLayout_4.setContentsMargins(16, 8, 16, 8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.insWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.stackedWidget.addWidget(self.insPage)
        self.configPage = QtWidgets.QWidget()
        self.configPage.setStyleSheet("")
        self.configPage.setObjectName("configPage")
        self.configBack = QtWidgets.QPushButton(self.configPage)
        self.configBack.setGeometry(QtCore.QRect(300, 542, 200, 28))
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        self.configBack.setFont(font)
        self.configBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.configBack.setStyleSheet("QPushButton {\n"
"font-size: 20px;\n"
"color: #2d1299;\n"
"background-color: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #8e2de2;\n"
"}")
        self.configBack.setObjectName("configBack")
        self.label_3 = QtWidgets.QLabel(self.configPage)
        self.label_3.setGeometry(QtCore.QRect(0, 30, 800, 51))
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-size: 30px;\n"
"color: #2d1299;\n"
"font-weight: bold;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.configWidget = QtWidgets.QWidget(self.configPage)
        self.configWidget.setGeometry(QtCore.QRect(100, 100, 600, 431))
        self.configWidget.setStyleSheet("QWidget#configWidget {\n"
"    background-color: #fff;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 18px;\n"
"}")
        self.configWidget.setObjectName("configWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.configWidget)
        self.verticalLayout_5.setContentsMargins(16, 8, 16, 8)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.configWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.stackedWidget.addWidget(self.configPage)
        self.aboutPage = QtWidgets.QWidget()
        self.aboutPage.setObjectName("aboutPage")
        self.label_4 = QtWidgets.QLabel(self.aboutPage)
        self.label_4.setGeometry(QtCore.QRect(0, 85, 800, 51))
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font-size: 30px;\n"
"color: #2d1299;\n"
"font-weight: bold;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.aboutWidget = QtWidgets.QWidget(self.aboutPage)
        self.aboutWidget.setGeometry(QtCore.QRect(100, 153, 600, 301))
        self.aboutWidget.setStyleSheet("QWidget#aboutWidget {\n"
"    background-color: #fff;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 18px;\n"
"}")
        self.aboutWidget.setObjectName("aboutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.aboutWidget)
        self.verticalLayout_3.setContentsMargins(16, 8, 16, 8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.aboutWidget)
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font-size: 24px;\n"
"color: #2d1299;\n"
"font-weight: bold;")
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.aboutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.widget_41 = QtWidgets.QWidget(self.aboutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.widget_41.setFont(font)
        self.widget_41.setObjectName("widget_41")
        self.formLayout = QtWidgets.QFormLayout(self.widget_41)
        self.formLayout.setContentsMargins(-1, 0, -1, -1)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.widget_42 = QtWidgets.QWidget(self.widget_41)
        self.widget_42.setObjectName("widget_42")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.widget_42)
        self.horizontalLayout_27.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem)
        self.label_114 = QtWidgets.QLabel(self.widget_42)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_114.setFont(font)
        self.label_114.setStyleSheet("font-weight: bold;")
        self.label_114.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_114.setObjectName("label_114")
        self.horizontalLayout_27.addWidget(self.label_114)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.widget_42)
        self.widget_43 = QtWidgets.QWidget(self.widget_41)
        self.widget_43.setObjectName("widget_43")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_43)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_115 = QtWidgets.QLabel(self.widget_43)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_115.setFont(font)
        self.label_115.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_115.setObjectName("label_115")
        self.verticalLayout_10.addWidget(self.label_115)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.widget_43)
        self.widget_45 = QtWidgets.QWidget(self.widget_41)
        self.widget_45.setObjectName("widget_45")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.widget_45)
        self.horizontalLayout_28.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem1)
        self.label_116 = QtWidgets.QLabel(self.widget_45)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_116.setFont(font)
        self.label_116.setStyleSheet("font-weight: bold;")
        self.label_116.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_116.setObjectName("label_116")
        self.horizontalLayout_28.addWidget(self.label_116)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.widget_45)
        self.widget_46 = QtWidgets.QWidget(self.widget_41)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.widget_46.setFont(font)
        self.widget_46.setObjectName("widget_46")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_46)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_117 = QtWidgets.QLabel(self.widget_46)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_117.setFont(font)
        self.label_117.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_117.setObjectName("label_117")
        self.verticalLayout_11.addWidget(self.label_117)
        self.label_123 = QtWidgets.QLabel(self.widget_46)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_123.setFont(font)
        self.label_123.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_123.setObjectName("label_123")
        self.verticalLayout_11.addWidget(self.label_123)
        self.label_124 = QtWidgets.QLabel(self.widget_46)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_124.setFont(font)
        self.label_124.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_124.setObjectName("label_124")
        self.verticalLayout_11.addWidget(self.label_124)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.widget_46)
        self.widget_47 = QtWidgets.QWidget(self.widget_41)
        self.widget_47.setObjectName("widget_47")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.widget_47)
        self.horizontalLayout_29.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem2)
        self.label_120 = QtWidgets.QLabel(self.widget_47)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_120.setFont(font)
        self.label_120.setStyleSheet("font-weight: bold;")
        self.label_120.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_120.setObjectName("label_120")
        self.horizontalLayout_29.addWidget(self.label_120)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.widget_47)
        self.label_7 = QtWidgets.QLabel(self.widget_41)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.verticalLayout_3.addWidget(self.widget_41)
        self.aboutBackBtn = QtWidgets.QPushButton(self.aboutPage)
        self.aboutBackBtn.setGeometry(QtCore.QRect(300, 465, 200, 28))
        font = QtGui.QFont()
        font.setFamily("SVN-Cookies")
        font.setPointSize(-1)
        self.aboutBackBtn.setFont(font)
        self.aboutBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aboutBackBtn.setStyleSheet("QPushButton {\n"
"font-size: 20px;\n"
"color: #2d1299;\n"
"background-color: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #8e2de2;\n"
"}")
        self.aboutBackBtn.setObjectName("aboutBackBtn")
        self.stackedWidget.addWidget(self.aboutPage)
        ConfigWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ConfigWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ConfigWindow)

    def retranslateUi(self, ConfigWindow):
        _translate = QtCore.QCoreApplication.translate
        ConfigWindow.setWindowTitle(_translate("ConfigWindow", "Digital Contact List"))
        self.label.setText(_translate("ConfigWindow", "Remote Control with Email Service"))
        self.insBtn.setText(_translate("ConfigWindow", "Instructions"))
        self.configBtn.setText(_translate("ConfigWindow", "Configurations"))
        self.aboutBtn.setText(_translate("ConfigWindow", "About Us"))
        self.runBtn.setText(_translate("ConfigWindow", "Run"))
        self.exitBtn.setText(_translate("ConfigWindow", "Exit"))
        self.label_12.setText(_translate("ConfigWindow", "Please read the Instruction carefully before running this app!"))
        self.label_2.setText(_translate("ConfigWindow", "Instructions"))
        self.insBack.setText(_translate("ConfigWindow", "Back to Home"))
        self.label_9.setText(_translate("ConfigWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Greeting from Group 8 - Hornors Program 2020, University of Science, VNUHCM. Thank you for using our application!</span></p><p><span style=\" font-size:11pt;\">Since you press the </span><span style=\" font-size:11pt; font-weight:600;\">Run</span><span style=\" font-size:11pt;\"> button below, your computer can be controlled by someone that is allowed by you!</span></p><p><span style=\" font-size:11pt; font-weight:600;\">How can they do that? </span><span style=\" font-size:11pt;\">using email, format of header,...</span></p><p><span style=\" font-size:11pt; font-weight:600;\">What things can they do with your device? </span><span style=\" font-size:11pt;\">summary of featues...</span></p><p><span style=\" font-size:11pt;\">The controllers can see all of commands by sending an email with header &quot;[R8GC] HELP&quot; to the host mail set by you.</span></p><p><span style=\" font-size:11pt; font-weight:600;\">Notice:</span><span style=\" font-size:11pt;\"> Before running this app, please go to </span><span style=\" font-size:11pt; font-weight:600;\">Configurations</span><span style=\" font-size:11pt;\"> to set up everything needed.</span></p><p><span style=\" font-size:11pt;\">(double click vào đây để chỉnh sửa)</span></p></body></html>"))
        self.configBack.setText(_translate("ConfigWindow", "Back to Home"))
        self.label_3.setText(_translate("ConfigWindow", "Configurations"))
        self.label_13.setText(_translate("ConfigWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">1. QLineEdit cho việc nhập host mail</span></p><p><span style=\" font-size:11pt;\">2. White list (các mail được phép điều khiển)</span></p><p><span style=\" font-size:11pt;\">2.1. Basic white Litst (không được dùng explorer, pc, registry)</span></p><p><span style=\" font-size:11pt;\">2.2. Vip while list (full các lệnh)</span></p><p><span style=\" font-size:11pt;\">Sử dụng QListWidget để hiển thị danh sách, thêm, xóa</span></p><p><span style=\" font-size:11pt;\">3. QCheckbox, khởi động cùng Window</span></p><p><span style=\" font-size:11pt;\">4. Button save</span></p></body></html>"))
        self.label_4.setText(_translate("ConfigWindow", "About Us"))
        self.label_6.setText(_translate("ConfigWindow", "Remote Control with Email Service"))
        self.label_5.setText(_translate("ConfigWindow", "This is our Final Project for Computer Networking Course\n"
"University of Science - VNUHCM"))
        self.label_114.setText(_translate("ConfigWindow", "Lecturers:"))
        self.label_115.setText(_translate("ConfigWindow", "Do Hoang Cuong"))
        self.label_116.setText(_translate("ConfigWindow", "Students:"))
        self.label_117.setText(_translate("ConfigWindow", "Hoang Trong Vu - 20120025"))
        self.label_123.setText(_translate("ConfigWindow", "Tran Ngoc Do - 20120057"))
        self.label_124.setText(_translate("ConfigWindow", "Tran Huu Thien - 20120584"))
        self.label_120.setText(_translate("ConfigWindow", "Class:"))
        self.label_7.setText(_translate("ConfigWindow", "CNTN20"))
        self.aboutBackBtn.setText(_translate("ConfigWindow", "Back to Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfigWindow = QtWidgets.QMainWindow()
    ui = Ui_ConfigWindow()
    ui.setupUi(ConfigWindow)
    ConfigWindow.show()
    sys.exit(app.exec_())

