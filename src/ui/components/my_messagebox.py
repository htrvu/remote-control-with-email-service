from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QLabel, QDialogButtonBox

class MyMessageBox(QMessageBox):
    def __init__(self, title = 'Message', msg = None, btn_titles = [], parent = None):
        super().__init__(parent)
        self.__btn_titles = btn_titles

        # Set center alignment
        grid_layout = self.layout()

        qt_msgboxex_icon_label = self.findChild(QLabel, "qt_msgboxex_icon_label")
        qt_msgboxex_icon_label.deleteLater()

        qt_msgbox_label = self.findChild(QLabel, "qt_msgbox_label")
        qt_msgbox_label.setAlignment(Qt.AlignCenter)
        grid_layout.removeWidget(qt_msgbox_label)

        qt_msgbox_buttonbox = self.findChild(QDialogButtonBox, "qt_msgbox_buttonbox")
        grid_layout.removeWidget(qt_msgbox_buttonbox)

        grid_layout.addWidget(qt_msgbox_label, 0, 0, alignment=Qt.AlignCenter)
        grid_layout.addWidget(qt_msgbox_buttonbox, 1, 0, alignment=Qt.AlignCenter)

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon('ui/assets/icons/remote_logo.png'))

        # text
        self.setText(msg)

        # Stylesheet
        self.setStyleSheet("QMessageBox {background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #C9D6FF,  stop:1 #E2E2E2); } QLabel {color: #2d1299; font-size: 20px; font-weight: bold;}")

        # button
        self.__create_btns()

    def __create_btns(self):
        btn_style = '''
    QPushButton {
        background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #2d1299,  stop:1 #2980b9);
        padding: 4px 16px;
        font-size: 18px;
        font-weight: bold;
        color: #fff;
        border: none;
        border-radius: 12px;
        outline: none;
    }

    QPushButton:hover {
        background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #8e2de2,  stop:1 #4a00e0);
    }
            '''
        
        if not self.__btn_titles:
            btn = self.addButton(MyMessageBox.Ok)
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.setStyleSheet(btn_style)
        else:
            for title in self.__btn_titles:
                btn = self.addButton(title, QMessageBox.AcceptRole)
                btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                btn.setStyleSheet(btn_style)


