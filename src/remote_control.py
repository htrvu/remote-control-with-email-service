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
        self.config_window.signals.exit.connect(self.exit)
        
        # Signals from TrayIcon
        self.tray_icon.signals.open.connect(self.config_window.show)
        self.tray_icon.signals.exit.connect(self.exit)

    def start(self):
        self.tray_icon.show()
        self.config_window.show()
        self.config_window.auto_run_setup()
        sys.exit(self.app.exec_())

    def __run(self):
        '''
            Run the app (first save time of configurations)
        '''
        # Start checking mail box and show notifications
        self.checking_thread = threading.Thread(target = check_email_thread, args = (self.host_mail, ))
        self.checking_thread.daemon = True
        self.checking_thread.start()
        self.noti_thread = threading.Thread(target = show_notification_thread, args = ())
        self.noti_thread.daemon = True
        self.noti_thread.start()

        # just print for demo
        # print('Configurations:')
        # print('Basic controllers:', global_variables.app_configs['white_list']['basic'])
        # print('Advanced controllers:', global_variables.app_configs['white_list']['advanced'])
        # print('Auto-run:', global_variables.app_configs['auto_run'])
        # print('----------------------------------------------')
        # print('Starting application...')

    def exit(self):
        if self.host_mail:
            try:
                self.host_mail.logout()
            except:
                pass

        sys.exit()
