import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, QObject

sys.path.append('..')

from ui.ui_whitelistdialog import Ui_WhiteListDialog
from ui.components.my_messagebox import MyMessageBox

from utils import mail_validate

class MySignals(QObject):
    added = pyqtSignal(str)

class WhiteListDialog(QtWidgets.QDialog):
    def __init__(self, role, parent = None):
        super(WhiteListDialog, self).__init__(parent)
        self.ui = Ui_WhiteListDialog()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.signals = MySignals()

        self.ui.role.setText(role)
        self.ui.mail.clear()
        self.ui.mail.setFocus()

        self.ui.addBtn.clicked.connect(self.__add_controller)

        self.show()

    def __add_controller(self):
        mail = self.ui.mail.text()
        
        if not mail_validate(mail):
            msg_box = MyMessageBox('Error', 'Invalid email address!', parent = self)
            msg_box.exec_()
            return

        self.signals.added.emit(mail)
    



    
