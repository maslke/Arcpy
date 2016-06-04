# -*- coding:utf-8 -*-

import arcpy
import xml.dom.minidom as DOM

path = 'E:\\grid_map.mxd'
connection = 'GIS Servers/..'

mxd = arcpy.mapping.MapDocument(path)
lyrs = arcpy.mapping.ListLayers(mxd)

brkLyrs = arcpy.mapping.ListBrokenDataSources(mxd)


analysis = arcpy.mapping.CreateMapSDDraft(mxd,'E:\\grid_map.sddraft','grid_map','ARCGIS_SERVER',connection,False,'folder',None,None)

#analysis mxd document
for key in ('errors','warnings','messages'):
    vals = analysis[key]
    print '---------------------'
    print key
    for ((message,code),layers) in vals.iteritems():
        print message,code
        for layer in layers:
            print layer.name

# disable kmlserver
xml = DOM.parse('E:\\grid_map.sddraft')
types = xml.getElementsByTagName('TypeName')
for type in types:
    if type.firstChild.data == 'KmlServer':
        parent = type.parentNode
        for node in parent.childNodes:
            if node.tagName == 'Enabled':
                node.firstChild.data = 'false'
#save a copy
f = open('E:\\grid_map_1.sddraft','w')
f.write(xml)
f.close()

#reanalysis after modify sddraft
analysis = arcpy.mapping.AnalyzeForSD('E:\\grid_map.sddraft')

arcpy.StageService_server('E:\\grid_map.sddraft','E:\\grid_map.sd')
arcpy.UploadServiceDefinition_server('E:\\grid_map.sd',connection)

