
"""
Created on Sat May 26 03:17:22 2018

@author: CO2
"""

import requests

#over all spot prices

#bitcoin
r1 = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")

p1=r1.json()
print(p1 )
prices_list =[]
prices_list.append("Bitcoin... " + p1['data']['amount'])
print("Bitcoin... " + p1['data']['amount'])
#prices_dic = dict([(p1['data']['base'], p1['data']['amount'])])



#ethereum
r2 = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot")

p2=r2.json()
#print("ETH_USD " + p2['data']['amount'])
#prices_dic.update(dict({p2['data']['base'] : p2['data']['amount']}) )
prices_list.append("\nEthereum... " + p2['data']['amount'])

#print(prices_dic)
#bitcoin cash
r3 = requests.get("https://api.coinbase.com/v2/prices/BCH-USD/spot")
 
p3=r3.json()
#print("BCH_USD " + p3['data']['amount'])
#prices_dic.update(dict({p3['data']['base'] : p3['data']['amount']}) )
prices_list.append("\nBitcoin Cash... " + p3['data']['amount'])

#light coin
r4 = requests.get("https://api.coinbase.com/v2/prices/LTC-USD/spot")

p4=r4.json()
#print("LTC_USD " + p4['data']['amount'])
#prices_dic.update(dict({p4['data']['base'] : p4['data']['amount']}) )
prices_list.append("\nLitecoin... " + p4['data']['amount'])


prices_list = '...'.join([i for i in prices_list])
#print(prices_dic)
print(prices_list)
# =============================================================================
# r5 = requests.get("https://api.coindesk.com/v1/bpi/currentprice/CNY.json")
# 
# print(r5.status_code)
# =============================================================================
