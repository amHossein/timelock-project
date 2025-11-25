from PySide6.QtGui import QPixmap
from pathlib import Path

PATH_IMG = Path(__file__).parent.parent / "assets" # go inside timelock first

def load_image(file_name:str):
    img = QPixmap(PATH_IMG / file_name)
    return img