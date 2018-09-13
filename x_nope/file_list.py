# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 02:25:01 2018

@author: CO2
"""

from os.path import expanduser, isfile, join
from os import walk, path, listdir

awsconfigfile = '\.aws\credentials'
region='us-east-1'
outputformat = 'json'

home = expanduser("~")
# filename = home + awsconfigfile
app_file = '\Projects\\flask3.0'
_path_ = home + app_file

print(_path_)
# =============================================================================
# 
# extension = os.path.splitext(filename)[1]
# =============================================================================
# =============================================================================
# 
#     def uploadDirectory(path,bucketname):
# app_base = path.split(_path_)[1]

onlyfiles = listdir(_path_) 

print('*'*50)
print(onlyfiles)
print('*'*50)

for root,dirs,files in walk(_path_):

    for file in files:
        
        if path.splitext(file)[1] != '.pyc':
            print(root.split("\\")[4:])
            # print(app_base +'/'+path.split(root)[1] +'/'+ file)
            # print(file)
# =============================================================================
#             
# import boto3
# 
# client = boto3.client('s3')
# 
# response = client.put_object(
#         Bucket='my-top-level-bucket',
#         Body='',
#         Key='test-folder/'
#         )
# =============================================================================
            # print(path.join(root, file))
#        s3C.upload_file(os.path.join(root,file),bucketname,file)
# =============================================================================
# =============================================================================
# 
# import os
# for root, dirs, files in os.walk(".", topdown=False):
#    for name in files:
#       print(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))
# =============================================================================
