# -*- coding:utf-8 -*-
# for:calculate the length of two points,in 4326 spatialreference
import arcpy

x1,y1 = raw_input('input first point(format:x1,y1):').split(',')
x2,y2 = raw_input('input second point(format:x2,y2):').split(',')
x1,y1 = float(x1),float(y1)
x2,y2 = float(x2),float(y2)
pnt1 = arcpy.Point(x1,y1)
pnt2 = arcpy.Point(x2,y2)
line = arcpy.Polyline(arcpy.Array([pnt1,pnt2]),arcpy.SpatialReference(4326))
print line.getLength()
