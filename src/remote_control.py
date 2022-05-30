import sys
from PyQt5.QtWidgets import QApplication

from ui.config_window import ConfigWindow
from ui.tray_icon import TrayIcon

class RemoteControl():
    def __init__(self, show_config = True):
        app = QApplication(sys.argv)
        QApplication.setQuitOnLastWindowClosed(False)

        self.config_window = ConfigWindow()
        self.tray_icon = TrayIcon('ui/assets/icons/remote_logo.png', parent=app)

        # Signals from ConfigWindow
        self.config_window.signals.run.connect(self.__run)
        self.config_window.signals.exit.connect(self.exit)
        
        # Signals from TrayIcon
        self.tray_icon.signals.open.connect(self.config_window.show)
        self.tray_icon.signals.exit.connect(self.exit)

        # Show window and tray icon
        self.tray_icon.show()
        if show_config == True:
            self.config_window.show()

        sys.exit(app.exec_())

    def __run(self, config):
        '''
            `config` is a dictionary with these information:
                - Basic controllers: List of string
                - Vip controllers: List of string
                - Auto-run: boolean
        '''
        # run app
        # ...

        # just print for demo
        print('Configurations:')
        print('Basic controllers:', config['basic'])
        print('Vip controllers:', config['vip'])
        print('Auto-run:', config['autorun'])
        print('----------------------------------------------')
        print('Starting application...')

    def exit(self):
        sys.exit()
