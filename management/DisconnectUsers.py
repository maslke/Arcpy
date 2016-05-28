# -*- coding:utf-8 -*-

# disconnect users release the lock

import arcpy

#创建的sde连接文件
connection = 'Database Connections/sdejrq@sdejrq.sde'

users = arcpy.ListUsers(connection)
print len(users)
arcpy.AcceptConnections(connection,False)
arcpy.DisconnectUser(connection,'All')

users = arcpy.ListUsers(connection)
print len(users) #should be 1