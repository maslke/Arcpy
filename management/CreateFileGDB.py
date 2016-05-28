# -*- coding:utf-8 -*-

# for:create a file geodatabase

import arcpy


path = r'C:\\arcpy\\'
name = 'test2.gdb'
arcpy.CreateFileGDB_management(path,name)
sr = arcpy.SpatialReference(4326)
arcpy.CreateFeatureDataset_management(path+name,'TEST',sr)
arcpy.CreateFeatureclass_management(path+name+'\\Test','test','POLYGON')

print arcpy.Exists(path+name+'\\Test\\test')


