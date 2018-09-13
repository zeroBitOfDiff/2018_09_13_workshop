#s3helper.py
import boto3 as b3
import sys
import pandas as pd
import requests
import getpass
import configparser
import base64
import logging
import xml.etree.ElementTree as ET
import re
from bs4 import BeautifulSoup
from os.path import expanduser

awsconfigfile = '\.aws\credentials'
region='us-east-1'
outputformat = 'json'

home = expanduser("~")
filename = home + awsconfigfile
#  open excell aws keys

config = configparser.ConfigParser()
config.read(filename)
# print(filename)
if 'zero_0000' in config:
    print("[zero_0000] creds is in")
    creds = config['zero_0000']
    access_key = creds['access_key']
    secret_access_key = creds['secret_access_key']

client =b3.client(service_name = 's3', 
        use_ssl=True, 
        aws_access_key_id=access_key, 
        aws_secret_access_key=secret_access_key, 
        config=None)

response = client.list_buckets()

# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]
# Print out the bucket list
print("Bucket List: %s" % buckets)

bucket_name = buckets[1]

def upload_file_to_s3(file):

    try:

        client.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={

                "ContentType": file.content_type
            }
        )

    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e
    
    # return "{}{}".format('http://{}.s3.amazonaws.com/'.format(bucket_name),file.filename)
    return "sup"