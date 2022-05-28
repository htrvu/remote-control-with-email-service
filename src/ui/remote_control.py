import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, QThread

from config_window import ConfigWindow
from tray_icon import TrayIcon

class RemoteControl():
    def __init__(self, show_config = True):
        app = QtWidgets.QApplication(sys.argv)
        QtWidgets.QApplication.setQuitOnLastWindowClosed(False)

        self.config_window = ConfigWindow()
        self.config_window.signals.exit.connect(self.exit)

        self.tray_icon = TrayIcon('./assets/icons/remote_logo.png', parent=app)
        self.tray_icon.signals.open.connect(self.show_config_window)
        self.tray_icon.signals.exit.connect(self.exit)
        self.tray_icon.show()

        if show_config == True:
            self.show_config_window()

        sys.exit(app.exec_())

    def show_config_window(self):
        self.config_window.show()

    def exit(self):
        sys.exit()
