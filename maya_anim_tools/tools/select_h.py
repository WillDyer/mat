import maya.cmds as cmds

def select():    
    def check_object(child):
        children = cmds.listRelatives(child, shapes=True, fullPath=True)
        if not children:
           print(f"{child} is a Group not selecting")
           return
        else:
            shape_type = cmds.nodeType(children[0])
            if shape_type == "nurbsCurve":
                print(f"{child} is a Curve")
                return child
            elif shape_type == "mesh":
                print(f"{child} is a Mesh")
                return child
    
    selection = cmds.ls(selection=True, type="transform")[0]
    selected_objects = [selection]
    tree = cmds.listRelatives(selection, ad=True)
    for child in tree:
        item = check_object(child)
        selected_objects.append(item)

    cmds.select(selected_objects)
