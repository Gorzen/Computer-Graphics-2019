import bpy

class TrackGenerator():
    points = [(1, 1, 1), (2, 2, 1), (10, 10, 1)]
    curveData = bpy.data.curve.new('trackCurve', type='CURVE')
    curveData.dimensions = '3D'
    curveData.resolution_u = 3
    
    curveObject = None
    
    def drawCurve():
        bezierCurve = curveData.splines.new('BEZIER')
        bezierCurve.points.add(len(coords))
        for i, coord in enumerate(points):
            x,y,z = coord
            polyline.points[i].co = (x, y, z, 1)
        
        curveObject = bpy.data.objects.new('RollerCoasterCurve', curveData)
        scn = bpy.context.scene
        scn.objects.link(curveObject)