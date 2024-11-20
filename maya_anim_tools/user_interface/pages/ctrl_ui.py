import os
import importlib
import maya.cmds as cmds

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
    

class CtrlSetUI(QWidget):
    def __init__(self, parent_widget):
        super().__init__()
        self.interface = parent_widget
        if isinstance(self.interface, QHBoxLayout):
            self.ctrl_widget = QWidget()
            self.ctrl_layout = QHBoxLayout(self.ctrl_widget)
            self.ctrl_layout.setContentsMargins(0, 0, 0, 0)
        else:
            raise TypeError(f"Expected self.interface to be a QWidget but got {type(self.interface)}")
        
        self.create_add_button()

        self.interface.addWidget(self.ctrl_widget)

    def create_add_button(self):
        add_button = QPushButton()
        add_button.setObjectName("button_add")
        add_button.setIcon(QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images','add.png')))
        add_button.setIconSize(QSize(25, 25))
        add_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.ctrl_layout.addWidget(add_button)
        QObject.connect(add_button, SIGNAL("clicked()"), lambda: self.add_ctrl_set())

    def add_ctrl_set(self):
        def create_sub_button(button_name):
            button = QPushButton(button_name)
            button.setObjectName(f"button_{button_name}")
            button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            self.ctrl_layout.addWidget()

        result = cmds.promptDialog(
                    title='Rename Object',
                    message='Enter Button Name:',
                    button=['OK', 'Cancel'],
                    defaultButton='Confirm',
                    cancelButton='Cancel',
                    dismissString='Cancel')

        use_dialog = True
        if use_dialog is True:
            button_name = result
        else:
            button_name = selected_control # TMP

        create_sub_button(button_name)


    def ctrl_button_select(self):
        cmds.select()