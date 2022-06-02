from ast import Global
import sys
from PyQt5.QtWidgets import QApplication

from ui.config_window import ConfigWindow
from ui.tray_icon import TrayIcon
from mail_service import MailService

from utils import *
from thread_targets import *

class RemoteControl():
    def __init__(self, host_mail: MailService):
        self.app = QApplication(sys.argv)
        QApplication.setQuitOnLastWindowClosed(False)

        self.config_window = ConfigWindow()
        self.tray_icon = TrayIcon('ui/assets/icons/remote_tray.png', parent=self.app)
        self.host_mail = host_mail

        # Signals from ConfigWindow
        self.config_window.signals.run.connect(self.__run)
        self.config_window.signals.save.connect(self.__save)
        self.config_window.signals.exit.connect(self.exit)
        
        # Signals from TrayIcon
        self.tray_icon.signals.open.connect(self.config_window.show)
        self.tray_icon.signals.exit.connect(self.exit)

    def start(self):
        self.tray_icon.show()
        self.config_window.show()
        sys.exit(self.app.exec_())

    def __save(self):
        '''
            Re-setup the configuration, open new thread for the app
        '''
        # destroy thread self.checking_thread and start a new one
        # self.checking_thread.join()
        # self.checking_thread = threading.Thread(target = check_email_thread, args = (self.host_mail, ))
        # self.checking_thread.start()
        pass

    def __run(self):
        '''
            Run the app (first save time of configurations)
        '''
        # Start checking mail box and show notifications
        self.checking_thread = threading.Thread(target = check_email_thread, args = (self.host_mail, ))
        self.checking_thread.daemon = True
        self.checking_thread.start()
        self.noti_thread = threading.Thread(target = show_notification_thead, args = ())
        self.noti_thread.daemon = True
        self.noti_thread.start()

        # just print for demo
        print('Configurations:')
        print('Basic controllers:', GlobalVariables.app_configs['white_list']['basic'])
        print('Advanced controllers:', GlobalVariables.app_configs['white_list']['advanced'])
        print('Auto-run:', GlobalVariables.app_configs['auto_run'])
        print('----------------------------------------------')
        print('Starting application...')

    def exit(self):
        if self.host_mail:
            try:
                self.host_mail.logout()
            except:
                pass

        sys.exit()
