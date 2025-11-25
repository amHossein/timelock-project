from PySide6.QtWidgets import *
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QShortcut, QKeySequence
from timelock.ui import constants
from timelock.utils import load


class MaineWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.setFixedSize(QSize(constants.WINDOW_WIDTH,constants.WINDOW_HEIGHT))
        
        self.alignment_center = Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        
        self.setup_ui()
        self.setup_shortcuts()
        self.connect_signals()
    
    
    def setup_ui(self):
        centeral_widget = QLabel()
        centeral_widget.setPixmap(load.load_image("ui-f1.png"))
        centeral_widget.setAlignment(self.alignment_center)
        self.setCentralWidget(centeral_widget)
    
    
    def setup_shortcuts(self):
        self.shortcut_quit = QShortcut(QKeySequence("Ctrl+Q"), self)
    
    
    def connect_signals(self):
        self.shortcut_quit.activated.connect(self._on_quit)

    
    def _on_quit(self):
        print("Ctrl+Q Pressed - closing the app")
        QApplication.quit()
    
    
if __name__ == "__main__":
    app = QApplication([])
    
    window = MaineWindow()
    window.show()
    
    app.exec()