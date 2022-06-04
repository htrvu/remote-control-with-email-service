import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, pyqtSignal, QObject

from ui.config_window import ConfigWindow
from ui.components.my_dialog import MyDialog
from ui.components.my_messagebox import MyMessageBox
from ui.tray_icon import TrayIcon

from mail_service import MailService

from utils import *
from thread_targets import *
import app_logging as logging

class LoggingThread(QObject):
        ok = pyqtSignal(MailService)
        fail = pyqtSignal()
        finished = pyqtSignal()

        def __init__(self, host_mail: MailService):
            super(LoggingThread, self).__init__()
            self.host_mail = host_mail
    
        def start(self):
            print_color('Login to mail server...', text_format.OKGREEN)
            logging.log('Login to mail server...')
            status = self.host_mail.login(REMOTE_MAIL, REMOTE_PWD)
            
            if status:
                print_color('Login successfully', text_format.OKGREEN)
                logging.log('Login successfully')
                self.ok.emit(self.host_mail)
            else:
                print_color('Failed to login with login with name: ' + REMOTE_MAIL, text_format.YELLOW)                
                logging.log(f'Failed to login with login with name: {REMOTE_MAIL}')
                self.fail.emit()
            
            self.finished.emit()

class RemoteControl():
    def __init__(self):
        self.app = QApplication(sys.argv)
        QApplication.setQuitOnLastWindowClosed(False)

        self.host_mail = MailService()
        self.config_window = ConfigWindow()
        self.tray_icon = TrayIcon('ui/assets/icons/remote_tray.png', parent=self.app)

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

    def __run_thread(self, status, close_window):
        '''
            Run threads for app if status is True
            After that, the Run button will become Hide button, the config window will closed or not based on close_window
        '''
        self.__dialog.close()
        if status == True:
            # Start checking mail box and show notifications
            self.checking_thread = threading.Thread(target = check_email_thread, args = (self.host_mail, ))
            self.checking_thread.daemon = True
            self.checking_thread.start()
            self.noti_thread = threading.Thread(target = show_notification_thread, args = ())
            self.noti_thread.daemon = True
            self.noti_thread.start()
            self.config_window.background_setup(close_window)
        else:
            self.__show_msg('Cannot login to mail server. Please try again later.')

    def __run(self, close_window):
        '''
            Run the app (first run button click or auto-run)
        '''
        self.__dialog = MyDialog('Message', 'Logging in Mail Server...', self.config_window)
        self.__dialog.show()

        # create thread and start
        self.__thread = QThread()
        self.__target = LoggingThread(self.host_mail)
        self.__target.moveToThread(self.__thread)

        self.__thread.started.connect(self.__target.start)

        self.__target.finished.connect(self.__thread.quit)
        self.__target.ok.connect(lambda: self.__run_thread(True, close_window))
        self.__target.fail.connect(lambda: self.__run_thread(False, close_window))
        
        self.__thread.start()
        
    def __show_msg(self, msg):
        msg = MyMessageBox(msg=msg, parent=self.config_window)
        msg.exec_()

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
