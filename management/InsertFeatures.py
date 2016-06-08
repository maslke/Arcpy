# -*- coding:utf-8 -*-

import arcpy

leftUp,rightDown = (122,23),(123,21)
t = 0.0001

pnt1 = arcpy.Point(leftUp[0]+t,leftUp[1]-t)
pnt2 = arcpy.Point(leftUp[0]+t,rightDown[1]+t)
pnt3 = arcpy.Point(rightDown[0]-t,rightDown[1]+t)
pnt4 = arcpy.Point(rightDown[0]-t,leftUp[1]-t)
points = [pnt1,pnt2,pnt3,pnt4]

line1 = arcpy.Polyline(arcpy.Array([pnt1,pnt2]))
line2 = arcpy.Polyline(arcpy.Array([pnt2,pnt3]))
line3 = arcpy.Polyline(arcpy.Array([pnt3,pnt4]))
line4 = arcpy.Polyline(arcpy.Array([pnt4,pnt1]))
polylines = [line1,line2,line3,line4]

polygon1 = arcpy.Polygon(arcpy.Array([pnt1,pnt2,pnt3,pnt4,pnt1]))


#datasetName = 'RES_10'
datasetName = None
#connection = 'Database Connections/sdejrq@sde.sde'
connection = r'C:\arcpy\res_10.gdb'
arcpy.env.workspace = connection
fc = arcpy.ListFeatureClasses(None,None,datasetName)
print 'total is '+str(len(fc))
for f in fc:
    print str(f)
    with arcpy.da.InsertCursor(f,['SHAPE@']) as cursor:
        des = arcpy.Describe(f)
        if des.shapeType == 'Polygon':
            cursor.insertRow([polygon1])
        elif des.shapeType == 'Point':
            for pnt in points:
                cursor.insertRow([pnt])
        elif des.shapeType == 'Polyline':
            for line in polylines:
                cursor.insertRow([line])
