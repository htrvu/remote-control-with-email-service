from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget
import sys
import os

sys.path.append('..')

from ui.ui_configwindow import Ui_ConfigWindow
from ui.whitelist_dialog import WhiteListDialog
import global_variables
from ui.components.my_messagebox import MyMessageBox

from utils import *

class MySignals(QObject):
    open = pyqtSignal()
    run = pyqtSignal(bool)    # close_window flag
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

    def auto_run_setup(self):
        # running status
        self.is_running = False

        if global_variables.app_configs['auto_run']:
            self.__run(close = False)

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

    def __render_config(self):
        self.ui.basicList.clear()
        self.ui.advancedList.clear()

        for mail in global_variables.app_configs['white_list']['basic']:
            self.ui.basicList.addItem(mail)
        for mail in global_variables.app_configs['white_list']['advanced']:
            self.ui.advancedList.addItem(mail)
        self.ui.autoRunBox.setChecked(global_variables.app_configs['auto_run'])

    def __stacked_index_slots(self, index):
        return lambda : self.ui.stackedWidget.setCurrentIndex(index)

    def __set_btn_slots(self):
        # Menu buttons
        self.ui.insBtn.clicked.connect(self.__stacked_index_slots(1))
        self.ui.configBtn.clicked.connect(self.__open_config_page)  # the data represented in this page is just a 'copy' of self.config
        self.ui.aboutBtn.clicked.connect(self.__stacked_index_slots(3))
        self.ui.runBtn.clicked.connect(lambda: self.__run(True))
        self.ui.exitBtn.clicked.connect(self.__exit)

        # Configurations buttons
        self.ui.configSaveBtn.clicked.connect(self.__save_config)
        self.ui.basicAddBtn.clicked.connect(lambda: self.__add_controller_dialog(is_basic=True))
        self.ui.advancedAddBtn.clicked.connect(lambda: self.__add_controller_dialog(is_basic=False))
        self.ui.basicRemoveBtn.clicked.connect(lambda: self.__remove_controller(self.ui.basicList))
        self.ui.advancedRemoveBtn.clicked.connect(lambda: self.__remove_controller(self.ui.advancedList))

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

    def __add_controller(self, mail, is_basic=True):
        basic, advanced = [], []

        for i in range(self.ui.basicList.count()):
            basic.append(self.ui.basicList.item(i).text())
        for i in range(self.ui.advancedList.count()):
            advanced.append(self.ui.advancedList.item(i).text())
            
        if mail in basic: 
            msg = MyMessageBox(title='Error', msg='This controller is already in the basic list!', parent=self)
            msg.exec_()
        elif mail in advanced:
            msg = MyMessageBox(title='Error', msg='This controller is already in the advanced list!', parent=self)
            msg.exec_()
        else:
            if is_basic:
                self.ui.basicList.addItem(mail)
            else:
                self.ui.advancedList.addItem(mail)
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
            'auto_run': False
        }
        basic, advanced = [], []
    
        for i in range(self.ui.basicList.count()):
            basic.append(self.ui.basicList.item(i).text())
        for i in range(self.ui.advancedList.count()):
            advanced.append(self.ui.advancedList.item(i).text())

        new_configs['white_list']['basic'] = basic
        new_configs['white_list']['advanced'] = advanced
        new_configs['auto_run'] = self.ui.autoRunBox.isChecked()

        # Set new_configs to global config
        global_variables.app_configs = new_configs

        # Save the config file
        save_config(new_configs, global_variables.configs_file_path)

        if new_configs['auto_run']:
            is_running_with_script = sys.argv[0].endswith('.py')
            path = get_startup_path() + '\\' + 'RemoteControl.lnk'
            
            w_dir = global_variables.app_location
            icon = global_variables.app_location + '\\ui\\assets\\icons\\remote_logo.ico'
            
            if is_running_with_script:
                runner = 'python'
                argument = '"' + global_variables.app_location + "\\" + sys.argv[0] + '"'
            else:
                runner = 'cmd.exe'
                argument = f'/C "{sys.argv[0]}"'

            create_shortcut(path, runner, argument, w_dir, icon)
   
        else:
            path = get_startup_path() + '\\' + 'RemoteControl.lnk'
            if os.path.exists(path):
                os.remove(path)

        # Notify user
        msg = 'Configurations saved'
        if not self.is_running:
            msg += '! Let\'s RUN!'
        else:
            msg += ' and applied!'
        msg_box = MyMessageBox(msg=msg, parent=self)
        msg_box.exec_()

        self.ui.stackedWidget.setCurrentIndex(0)

    def __run(self, close = True):
        if self.is_running:
            self.background_setup(True)
        else:
            self.signals.run.emit(close)

    def background_setup(self, close_window):
        '''
            Close window for running background
        '''
        if not self.is_running:
            self.ui.runBtn.setText("Hide")
            self.is_running = True

        if close_window:
            self.close()

    def __exit(self):
        self.close()
        self.signals.exit.emit()

    def show(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        super(ConfigWindow, self).show()