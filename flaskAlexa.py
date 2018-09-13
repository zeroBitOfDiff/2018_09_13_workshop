# -*- coding: utf-8 -*-
"""
Created on Sun May 27 14:37:51 2018

@author: CO2
"""

from flask import Flask
from flask_ask import Ask, statement
import json
import requests

app = Flask(__name__)
ask = Ask(app, '/')

# python logic.. basically gets from api
def get_price():
    #over all spot prices
    prices_list =[]
    
    #bitcoin
    r1 = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
    p1=r1.json()
    prices_list.append("Bitcoin... " + p1['data']['amount'])
    
    #ethereum
    r2 = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot")
    p2=r2.json()
    prices_list.append("Ethereum... " + p2['data']['amount'])

    #bitcoin cash
    r3 = requests.get("https://api.coinbase.com/v2/prices/BCH-USD/spot") 
    p3=r3.json()
    prices_list.append("Bitcoin Cash... " + p3['data']['amount'])

    #light coin
    r4 = requests.get("https://api.coinbase.com/v2/prices/LTC-USD/spot")
    p4=r4.json()
    prices_list.append("Litecoin... " + p4['data']['amount'])

    prices_list = '...'.join([i for i in prices_list])
    return prices_list

# =============================================================================
# Debug statement
# prices = get_price()
# print(prices)
# =============================================================================

@app.route('/')
def homepage():
    return "howdy!"

@ask.launch
def start_skill():
    welcome_message = 'Hello there, would you like to the spot price of Bitcoin, Ethereum, Litecoin, or Bitcoin Cash' 

@ask.intent('YesIntent')
def share_price():
    spot_price = get_price()
    price_msg = 'The current spot prices are {}'.format(spot_price)
    return statement(price_msg)

@ask.intent('NoIntent')
def no_intent():
    bye_text = 'Goodbye Felisha, no crypto price for you!'
    return statement(bye_text)

if __name__ == '__main__':
    app.run()