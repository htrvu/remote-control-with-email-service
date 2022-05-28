from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject

from ui_configwindow import Ui_ConfigWindow

class MySignals(QObject):
    open = pyqtSignal()
    exit = pyqtSignal()

class ConfigWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ConfigWindow, self).__init__()
        self.ui = Ui_ConfigWindow()
        self.ui.setupUi(self)

        self.signals = MySignals()
        
        self.__set_btn_slots()

    def __set_btn_slots(self):
        # Exit button will emit exit signal for RemoteControl
        self.ui.exitBtn.clicked.connect(self.exit)


    def exit(self):
        self.signals.exit.emit()
        self.close()