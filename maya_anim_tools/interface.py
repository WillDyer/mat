import weakref
import os
import sys
import importlib

import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMayaUI as omui

try:
    from PySide6 import QtCore
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
    from PySide2 import QtCore
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

from user_interface.pages import buttons

module_list = [buttons]
for module in module_list:
    importlib.reload(module)

def dock_window(dialog_class):
    try: cmds.deleteUI(dialog_class.CONTROL_NAME)
    except: pass

    TIME_SLIDER = mel.eval('getUIComponentToolBar("Time Slider", false)')

    main_control = cmds.workspaceControl(dialog_class.CONTROL_NAME,
                                         dtm=["bottom", False],
                                         ih=50,
                                         li=True,
                                         hp="fixed",
                                         tp=["east", True],
                                         floating=False,
                                         label = dialog_class.DOCK_LABEL_NAME
                                         )
    cmds.workspaceControl(dialog_class.CONTROL_NAME, edit=True, dtc=(TIME_SLIDER, "top"))
    
    control_widget = omui.MQtUtil.findControl(dialog_class.CONTROL_NAME)
    control_wrap = wrapInstance(int(control_widget), QWidget)
    
    control_wrap.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    win = dialog_class(control_wrap)
    
    cmds.evalDeferred(lambda *args: cmds.workspaceControl(main_control, e=True, rs=True))
    print("Inteface docked...")
    return win.run()


class AnimToolsInterface(QWidget):
    instances = list()
    CONTROL_NAME = '12_Tools'
    DOCK_LABEL_NAME = '12 Tools'

    def __init__(self, parent=None):
        super(AnimToolsInterface, self).__init__(parent)
   
        AnimToolsInterface.delete_instances()
        self.__class__.instances.append(weakref.proxy(self))

        self.window_name = self.CONTROL_NAME
        self.ui = parent
        self.main_layout = parent.layout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.init_ui()
        self.init_style()
        print("Interface built...")

    def init_ui(self):
        self.widget = QWidget()
        self.widget.setContentsMargins(5, 5, 5, 5)
        self.widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        """self.horizontal_layout = QHBoxLayout(self.widget)
        self.horizontal_layout.setContentsMargins(5, 5, 5, 5)
        self.horizontal_layout.setSpacing(5)"""

        buttons_instance = buttons.CreateButtons(parent_widget=self.widget)

        #horizontal_layout = QVBoxLayout(self)
        #horizontal_layout.addWidget(self.widget)
        
        self.main_layout.addWidget(self.widget)

    def init_style(self):
        stylesheet_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"user_interface","style","style.css")
        with open(stylesheet_path, "r") as file:
            stylesheet = file.read()
        self.ui.setStyleSheet(stylesheet)

    @staticmethod
    def delete_instances():
        for ins in AnimToolsInterface.instances:
            try:
                ins.setParent(None)
                ins.deleteLater()
            except:
                # ignore the actual parent has already been deleted by Maya
                pass

            AnimToolsInterface.instances.remove(ins)
            del ins

    def run(self):
        return self


def main():
    ui = dock_window(AnimToolsInterface)
