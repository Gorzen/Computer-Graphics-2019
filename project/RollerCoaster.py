import os
import bpy
from bpy.types import Panel
import numpy as np
import math

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
        straight = Symbol(" straight ")
        right = Symbol(" right ")
        f = Symbol("F")
        looping = Symbol(" looping ")
        
        p = Symbol("+")
        m = Symbol("-")
        u = Symbol(" UP ")
        d = Symbol(" DOWN ")

        rules = Rules({right : [straight, p, straight],
                        looping : [straight, u, straight, u, straight, u, straight, u, m, m, m, m, straight, d, straight, d, straight, d, straight, d, straight, d, straight, d, straight, d, straight, d, p, p, p, p, straight, u, straight, u, straight, u, straight, u, straight],
                        f : [f, p, m, u, f]})

        lsystem = LSystem(rules, math.pi / 4, math.pi / 8, 1, (0.0, 0.0, 0.0))

        symbols = lsystem.expand([looping], 10)

        pos = lsystem.compute_symbols(symbols)

        points = pos
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
    

## L-Systems files
## Import didn't work

class Symbol:
    def __init__(self, str):
        self.str = str

    def __str__(self):
        return self.str

class Rules:
    def __init__(self, rules):
        self.rules = rules

    def add(self, symbol, expansion):
        self.rules.update({symbol : expansion})

    def expandSymbol(self, symbol):
        return self.rules.get(symbol, [symbol])

    def length(self):
        return len(self.rules)


slope_angle_limit = math.pi / 2

min_phi = math.pi / 2 - slope_angle_limit
max_phi = math.pi / 2 + slope_angle_limit

class LSystem():
    def __init__(self, rules, theta_step, phi_step, length, p0):
        assert phi_step >= 0 and theta_step >= 0
        self.rules = rules
        self.theta_step = theta_step
        self.phi_step = phi_step
        self.length = length
        self.p0 = p0

    def expandOnce(self, symbols):
        s = []
        for symbol in symbols:
            s += self.rules.expandSymbol(symbol)
        return s

    def expand(self, symbols, num_iters):
        s = symbols.copy()
        for i in range(num_iters):
            s = self.expandOnce(s)

        return s

    def compute_symbols(self, symbols):
        theta = 0.0
        phi = math.pi / 2
        p = self.p0

        list_pos = [p]

        for s in symbols:
            if s.str == "+":
                theta += self.theta_step
            elif s.str == "-":
                theta -= self.theta_step
            elif s.str == " UP ":
                phi -= self.phi_step
                if phi < min_phi:
                    phi = min_phi
            elif s.str == " DOWN ":
                phi += self.phi_step
                if phi > max_phi:
                    phi = max_phi
            else:
                p = (self.length * math.cos(theta) * math.sin(phi) + p[0], self.length * math.sin(theta) * math.sin(phi) + p[1], self.length * math.cos(phi) + p[2])
                list_pos.append(p)

        return list_pos

    
#Needed to run the script inside Blender Text Editor
if __name__ == '__main__':
    register()
