from PySide6.QtWidgets import *
from PySide6.QtCore import QSize, Qt, QPoint
from PySide6.QtGui import QShortcut, QKeySequence, QScreen
from timelock.ui import constants
from timelock.utils import load
from timelock.signals import signals


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.setGeometry(constants.WINDOW_X,constants.WINDOW_Y,constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
        #self.setFixedSize(QSize(constants.WINDOW_WIDTH,constants.WINDOW_HEIGHT))
        
        self.alignment_center = Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        
        self.setup_ui()
        self.setup_shortcuts()
        self.connect_signals()
        self._leftMouseState = False
        self._dragPos = QPoint()
        
    
    def mousePressEvent(self, event):    
        if event.button() == Qt.MouseButton.LeftButton:
            self._leftMouseState = True
            self._dragPos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            
        elif event.button() == Qt.MouseButton.RightButton:
            # handle the right-button press in here.
            pass
    
    def mouseMoveEvent(self, event):
        if self._leftMouseState:
            self.move(event.globalPosition().toPoint() - self._dragPos)
            
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._leftMouseState = False

        elif event.button() == Qt.MouseButton.RightButton:
            # handle the right-button press in here.
            pass
    
    def moveEvent(self, event):
        screen = self.screen().availableGeometry() 
        # rect of usable screen area left,top,right,bottom
        posx = self.x()
        posy = self.y()
        width = constants.WINDOW_WIDTH
        height = constants.WINDOW_HEIGHT
        
        if posx < screen.left():
            posx = screen.left()
        if posx + width > screen.right():
            posx = screen.right() - width
            
        if posy < screen.top():
            posy = screen.top()
        if posy + height > screen.bottom():
            posy = screen.bottom() - height
        
        self.move(posx,posy)
        
            
    def setup_ui(self):
        centeral_widget = QLabel()
        centeral_widget.setPixmap(load.load_image("ui-f1.png"))
        centeral_widget.setAlignment(self.alignment_center)
        self.setCentralWidget(centeral_widget)
    
    
    def setup_shortcuts(self):
        self.shortcut_quit = QShortcut(QKeySequence("Ctrl+Q"), self)
    
    
    def connect_signals(self):
        #self.shortcut_quit.activated.connect(self._on_quit)
        signals._shortcut_ctrl_q(self.shortcut_quit)

        
    

    
    
if __name__ == "__main__":
    app = QApplication([])
    
    window = MainWindow()
    window.show()
    
    app.exec()