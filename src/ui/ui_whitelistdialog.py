# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_whitelistdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontDatabase

import os

class Ui_WhiteListDialog(object):
    def setupUi(self, WhiteListDialog):
        WhiteListDialog.setObjectName("WhiteListDialog")
        WhiteListDialog.resize(400, 235)
        WhiteListDialog.setMinimumSize(QtCore.QSize(400, 235))
        WhiteListDialog.setMaximumSize(QtCore.QSize(400, 235))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/assets/icons/remote_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WhiteListDialog.setWindowIcon(icon)
        WhiteListDialog.setStyleSheet("QPushButton {\n"
"    outline: none !important; \n"
"}\n"
"\n"
"QDialog#WhiteListDialog {\n"
"background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #C9D6FF,  stop:1 #E2E2E2);\n"
"}\n"
"/* stop:0 #acb6e5,  stop:1 #86fde8 */")


        # Load font from assets
        fonts = os.listdir('ui/assets/fonts')
        FONTS_DICT = {}
        for font in fonts:
            name = font.replace('.ttf', '')
            id = QFontDatabase.addApplicationFont('ui/assets/fonts/' + font)
            family = QFontDatabase.applicationFontFamilies(id)[0]
            FONTS_DICT[name] = family

        self.label_2 = QtWidgets.QLabel(WhiteListDialog)
        self.label_2.setGeometry(QtCore.QRect(0, 9, 400, 51))
        font = QtGui.QFont()
        font = QtGui.QFont(FONTS_DICT['SVN-Cookies'])
        
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-size: 24px;\n"
"color: #2d1299;\n"
"font-weight: bold;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.configWidget = QtWidgets.QWidget(WhiteListDialog)
        self.configWidget.setGeometry(QtCore.QRect(45, 63, 310, 100))
        self.configWidget.setStyleSheet("QWidget#configWidget {\n"
"    background-color: #fff;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel, QLineEdit {\n"
"    font-size: 18px;\n"
"}")
        self.configWidget.setObjectName("configWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.configWidget)
        self.gridLayout.setContentsMargins(16, 16, 16, 16)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.configWidget)
        font = QtGui.QFont()
        font = QtGui.QFont(FONTS_DICT['Roboto'])
        
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.role = QtWidgets.QLabel(self.configWidget)
        font = QtGui.QFont()
        font = QtGui.QFont(FONTS_DICT['Roboto'])
        
        self.role.setFont(font)
        self.role.setObjectName("role")
        self.gridLayout.addWidget(self.role, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.configWidget)
        font = QtGui.QFont()
        font = QtGui.QFont(FONTS_DICT['Roboto'])
        
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.mail = QtWidgets.QLineEdit(self.configWidget)
        font = QtGui.QFont()
        font = QtGui.QFont(FONTS_DICT['Roboto'])
        
        self.mail.setFont(font)
        self.mail.setObjectName("mail")
        self.gridLayout.addWidget(self.mail, 1, 1, 1, 1)
        self.addBtn = QtWidgets.QPushButton(WhiteListDialog)
        self.addBtn.setGeometry(QtCore.QRect(160, 177, 80, 34))
        font = QtGui.QFont()
        font = QtGui.QFont(FONTS_DICT['SVN-Cookies'])
        
        self.addBtn.setFont(font)
        self.addBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addBtn.setStyleSheet("QPushButton {\n"
"    background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #2d1299,  stop:1 #2980b9);\n"
"    padding: 8px 14px;\n"
"     font-size: 18px;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #8e2de2,  stop:1 #4a00e0);\n"
"}")
        self.addBtn.setObjectName("addBtn")

        self.retranslateUi(WhiteListDialog)
        QtCore.QMetaObject.connectSlotsByName(WhiteListDialog)

    def retranslateUi(self, WhiteListDialog):
        _translate = QtCore.QCoreApplication.translate
        WhiteListDialog.setWindowTitle(_translate("WhiteListDialog", "WhiteListDialog"))
        self.label_2.setText(_translate("WhiteListDialog", "Add controller"))
        self.label.setText(_translate("WhiteListDialog", "Role:"))
        self.role.setText(_translate("WhiteListDialog", "Basic Controller"))
        self.label_4.setText(_translate("WhiteListDialog", "Email:"))
        self.addBtn.setText(_translate("WhiteListDialog", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WhiteListDialog = QtWidgets.QDialog()
    ui = Ui_WhiteListDialog()
    ui.setupUi(WhiteListDialog)
    WhiteListDialog.show()
    sys.exit(app.exec_())
