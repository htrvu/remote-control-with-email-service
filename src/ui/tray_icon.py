from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal, QObject

class MySignals(QObject):
    open = pyqtSignal()
    exit = pyqtSignal()

class TrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon_path, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, QtGui.QIcon(icon_path), parent)
        self.__set_menu()
        self.signals = MySignals()

        self.activated.connect(self.__systemIcon)

    def __systemIcon(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.show_config_window()

    def __set_menu(self):
        menu = QtWidgets.QMenu()
        self.setContextMenu(menu)
        menu.addAction("Open Window", self.show_config_window)
        menu.addAction("Exit", self.exit)

    def show_config_window(self):
        self.signals.open.emit()

    def exit(self):
        self.signals.exit.emit()
