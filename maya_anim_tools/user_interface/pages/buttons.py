try:
    from PySide6.QtCore import Qt
    from PySide6.QtGui import QIcon
    from PySide6.QtWidgets import (QWidget,
                                   QVBoxLayout,
                                   QHBoxLayout,
                                   QPushButton,
                                   QScrollArea,
                                   QLabel,
                                   QSizePolicy,
                                   QLineEdit)
except ModuleNotFoundError:
    from PySide2.QtCore import Qt
    from PySide2.QtGui import QIcon
    from PySide2.QtWidgets import (QWidget,
                                   QVBoxLayout,
                                   QHBoxLayout,
                                   QPushButton,
                                   QScrollArea,
                                   QLabel,
                                   QSizePolicy,
                                   QLineEdit)


class CreateButtons():
    def __init__(self, interface_layout):
        self.interface = interface_layout
        self.button_layout = QHBoxLayout(self.interface)
        
        self.default_value()

    def default_values(self):
        default_value = self.QPushButton("ZERO")
        self.button_layout.addWidget(default_value)
