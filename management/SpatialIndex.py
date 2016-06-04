# -*- coding:utf-8 -*-

import arcpy

connection ='Database Connections/sdejrq@sde.sde'
arcpy.env.workspace = connection
arcpy.AddSpatialIndex_management('RES_10/MAP_JRQ_GRID_10')

