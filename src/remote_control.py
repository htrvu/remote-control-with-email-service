import sys
from PyQt5.QtWidgets import QApplication

from ui.config_window import ConfigWindow
from ui.tray_icon import TrayIcon

class RemoteControl():
    def __init__(self, show_config = True):
        app = QApplication(sys.argv)
        QApplication.setQuitOnLastWindowClosed(False)

        self.config_window = ConfigWindow()
        self.tray_icon = TrayIcon('ui/assets/icons/remote_tray.png', parent=app)

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
                - white_list: list of basic and advanced controllers
                - autorun: boolean
        '''
        # run app
        # ...

        # just print for demo
        print('Configurations:')
        print('Basic controllers:', config['white_list']['basic'])
        print('Advanced controllers:', config['white_list']['advanced'])
        print('Auto-run:', config['autorun'])
        print('----------------------------------------------')
        print('Starting application...')

    def exit(self):
        sys.exit()
