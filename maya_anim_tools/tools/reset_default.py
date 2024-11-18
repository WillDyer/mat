import maya.cmds as cmds

class reset_values():
    def __init__(self):
        self.collect_data()

    def collect_data(self):
        ctrl_list = cmds.ls(sl=1)
        for ctrl in ctrl_list:
            keyable_attrs = cmds.listAttr(ctrl, keyable=True)
            if keyable_attrs:
                self.zero_value(ctrl, keyable_attrs)

    def zero_value(self, ctrl, keyable_attrs):
        for attr in keyable_attrs:
            cmds.setAttr(f"{self.ctrl}.{attr}", 0)