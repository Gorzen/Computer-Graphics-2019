import bpy
from bpy.types import Panel

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
        row.label(text='Generate a Suzanne!')
        
        row = layout.row()
        row.operator('mesh.primitive_monkey_add', text='Add dummy')
        
#Script registration
def register():
    bpy.utils.register_class(RollerCoasterPanel)
    
def unregister():
    bpy.utils.unregister_clas(RollerCoasterPanel)
    
#Needed to run the script inside Blender Text Editor
if __name__ == '__main__':
    register()