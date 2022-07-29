#imports
import yfinance as yf
import pandas as pd
import csv

################################################################################
#                           Program Goals                                      #
################################################################################
################################################################################
#                                                                              #
#   import stock information                                                   #
#   create database for information                                            #
#   insert information into database                                           #
#   call information from database and display in console                      #
#   display information in GUI                                                 #
#   create controls for user to select data                                    #
#                                                                              #
################################################################################

#initialize global variables for stock data collected.
gme = yf.Ticker("GME")
#amd = yf.Ticker("AMD")
#sony = yf.Ticker('Sony')

yf.pdr_override()


tickerData = pd.get_data_yahoo("GME AMD SONY TLRY", start="2022-04-01", end="2022-04-21", interval="15m", group_by='ticker')

dataTable = pd.DataFrame(tickerData)

with open('stockData.csv', 'w', newline='') as csvfile:
          
          stockWriter = csv.writer(csvfile, delimiter=' ')
          stockWriter.writerow([dataTable])

print(tickerData)