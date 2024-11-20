import maya.cmds as cmds


class create_cam():
    def __init__(self):
        self.find_cam()

    def find_cam(self):
        cameras = cmds.ls(type="transform")
        create_cam = False
        for cam in cameras:
            try:
                if cmds.attributeQuery("mat_cam", node=cam, exists=True):
                    self.remove_cam(camera=cam)
                else:
                    create_cam = True
            except TypeError:
                pass
        if create_cam:
            self.create_cam()

    def create_cam(self):
        object = cmds.ls(sl=1)[0]
        persp_cam = cmds.ls("persp")[0]
        follow_cam = cmds.duplicate(persp_cam, n="follow_cam")
        cmds.addAttr(follow_cam, ln="mat_cam", nn="mat_cam", at="enum", en="True")
        cmds.showHidden(follow_cam)
        constraint = cmds.parentConstraint(object, follow_cam, mo=True)[0]
        cmds.setAttr(f"{constraint}.hiddenInOutliner", 1)
        print(f"{follow_cam} created.")

    def remove_cam(self, camera):
        cmds.delete(camera)
        print(f"{camera} deleted.")