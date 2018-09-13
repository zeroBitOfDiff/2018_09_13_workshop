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

def get_creds():
    if 'scrappy' in config:
        # print("[scrappy] creds is in")
        creds = config['scrappy']
        # user = creds['user']
        # psd = creds['psd']

        return creds
    else:
        return 'nope'
    # debug statment
    # print(user) 
    # print(psd)

def get_all_school_urls():
    url = 'https://www.ucf.edu/'

    s = requests.Session()


    response = s.get(url)

    # print(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')

    #print(soup.prettify())

    a = soup.find_all('a')
    print('*'*100)
    # print(a)
    for item in a:
        try:
            
            print(item['href'])
        except:
            pass

def get_webcourses():
    url2 = 'https://webcourses.ucf.edu/'

    s2 = requests.session()

    # r2 = s2.get(url2)
    creds = get_creds()
    
    wcreds = {'j_username':creds['user'], 'j_password':creds['psd']}
    
    r2 = s2.post(url2, data=wcreds)

    soup2 = BeautifulSoup(r2.text, 'html.parser')
    
    

    print(soup2.prettify()) 
    

def main():
    print('do you want all the urls on ucf website y or n')
    d1=input()
    if d1 == 'y':
        get_all_school_urls()

    print('do you want to access webcourses y or n')
    d2=input()
    if d2 == 'y':
        get_webcourses()

    

if __name__ == "__main__":
    main()

