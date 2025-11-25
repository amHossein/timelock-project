from PySide6.QtWidgets import QApplication
from timelock.ui.main_window import MaineWindow


def main():
    print(".: welcome to timelock :.")
    app = QApplication([])
    
    window = MaineWindow()
    window.show()
    
    app.exec()
    
    

if __name__ == "__main__":
    main()