import os
import importlib

try:
    from PySide6.QtCore import Qt, QSize, QObject, SIGNAL
    from PySide6.QtGui import QIcon
    from PySide6.QtWidgets import (QWidget,
                                   QVBoxLayout,
                                   QHBoxLayout,
                                   QPushButton,
                                   QScrollArea,
                                   QLabel,
                                   QSizePolicy,
                                   QLineEdit,
                                   QSpacerItem)
except ModuleNotFoundError:
    from PySide2.QtCore import Qt, QSize, QObject, SIGNAL
    from PySide2.QtGui import QIcon
    from PySide2.QtWidgets import (QWidget,
                                   QVBoxLayout,
                                   QHBoxLayout,
                                   QPushButton,
                                   QScrollArea,
                                   QLabel,
                                   QSizePolicy,
                                   QLineEdit,
                                   QSpacerItem)

from tools import reset_default

module_list = [reset_default]
for module in module_list: importlib.reload(module)


class CreateButtons(QWidget):
    def __init__(self, parent_widget):
        super().__init__()
        self.interface = parent_widget
        if isinstance(self.interface, QWidget):
            self.button_layout = QHBoxLayout(self.interface)
            self.button_layout.setContentsMargins(0, 0, 0, 0)
        else:
            raise TypeError(f"Expectec self.interface to be a QWidget but got {type(self.interface)}")
        
        L_spacer = QSpacerItem(20,40,QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button_layout.addSpacerItem(L_spacer)

        self.default_values()
        self.copy_pos()
        self.paste_pos()

        R_spacer = QSpacerItem(20,40,QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button_layout.addSpacerItem(R_spacer)

    def default_values(self):
        default_value = QPushButton()
        default_value.setObjectName("button_defaultvalue")
        default_value.setIcon(QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images','zero_out.png')))
        default_value.setIconSize(QSize(25, 25))
        default_value.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.button_layout.addWidget(default_value)
        QObject.connect(default_value, SIGNAL("clicked()"), lambda: reset_default.reset_values())
    
    def copy_pos(self):
        copy_position = QPushButton()
        copy_position.setObjectName("button_copyposition")
        copy_position.setIcon(QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'copy.png')))
        copy_position.setIconSize(QSize(25,25))
        copy_position.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.button_layout.addWidget(copy_position)

    def paste_pos(self):
        paste_position = QPushButton()
        paste_position.setObjectName("button_pasteposition")
        paste_position.setIcon(QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'paste.png')))
        paste_position.setIconSize(QSize(25,25))
        paste_position.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.button_layout.addWidget(paste_position)
