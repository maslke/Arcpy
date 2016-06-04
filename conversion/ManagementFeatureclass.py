# -*- coding:utf-8 -*-
#将sde中的要素类复制到file gdb
import arcpy

connection = 'Database Connections\sdejrq@sdejrq.sde'
arcpy.env.workspace = connection
gdb = 'C:\\arcpy\\test2.gdb\\Test'
fc = arcpy.ListFeatureClasses(None,None,'RES_10')

#fc to geodatabase
for f in fc:
    arcpy.FeatureClassToGeodatabase_conversion(f,gdb)

#fc to fc
for f in fc:
    arcpy.FeatureClassToFeatureClass_conversion(f,gdb,str(f),'"MAPID"=1')

# fc to shp
for f in fc:
    arcpy.FeatureClassToShapefile_conversion(f,r'C:\\arcpy')



