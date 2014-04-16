import models as MOD
import yahooDataRetriever
import csv

ticker_file = "./dataloader/SandP500TickerSymbols.txt"


def input_company_hist():
  ''' Returns a dictionary of S&P 500 company historical data'''
  
  # Gets all of the historical data
  #yahooDataRetriever.get_S_and_P_500_data()
  
  # Creates all of the historical data objects in the database
  yahoo_data = yahooDataRetriever.get_top_500_tickers(ticker_file)
  
  for i in yahoo_data:
    cr = csv.reader(open( "./dataloader/Data/" + i + ".csv", "rb"))
    
    count = 0
    for row in cr:
      if count == 0:
        continue
      h = MOD.Historical_Data()
      
      #h.date = datetime.date(
      h.opening = row[1]
      h.high = int(row[2])
      h.low = int(row[3])
      h.closing = int(row[4])
      h.volume = int(row[5])
      h.adj_close = int(row[6])
      h.save()
      print "saved data for: "+ h
      count = count + 1

