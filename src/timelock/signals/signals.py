from PySide6.QtWidgets import *
from PySide6.QtGui import QShortcut


# Slots
def on_quit():
    print("Ctrl+Q Pressed - closing the app")
    QApplication.quit()
    

# Signals
def _shortcut_ctrl_q(parent:QShortcut):
    parent.activated.connect(on_quit)
    
