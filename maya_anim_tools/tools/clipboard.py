import maya.cmds as cmds

class CopyNPaste():
    def __init__(self):
        self.data = {}
        self.copy()

    def copy(self):
        current_frame = int(cmds.currentTime(query=True))
        object = cmds.ls(sl=1)
        if object:
            object = object[0]

            if cmds.ls(object, st=True)[1] == "transform":
                all_attrs = cmds.listAttr(object, keyable=True, unlocked=True)
                for attr in all_attrs:
                    if cmds.keyframe(f"{object}.{attr}", query=True, keyframeCount=True) > 0:
                        if cmds.keyframe(f"{object}.{attr}", query=True, time=(current_frame,)):
                            print(attr)
                            attr_value = cmds.getAttr(f"{object}.{attr}")
                            tmp_data = {
                                "control": object,
                                "attr": attr,
                                "value": attr_value,
                                "frame": current_frame
                            }
                        
                            self.data[f"{object}_{current_frame}_{attr}"] = tmp_data
                            print(f"Copied {attr_value} on keyframe: {current_frame} to {object}.{attr}")
                    
            else:
                cmds.warning("Cannot copy item as is not a transform object or a blacklisted item")
        else:
            cmds.warning("No object selected.")

    def paste(self):
        if not self.data:
            cmds.warning("No data to paste.")
            return

        for key in self.data.values():
            current_frame = int(cmds.currentTime(query=True))
            cmds.setAttr(f"{key['control']}.{key['attr']}", key['value'])
            cmds.setKeyframe(f"{key['control']}.{key['attr']}")
            print(f"Pasted {key['value']} on keyframe: {current_frame} to {key['control']}.{key['attr']}")
