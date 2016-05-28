# -*- coding:utf-8 -*-
#将sde中的要素类复制到file gdb
import arcpy

connection = 'Database Connections\sdejrq@sdejrq.sde'
arcpy.env.workspace = connection
gdb = 'C:\\arcpy\\test2.gdb\\Test'
fc = arcpy.ListFeatureClasses(None,None,'RES_10')
for f in fc:
    print f
    arcpy.FeatureClassToGeodatabase_conversion(f,gdb)

print 'ok'
