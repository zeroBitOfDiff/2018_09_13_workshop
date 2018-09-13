# -*- coding: utf-8 -*-
"""
Created on Tue May 22 20:41:32 2018

@author: CO2

aws endpoint = apigateway.us-east-1.amazonaws.com


"""
import boto3 as b3
import pandas as pd

df_creds = pd.read_csv("credentials.csv")



print("aws_access_key_id= " + df_creds.at[0,"Access key ID"])

print("aws_secret_access_key= " + df_creds.at[0,"Secret access key"])



s3 = b3.resource(
        's3',
        aws_access_key_id=df_creds.at[0,"Access key ID"],
        aws_secret_access_key=df_creds.at[0,"Secret access key"])

for bucket in s3.buckets.all():
    print(bucket.name)
    
# Upload a new file
data = open('8b6.jpg', 'rb')
s3.Bucket(bucket.name).put_object(Key='8b6.jpg', Body=data)

my_bucket = s3.Bucket(bucket.name)

#mybucket.objects.filter(Prefix='foo/bar')
for object in my_bucket.objects.all():
    print(object)







