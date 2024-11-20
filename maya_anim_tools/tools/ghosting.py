import maya.cmds as cmds


class ObjectGhosting():
    def __init__(self):
        self.check_ghost()

    def check_ghost(self):
        object = cmds.ls(sl=1)
        if object:
            self.object_shape = cmds.listRelatives(object, shapes=True)[0]
            if cmds.ls(object, st=True)[1] == "transform":
                ghost_status = cmds.getAttr(f"{self.object_shape}.ghosting")
                if ghost_status is True:
                    self.remove_ghost()
                elif ghost_status is False:
                    self.create_ghost()
                else:
                    cmds.warning("ghost_status returned unexpected value")
        else:
            cmds.warning("No object selected")

    def create_ghost(self):
        cmds.setAttr(f"{self.object_shape}.ghosting", 1)

    def remove_ghost(self):
        cmds.setAttr(f"{self.object_shape}.ghosting", 0)
