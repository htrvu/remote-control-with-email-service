import sys
from PyQt5.QtWidgets import QApplication

from ui.config_window import ConfigWindow
from ui.tray_icon import TrayIcon
from mail_service import MailService

from utils import *
from thread_targets import *
import app_logging as logging

class RemoteControl():
    def __init__(self):
        self.app = QApplication(sys.argv)
        QApplication.setQuitOnLastWindowClosed(False)

        self.config_window = ConfigWindow()
        self.tray_icon = TrayIcon('ui/assets/icons/remote_tray.png', parent=self.app)
        self.host_mail = None

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
        
        try:
            print_color('Login to mail server...', text_format.OKGREEN)
            logging.log('Login to mail server...')
            self.host_mail = MailService()
            self.host_mail.login(REMOTE_MAIL, REMOTE_PWD)
            print_color('Login successfully', text_format.OKGREEN)
        except Exception as e:
            print_color('Failed to login with login with name: ' + REMOTE_MAIL, text_format.YELLOW)
            print_color('Full detail below:', text_format.YELLOW)
            
            logging.log(f'Failed to login with login with name: {REMOTE_MAIL}\nTraceback: \n{e}')
            
            print_indent(str(e), level = 1, option = text_format.RED)
            exit(1)
        
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
                logging.log('Logout mail server...')
                self.host_mail.logout()
            except:
                logging.log('Exceptinon raised white loging out')
                pass
        
        logging.log('App close')
        logging.save()
        sys.exit()
