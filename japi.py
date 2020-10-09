# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:27:09 2020

@author: Matt-Predator
"""

import urllib.request
import json

def getStockData(symbol):
    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + symbol +"&apikey=633FNJ17M123OGDF" 
    connection = urllib.request.urlopen(url)
    responseString = connection.read().decode()

    return responseString


keep_going = True

while(keep_going):
    print("Enter a Stock Symbol or quit to exit")
    symbol = input()
    if symbol == 'quit':
        keep_going = False
    else:
        raw_data = getStockData(symbol)
    
        print(raw_data)
        data_dict = json.loads(raw_data)  
        #print(data_dict)
        price = data_dict['Global Quote']['05. price']
        print ("The current price of " + symbol + " is: " + price)
    
    
print("Stock Quotes retrieved successfully!")