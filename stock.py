from pandas.io.pytables import AppendableFrameTable
import requests
import json
from collections import defaultdict
from alpha_vantage.timeseries import TimeSeries # The alpha_vantage can be used when working with alpha_vantage api. There is no need to use the request libary to make API calls in this case
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime, timedelta
import random
import time
'''This script will simulate a trading stock and shares by producing a trading bot that initially trades £2000 over 5 different stocks that are already decided. These stock/shares will be day traded using a day trading strategy '''

'''Stocks to be traded:

1) GDX -  global investment manager firm
2) AMD - Advanced Micro Devices Inc
3) TSLA - Tesla Inc
4) ROKU - Roku Inc. is an American company offering digital streaming services and hardware
5) AMC - The movie theater stock, favorite of Reddit traders since January

We limited to 5 API calls per minute so an API call for each stock each minute. This may affect returns due to price changes onlt being known every minute rather than continuesely(ie: every second)
'''

API_KEY = 'RVMUSLYVL9TZ0R55' # Private and unique API key used for authentication

initial = {
  'api_key':'RVMUSLYVL9TZ0R55',
  'money':2000
}
class StockHolder:
  '''Holds all five stocks'''
  def __init__(self,ticker1 = ' ',ticker2 = ' ',ticker3 = ' ',ticker4 = ' ',ticker5 = ' ',totalinvestment = 1000):
    self.totalinvestment = totalinvestment
    self.investmentEachStock = self.totalinvestment//5
    '''List containing all stocks'''
    self.listofStocks = [Stock(self.investmentEachStock,ticker1),Stock(self.investmentEachStock,ticker2),Stock(self.investmentEachStock,ticker3),Stock(self.investmentEachStock,ticker4),Stock(self.investmentEachStock,ticker5)]
    
  def run(self):
    '''Iterates though each list stock of stocks every minute becuae the API only allows for 5 api calls per minute '''
    while int(datetime.now().strftime('%H'))<20:
      time.sleep(60)
      for stock in self.listofStocks:
        stock.scan()
        time.sleep(5)
    
    '''At 8pm, the program should stop and returns should be summed'''
    total = 0
    for stock in self.listofStocks:
      total+=stock.final
    '''Return trading results'''
    print('Total after trading ended:',total)
    print('Profit/loss:',total-self.totalinvestment)
  
  def __repr__(self):
    return 'Stocks Owned:' + str(self.listofStocks)

class Stock:
  def __init__(self,investment,ticker = ' '):
    self.ticker = ticker # Stock ticker name
    self.investment = investment # initialisation of initial investment, should be £500 pound for each investment
    self.sharePrice = []
    ts = TimeSeries(API_KEY)
    self.data = ts.get_intraday(self.ticker,interval='1min',outputsize='full')
    self.date = []
    self.day = 1
    self.status = 'DO NOT OWN'
    self.buyPrice = 0
    self.sellPrice = 0
    self.final = 0
  def plot(self):
    date = datetime.now()
    date = date.strftime('%Y-%m-%d %H:%M:00')
    openPrice = self.data[0][date]['1. open'] # gets the open price of each stock when a GET request is requested each one minute
    openPrice = float(openPrice)
    print('Share Price',openPrice)
    date = datetime.strptime(date,'%Y-%m-%d %H-%M-%S') # string format of datetime parsed into datetime format/object
    self.date.append(date) # datetime date appended into date list
    def animate(i):
      randomColor = ['red','purple','green','orange']
      self.sharePrice.append(openPrice)
      plt.plot_date(self.date,openPrice,label = self.ticker + ' ' + 'Stock',color = random.choice(randomColor))

      plt.title(self.ticker)
      plt.xlabel('Date',fontdict={'fontweight':'bold','fontsize':8})
      plt.ylabel('Share Price',fontdict={'fontweight':'bold','fontsize':8})
      plt.tight_layout()
      plt.gcf().autofmt_xdate() # Formats date on x axis
      
    
    ani = FuncAnimation(plt.gcf(),animate,interval = 1000) # Animation object
    plt.show() # plots and shows animations
      
      
  
  def buy(self):
    '''Buys stock for 200 dollars at that right time'''
    if self.status == 'DO NOT OWN':
      buyPrice = initial['money']//5 # 200 dollars
      date = datetime.now()
      date = date.strftime('%Y-%m-%d %H:%M:00')
      try:
        self.buyPrice = self.data[0][date]['1. open']
        self.status = self.ticker + ' ' + '(owned)'
        print(self.status)
        
      except:
        print('Cannot buy')
      
    else:
      print('Already owned-bot can only sell now at the right time')
  
  def sell(self):
    '''Sells stock when the sitution right based on the strategy being used'''
    try:
      date = datetime.now()
      date = date.strftime('%Y-%m-%d %H:%M:00')
      self.sellPrice = self.data[0][date]['1. open']
      '''Now find percentage difference between sell price and buy price'''
      diff = ((float(self.sellPrice) - float(self.buyPrice))/float(self.buyPrice))
      moneyMadeorLost = self.investment*diff
      self.final = self.investment+moneyMadeorLost
      self.status = 'Sold'
  
    except:
      pass
  
  def scan(self):
    '''Scans the price of each stock every minute '''
    try:
      date = datetime.now()
      date = date.strftime('%Y-%m-%d %H:%M:00')
      print(self.ticker + ' current price:',self.date[0][date]['1. open'])
      diff = self.percentages(date) #Need to refactor 
      if diff<=0.01:
        self.buy()
        print(self.ticker + ' ' + 'bought')
        
      
      elif diff>=0.02 and self.status ==  self.ticker + ' ' + '(owned)':
        self.sell()
        print(self.ticker + ' ' + 'sold')
      else:
        print(self.ticker + ':Percentage difference-',self.percentages() )
    except:
      print(self.ticker + ':','Price not found')
  
  def percentages(self,date):
    '''Compares percentages off stock every minute with previous minute. This percentage is being used to figure out if stock should be sold or bought'''
    try:
      OpenNow = self.data[0][date]['1. open']
      DateBefore = datetime.strptime(date,'%Y-%m-%d %H:%M:%S') - timedelta(minutes=1)
      DateBefore = DateBefore.strftime('%Y-%m-%d %H:%M:00')
      OpenBefore = self.data[0][DateBefore]['1. open']
      # print('Open Before:',OpenBefore)
      diff = ((float(OpenNow) - float(OpenBefore))/float(OpenBefore))
      return diff
      
    except:
      print('Percentage difference cannot be found')
      
  def __repr__(self):
    return 'Stock:' + self.ticker



# s = Stock(200,'AAPL')
# print(s)
# # s.scan()



holder = StockHolder('GDX','AMD','TSLA','ROKU','AMC',2000)
holder.run()


  




    


    

