import os
import bpy
from bpy.types import Panel
import numpy as np
import math
import os
import sys

dir = os.path.dirname(bpy.data.filepath)
if not(dir in sys.path):
    sys.path.append(dir)
    
from LSystem.LSystems import LSystem
from LSystem.Symbol import Symbol
from LSystem.Symbol import Rules
from LSystem.RollerCoasterLSystem import get_points

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
        
        row = layout.row()
        row.label(text='Generate a procedural Roller Coaster!')
        
        row = layout.row()
        self.layout.operator('roller_coaster.draw_tracks', text='DRAW THIS ROLLERCOASTER!')
        
        row = layout.row()
        self.layout.operator('roller_coaster.delete_roller_coaster', text='Delete the Roller Coaster')

class track_generator_operator(bpy.types.Operator):
    bl_idname = 'roller_coaster.draw_tracks'
    bl_label = 'Draw roller coaster tracks'
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        points = get_points()
        
        curveName = 'RollerCoasterCurve'
        tracksName = 'tracks'
        
#        circles_distance = 1
#        circles_radius = 0.2
#        circles_name = 'track_circles'
#DEPRECATED: Use another way to draw now        
#    #Draw the circles
#        #add circle and rename it
#        bpy.ops.curve.primitive_bezier_circle_add(radius=circles_radius, enter_editmode=True, location=(0, 0, 0))
#        bpy.context.object.name = circles_name
#        #translate it
#        bpy.ops.transform.translate(value=(circles_distance, 0, 0))
#        #duplicate it
#        bpy.ops.curve.duplicate_move(CURVE_OT_duplicate={}, TRANSFORM_OT_translate={"value":(-circles_distance*2, 0, 0), "constraint_axis":(True, #False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', #"proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), #"gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
#        
#        #End: quit editmode
#        bpy.ops.object.editmode_toggle()
        
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
#        bpy.context.object.data.bevel_object = bpy.data.objects[circles_name]

    #Draw the tracks
        #import the tracks and set it active
        bpy.ops.object.select_all(action='DESELECT')
        path = os.path.join(os.getcwd(), 'tracks.obj')
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
        bpy.data.objects[curveName].select = True    # Blender 2.7x
        bpy.ops.object.delete()
        #Delete the tracks
        bpy.data.objects[tracksName].select = True    # Blender 2.7x
        bpy.ops.object.delete()
        return {"FINISHED"}
        
#Script registration
def register():
    bpy.utils.register_class(RollerCoasterPanel)
    bpy.utils.register_class(track_generator_operator)
    bpy.utils.register_class(delete_operator)
    
def unregister():
    bpy.utils.unregister_class(RollerCoasterPanel)
    bpy.utils.unregister_class(track_generator_operator)
    bpy.utils.unregister_class(delete_operator)

    
#Needed to run the script inside Blender Text Editor
if __name__ == '__main__':
    register()
