from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget
import sys

sys.path.append('..')

from ui.ui_configwindow import Ui_ConfigWindow
from ui.whitelist_dialog import WhiteListDialog

from ui.components.my_messagebox import MyMessageBox

class MySignals(QObject):
    open = pyqtSignal()
    run = pyqtSignal(dict)
    save_config = pyqtSignal()
    exit = pyqtSignal()

class ConfigWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ConfigWindow, self).__init__()
        self.ui = Ui_ConfigWindow()
        self.ui.setupUi(self)

        self.signals = MySignals()

        # Set default page to Home page
        self.ui.stackedWidget.setCurrentIndex(0)

        # Multiple selection for QListWidget
        self.ui.basicList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ui.advancedList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        self.__set_btn_slots()
        self.__load_instructions()
        self.__load_config()

    def __load_instructions(self):
        with open('ui/assets/docs/instructions.html') as f:
            content = f.read()
        self.ui.insScrollArea.setWidgetResizable(True)

        container = QWidget()
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel()
        label.setText(content)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        label.setFont(font)
        label.setAlignment(QtCore.Qt.AlignTop)
        label.setStyleSheet('background-color: white;')
        label.setWordWrap(True)
        layout.addWidget(label)

        self.ui.insScrollArea.setWidget(container)

    def __load_config(self):
        self.config = {
            'basic': [],
            'vip': [],
            'autorun': False
        }

        # Doc config tu file (neu co)
        # ...

    def __render_config(self):
        self.ui.basicList.clear()
        self.ui.advancedList.clear()

        for mail in self.config['basic']:
            self.ui.basicList.addItem(mail)
        for mail in self.config['vip']:
            self.ui.advancedList.addItem(mail)
        self.ui.autoRunBox.setChecked(self.config['autorun'])

    def __stacked_index_slots(self, index):
        return lambda : self.ui.stackedWidget.setCurrentIndex(index)

    def __set_btn_slots(self):
        # Menu buttons
        self.ui.insBtn.clicked.connect(self.__stacked_index_slots(1))
        self.ui.configBtn.clicked.connect(self.__open_config_page)  # the data represented in this page is just a 'copy' of self.config
        self.ui.aboutBtn.clicked.connect(self.__stacked_index_slots(3))
        self.ui.runBtn.clicked.connect(self.__run)
        self.ui.exitBtn.clicked.connect(self.__exit)

        # Configurations buttons
        self.ui.configSaveBtn.clicked.connect(self.__save_config)
        self.ui.basicAddBtn.clicked.connect(lambda: self.__add_controller_dialog(is_basic=True))
        self.ui.vipAddBtn.clicked.connect(lambda: self.__add_controller_dialog(is_basic=False))
        self.ui.basicRemoveBtn.clicked.connect(lambda: self.__remove_controller(self.ui.basicList))
        self.ui.vipRemoveBtn.clicked.connect(lambda: self.__remove_controller(self.ui.advancedList))

        # Back home buttons
        self.ui.insBackBtn.clicked.connect(self.__stacked_index_slots(0))
        self.ui.configBackBtn.clicked.connect(self.__stacked_index_slots(0))
        self.ui.aboutBackBtn.clicked.connect(self.__stacked_index_slots(0))

    def __open_config_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.__render_config()

    def __add_controller_dialog(self, is_basic = True):
        if is_basic:
            role = 'Basic Controller'
        else:
            role = 'Advanced Controller'
        self.__dialog = WhiteListDialog(role, self)
        self.__dialog.signals.added.connect(lambda mail: self.__add_controller(mail, is_basic))

    def __add_controller(self, mail, is_basic = True):
        if is_basic:
            c_list = self.config['basic']
            ui_list = self.ui.basicList
        else:
            c_list = self.config['vip']
            ui_list = self.ui.advancedList
        
        if mail in c_list:
            msg = MyMessageBox(title='Error', msg='This controller is already in the list!', parent=self)
            msg.exec_()
        else:
            c_list.append(mail)
            ui_list.addItem(mail)
            self.__dialog.close()

    def __remove_controller(self, controller_list : QtWidgets.QListWidget):
        selected = controller_list.selectedItems()
        if len(selected) == 0:
            msg = MyMessageBox(title='Error', msg='Please select controllers to remove!', parent=self)
            msg.exec_()
        for item in selected: 
            controller_list.takeItem(controller_list.row(item))

    def __save_config(self):
        # Get the configurations from UI
        new_configs = {
            'white_list': {},
            'autorun': False
        }
        basic, advanced = [], []

        for i in range(self.ui.basicList.count()):
            basic.append(self.ui.basicList.item(i).text())
        for i in range(self.ui.advancedList.count()):
            advanced.append(self.ui.advancedList.item(i).text())
        new_configs['white_list']['basic'] = basic
        new_configs['white_list']['advanced'] = advanced
        new_configs['autorun'] = self.ui.autoRunBox.isChecked()

        # Save to the config file
        # if autorun == True:
        #     create bash file for start up
        # else:
        #     remove bash file

        # Emit signal to application
        self.signals.save_config.emit()

        # Notify user
        msg = MyMessageBox(msg='Configurations saved successfully!', parent=self)
        msg.exec_()

        self.ui.stackedWidget.setCurrentIndex(0)

    def __run(self):
        self.close()
        self.signals.run.emit(self.config)

    def __exit(self):
        self.close()
        self.signals.exit.emit()

    def show(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        super(ConfigWindow, self).show()