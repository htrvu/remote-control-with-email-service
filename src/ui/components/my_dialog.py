from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel, QHBoxLayout

class MyDialog(QDialog):
    def __init__(self, title=None, msg=None, parent=None):
        super().__init__(parent)

        # Modal mode
        self.setModal(True)

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon('ui/assets/icons/remote_logo.png'))

        # Stylesheet
        self.setStyleSheet("QDialog {background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #C9D6FF,  stop:1 #E2E2E2); } QLabel {color: #2d1299; font-size: 18px; font-weight: bold;}")

        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.__layout = QHBoxLayout(self)
        self.__label = QLabel(self)
        self.__label.setText(msg)
        self.__label.setAlignment(Qt.AlignCenter)
        self.__label.adjustSize()
        self.__layout.addWidget(self.__label)

        # fix size
        self.setMaximumWidth(self.width())
        self.setMaximumHeight(self.height())
     