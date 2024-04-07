'''
interpJoint = InterpolationJoint("l_armJAroll_JNT", "l_armJB_JNT", "interpA").create_interpolation_joint()
'''
#TODO: Connect Interp Jonint and add bias, etc attrs, cleanup grouping

import maya.cmds as cmds

class InterpolationJoint:

    JOINTTYPE = "Interpolation Joint"
    ERROR1 = "Input must be a string"

    def __init__(self, parent_joint, movement_joint, joint_name):
        self._parent_joint = parent_joint
        self._movement_joint = movement_joint
        self._joint_name = joint_name

    @property
    def parent_joint(self):
        return self._parent_joint

    @parent_joint.setter
    def parent_joint(self, value):
        if isinstance(value, str):
            self._parent_joint = value
        else:
            raise ValueError(self.ERROR1)

    @property
    def movement_joint(self):
        return self._movement_joint

    @movement_joint.setter
    def movement_joint(self, value):
        if isinstance(value, str):
            self._movement_joint = value
        else:
            raise ValueError(self.ERROR1)

    @property
    def joint_name(self):
        return self._joint_name

    @joint_name.setter
    def joint_name(self, value):
        if isinstance(value, str):
            self._joint_name = value
        else:
            raise ValueError(self.ERROR1)

    def create_interpolation_joint(self):
        ref_locator = cmds.spaceLocator(name = (self._joint_name + '_ref_locator'))
        move_locator = cmds.spaceLocator(name = (self._joint_name + '_move_locator'))
        interp_locator = cmds.spaceLocator(name = (self._joint_name + '_interp_locator'))
        print(interp_locator)

        cmds.matchTransform(ref_locator,move_locator, interp_locator, self._movement_joint)
        cmds.parentConstraint(self._movement_joint, move_locator, mo=1)
        cmds.pointConstraint(self._movement_joint, ref_locator, mo=1)
        cmds.orientConstraint(self._parent_joint, ref_locator, mo=1)

        interp_joint = cmds.joint(name=(self._joint_name) + "_interp_joint")
        cmds.matchTransform(interp_joint,self._movement_joint)

        skeleton_group = cmds.group(em=1,world=1,name=(self._joint_name + "_skeleton_group"))

        if cmds.objExists('interpolationJoint_group'):
            main_group = 'interpolationJoint_group'
        else:    
            main_group = cmds.group(world=1,name='interpolationJoint_group')

        parts_group = cmds.group(ref_locator, move_locator, interp_locator, name=(self.joint_name + '_parts_group'))

        smart_constraint = cmds.createNode('cMuscleSmartConstraint')

        cmds.connectAttr((self._parent_joint + ".worldMatrix"), (smart_constraint + ".worldMatrixA"))
        cmds.connectAttr((self._movement_joint + ".worldMatrix"), (smart_constraint + ".worldMatrixB"))
        cmds.connectAttr((smart_constraint + ".outTranslate"), (interp_locator[0] + ".t"))
        cmds.connectAttr((smart_constraint + ".outRotate"), (interp_locator[0] + ".r"))
        
        cmds.pointConstraint(self._movement_joint,interp_joint)
        cmds.orientConstraint(interp_locator,interp_joint)
        
        cmds.setAttr((parts_group + '.v'), 0)
        cmds.setAttr((interp_joint + '.radi'), 2*cmds.getAttr(self._movement_joint + '.radi'))
        cmds.setAttr((interp_joint + '.overrideEnabled'), 1)
        cmds.setAttr((interp_joint + '.overrideColor'), 6)

        cmds.parent(skeleton_group, parts_group, main_group)
        cmds.parent(interp_joint,skeleton_group)
		

    @classmethod
    def get_joint_type(cls):
        return cls.JOINTTYPE