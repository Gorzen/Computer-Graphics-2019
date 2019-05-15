import os
import bpy
from bpy.types import (Panel,
                        PropertyGroup,
                        )
from bpy.props import (PointerProperty,
                        BoolProperty,
                        IntProperty,
                        )
import numpy as np
import math
import os
import sys
import importlib

dir = os.path.dirname(bpy.data.filepath)
if not(dir in sys.path):
    sys.path.append(dir)

import LSystem as LS

from LSystem.LSystems import *
from LSystem.Symbol import *
from LSystem.RollerCoasterLSystem import *

importlib.reload(LS.LSystems)
importlib.reload(LS.Symbol)
importlib.reload(LS.RollerCoasterLSystem)

class RollerCoasterSettings(PropertyGroup):
    loopings = BoolProperty(
        name = 'looping',
        description = 'Enable loopings to appear in the roller coaster',
        default = True,
    )

    iterations = IntProperty(
        name = 'iterations',
        description = 'Number of iterations that the L-System will perform',
        default = 0,
        min = 0,
        max = 10,
    )

class RollerCoasterPanel(Panel):
    #Addon informations
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_label = 'Procedural RollerCoaster'
    bl_context = 'objectmode'
    bl_category = 'RollerCoaster'

    #UI elements
    def draw(self, context):
        layout = self.layout
        settings = context.scene.roller_coaster_settings

        row = layout.row()
        row.label(text='Roller Coaster features')

        row = layout.row()
        row.prop(settings, "loopings", text = 'loopings')
        row = layout.row()
        row.prop(settings, 'iterations', text = 'Number of iterations')

        row = layout.row()
        self.layout.operator('roller_coaster.draw_tracks', text='Go!')

        row = layout.row()
        self.layout.operator('roller_coaster.delete_roller_coaster', text='Delete the Roller Coaster')

class track_generator_operator(bpy.types.Operator):
    bl_idname = 'roller_coaster.draw_tracks'
    bl_label = 'Draw roller coaster tracks'
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

    #Get settings
        settings = context.scene.roller_coaster_settings
        iterations = settings.iterations
        print(iterations)

        points = get_points(iterations = iterations)

        curveName = 'RollerCoasterCurve'
        tracksName = 'tracks'

    #First delete the existing roller coaster if it exists
        bpy.ops.roller_coaster.delete_roller_coaster()

    #Draw the curve
        curveData = bpy.data.curves.new('trackCurve', type='CURVE')
        curveData.dimensions = '3D'
        curveData.resolution_u = 4

        curve = curveData.splines.new('NURBS')
        curve.use_endpoint_u = True
        curve.points.add(len(points)-1)
        for i, coord in enumerate(points):
            x,y,z = coord
            curve.points[i].co = (x, y, z, 1)

        curveObject = bpy.data.objects.new(curveName, curveData)
        scn = bpy.context.scene
        scn.objects.link(curveObject)
        scn.objects.active = curveObject
        curveObject.select = True
        bpy.context.object.data.splines[0].order_u = 3
        bpy.context.object.data.splines[0].use_cyclic_u = True
        bpy.context.object.data.twist_mode = 'Z_UP'
        bpy.context.object.data.use_deform_bounds = True

    #Draw the tracks
        #import the tracks and set it active
        bpy.ops.object.select_all(action='DESELECT')
        path = os.path.join(dir, 'tracks.obj')
        tracks = bpy.ops.import_scene.obj(filepath = path)
        bpy.context.scene.objects.active = bpy.context.selected_objects[0]
        bpy.context.object.name = tracksName
        #Add array modifier to the tracks
        bpy.ops.object.modifier_add(type='ARRAY')
        bpy.context.object.modifiers["Array"].fit_type = 'FIT_CURVE'
        bpy.context.object.modifiers["Array"].curve = bpy.data.objects[curveName]
        bpy.ops.object.modifier_add(type='CURVE')
        bpy.context.object.modifiers["Curve"].object = bpy.data.objects[curveName]
        #Indicate the script terminated successfully
        return {"FINISHED"}

class delete_operator(bpy.types.Operator):
    bl_idname = 'roller_coaster.delete_roller_coaster'
    bl_label = 'Delete every objects related to the roller coaster'
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        curveName = 'RollerCoasterCurve'
        tracksName = 'tracks'

        bpy.ops.object.select_all(action='DESELECT')
        #Delete the curve
        if bpy.data.objects.get(curveName) is not None:
            bpy.data.objects[curveName].select = True    # Blender 2.7x
            bpy.ops.object.delete()
        #Delete the tracks
        if bpy.data.objects.get(tracksName) is not None:
            bpy.data.objects[tracksName].select = True    # Blender 2.7x
            bpy.ops.object.delete()
        return {"FINISHED"}

#Script registration
def register():
    bpy.utils.register_class(RollerCoasterPanel)
    bpy.utils.register_class(track_generator_operator)
    bpy.utils.register_class(delete_operator)
    bpy.utils.register_class(RollerCoasterSettings)
    bpy.types.Scene.roller_coaster_settings = PointerProperty(type=RollerCoasterSettings)

def unregister():
    bpy.utils.unregister_class(RollerCoasterPanel)
    bpy.utils.unregister_class(track_generator_operator)
    bpy.utils.unregister_class(delete_operator)
    del bpy.types.Scene.roller_coaster_settings


#Needed to run the script inside Blender Text Editor
if __name__ == '__main__':
    register()
