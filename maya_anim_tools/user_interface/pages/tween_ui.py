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

from tools import tweenmachine

module_list = [tweenmachine]
for module in module_list:
    importlib.reload(module)


class CreateTweenUI(QWidget):
    def __init__(self, parent_widget):
        super().__init__()
        self.interface = parent_widget
        if isinstance(self.interface, QHBoxLayout):
            tween_ui = tweenmachine.create_tweenmachine()

            self.tween_widget = QWidget()
            self.tween_layout = QHBoxLayout(self.tween_widget)
            self.tween_layout.setContentsMargins(0, 0, 0, 0)
            self.tween_layout.addWidget(tween_ui)
            self.interface.addWidget(self.tween_widget)
        else:
            raise TypeError(f"Expected self.interface to be a QWidget but got {type(self.interface)}")
        