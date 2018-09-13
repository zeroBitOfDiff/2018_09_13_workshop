# -*- coding: utf-8 -*-
"""
Created on Sat May 26 02:49:09 2018

@author: CO2
"""

import pycurl 

from io import BytesIO

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://api.coinbase.com/v2/prices/ETH-USD/spot')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue().decode('utf-8')
# Body is a string in some encoding.
# In Python 2, we can print it without knowing what the encoding is.
print(body)