from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt

class CustomContextMenu:
    def __init__(self, widget: QWidget):
        self.widget = widget
        self.widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.widget.customContextMenuRequested.connect(self.show_menu)

    def show_menu(self):
        #Dummy
        return
