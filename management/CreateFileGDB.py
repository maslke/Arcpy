# -*- coding:utf-8 -*-

# for:create a file geodatabase

import arcpy


path = r'C:\\arcpy\\'
name = 'test2.gdb'
#create file gdb
arcpy.CreateFileGDB_management(path,name)

#spatialReference
sr = arcpy.SpatialReference(4326)

#create dataset
arcpy.CreateFeatureDataset_management(path+name,'TEST',sr)

#create featureclass
arcpy.CreateFeatureclass_management(path+name+'\\Test','test','POLYGON')

fc = path+name+'\\Test\\test'

#delete features
arcpy.DeleteFeatures_management(fc)

#delete features with cursor:
with arcpy.da.UpdateCursor(fc,['NAME']) as cursor:
    for row in cursor:
        cursor.deleteRow()

#get polygon extent
with arcpy.da.SearchCursor(fc,['NAME','SHAPE@']) as cursor:
    for row in cursor:
        print row[0],row[1].extent.XMin,row[1].extent.XMax,row[1].extent.YMin,row[1].extent.YMax

#remove field
arcpy.DeleteField_management(fc,'NAME')

#add field
arcpy.AddField_management(fc,'NAME','Text',None,None,50)

#calculate field
arcpy.CalculateField_management(fc,'NAME','[_NAME]')

#list fields
fields = arcpy.ListFields(fc,None,None)
for fld in fields:
    print fld.name,fld.type,fld.length









