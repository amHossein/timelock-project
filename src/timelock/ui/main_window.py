from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QShortcut, QKeySequence, QIntValidator
from timelock.ui import constants
from timelock.utils import load
from timelock.signals import signals


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.setGeometry(constants.WINDOW_X,constants.WINDOW_Y,constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
        
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
    
    def setup_widgets_entry(self, parent:QLabel):
        parent.WLineEditS = QLineEdit(parent)
        parent.WLineEditS.resize(constants.WENTRY_WIDTH,constants.WENTRY_HEIGHT)
        parent.WLineEditS.move(constants.WENTRY_S_POSX,constants.WENTRY_POSY)
        
        parent.WLineEditSS = QLineEdit(parent)
        parent.WLineEditSS.resize(constants.WENTRY_WIDTH,constants.WENTRY_HEIGHT)
        parent.WLineEditSS.move(constants.WENTRY_SS_POSX,constants.WENTRY_POSY)
        
        
        parent.WLineEditM = QLineEdit(parent)
        parent.WLineEditM.resize(constants.WENTRY_WIDTH,constants.WENTRY_HEIGHT)
        parent.WLineEditM.move(constants.WENTRY_M_POSX,constants.WENTRY_POSY)
        
        parent.WLineEditMM = QLineEdit(parent)
        parent.WLineEditMM.resize(constants.WENTRY_WIDTH,constants.WENTRY_HEIGHT)
        parent.WLineEditMM.move(constants.WENTRY_MM_POSX,constants.WENTRY_POSY)
        
        
        parent.WLineEditH = QLineEdit(parent)
        parent.WLineEditH.resize(constants.WENTRY_WIDTH,constants.WENTRY_HEIGHT)
        parent.WLineEditH.move(constants.WENTRY_H_POSX,constants.WENTRY_POSY)
        
        parent.WLineEditHH = QLineEdit(parent)
        parent.WLineEditHH.resize(constants.WENTRY_WIDTH,constants.WENTRY_HEIGHT)
        parent.WLineEditHH.move(constants.WENTRY_HH_POSX,constants.WENTRY_POSY)
        
        self.widgets_entries = [parent.WLineEditS, parent.WLineEditSS, parent.WLineEditM, parent.WLineEditMM, parent.WLineEditH, parent.WLineEditHH]

        

            
    def setup_ui(self):
        background = QLabel()
        background.setPixmap(load.load_image("ui-f1.png"))
        background.setAlignment(self.alignment_center)
        self.setCentralWidget(background)
        
        self.setup_widgets_entry(background)

        
        
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