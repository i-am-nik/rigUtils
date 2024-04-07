'''#TODO : add the goddam logic'''

import maya.cmds as cmds

def add_offset_group(input):
    for object_name in input:
        if cmds.nodeType(object_name) == "Joint":
            add_offset_on_joint(object_name)
            
def add_offset_on_joint(input):
    print("Its a joint")        