# -*- coding:utf-8 -*-
#replace datasource and save a copy
import arcpy

names = ['grid_map_'+str(x) for x in range(11,24) if x <> 14]
mxdPath = 'E:\\Media\\arcpy\\res_map_14.mxd'
for name in names:
    mxd = arcpy.mapping.MapDocument(mxdPath)
    lyrs = arcpy.mapping.ListLayers(mxd)
    for lyr in lyrs:
        connection = lyr.dataSource
        connection = connection.replace('14',str(name))
        contents = connection.split('\\')
        lyr.replaceDataSource(contents[0]+'\\'+contents[1],'SDE_WORKSPACE',contents[-1],True)
    mxd.saveACopy('E:\\Media\\arcpy\\grid_map_'+str(name)+'.mxd')
    del mxd
