# -*- coding:utf-8 -*-

import arcpy
# need to remove lock manually
connection ='Database Connections/sdejrq@sde.sde'
arcpy.env.workspace = connection
names=['RES_'+str(x) for x in range(11,24)]
for ds in names:
    print ds
    fc = arcpy.ListFeatureClasses(None,None,ds)
    print fc
    for f in fc:
        des = arcpy.Describe(f)
        if str(des.hasSpatialIndex) == 'True':
            print 'delete spatial index:',str(f)
            arcpy.RemoveSpatialIndex_management(f)
        print 'add spatial index:',str(f)
        arcpy.AddSpatialIndex_management(f)
        print str(f),'ok'

