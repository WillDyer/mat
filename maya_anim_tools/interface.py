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
    from shiboken6 import wrapInstance
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
    from shiboken2 import wrapInstance

import maya.cmds as cmds
import maya.mel as mel
from maya import OpenMayaUI as omui

# module imports
from user_interface.pages import buttons

mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QWidget)

class Interface(QWidget):
    def __init__(self, *args, **kwargs):
        super(Interface, self).__init__(*args, **kwargs)
        self.start_ui()

    def init_ui(self):
        self.setWindowTitle("12 Tools")

        # Set size policies
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.widget = QWidget(self)
        self.widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Set layout
        self.horizontal_layout = QHBoxLayout(self.widget)
        self.horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout.setSpacing(5)

        # Add a test button
        button = QPushButton("Test")
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.horizontal_layout.addWidget(button)

        # Embed widget
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.widget)
        self.setLayout(main_layout)

def start_ui():
    Workspacename = "12_tools"
    DEBUG = True
    TIME_SLIDER = mel.eval('getUIComponentToolBar("Time Slider", false)')
    
    if DEBUG is True and cmds.workspaceControl(Workspacename, query=True, exists=True) is True:
        cmds.deleteUI(Workspacename)
        print("DEBUG: deleted UI")

    if cmds.workspaceControl(Workspacename, query=True, exists=True) is False:
        cmds.workspaceControl(Workspacename,dtm=["bottom", False], ih=200, li=True, hp="fixed", tp=["east", True], floating=False, uiScript="") # RUN THIS FROM MAIN OR SOMETHING AND SHOULD BE LIKE IMPORT THIS SCRIPT
        cmds.workspaceControl(Workspacename, edit=True, dtc=( TIME_SLIDER ,"top"))
        
        print("Interface built...")
    else:
        cmds.workspaceControl(Workspacename, edit=True, restore=True)
        print("Interface restored...")

def main():
    ui = start_ui()
    return ui
