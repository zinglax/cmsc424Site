# Views for Dataloader appication
from django.http import HttpResponse
from django.shortcuts import render_to_response
import dataloader as d
import yahooDataRetriever

from models import *

ticker_file = "./dataloader/SandP500TickerSymbols.txt"


def dataloader(request):
  name = 'Dylan'
  html = '<html><body background="http://colourlovers.com.s3.amazonaws.com/images/patterns/1202/1202172.png">Historical Data and companies are now objectified in a sqlite3 database</body></html>' 

  d.input_companies()  
  d.input_company_hist()

    
  return HttpResponse(html)    

def home(request):
  
  input_company_hist()
  
  
  results = yahooDataRetriever.get_top_500_tickers(ticker_file)
  results.sort()
  
   
  
  return render_to_response("nav/home.html", {'results':results})

def investing(request):

  return render_to_response("nav/investing.html", {})


def queries(request):
  
  return render_to_response("nav/queries.html", {})


def misc(request):
  
  return render_to_response("nav/misc.html", {})




def input_company_hist():
  ''' Returns a dictionary of S&P 500 company historical data'''
  
  # Gets all of the historical data
  #yahooDataRetriever.get_S_and_P_500_data()
  
  # Creates all of the historical data objects in the database
  yahoo_data = yahooDataRetriever.get_top_500_tickers(ticker_file)
  
  # Loops over every csv file in the Data folder
  for i in yahoo_data:
    cr = csv.reader(open( "./dataloader/Data/" + i + ".csv", "rb"))
    
    count = 0
    for row in cr:
      # skips description line of text at top
      ## Date,Open,High,Low,Close,Volume,Adj Close
      if count == 0:
        continue
      h = Historical_Data()
      
      
      #h.date = datetime.date(
      h.opening = row[1]
      h.high = int(row[2])
      h.low = int(row[3])
      h.closing = int(row[4])
      h.volume = int(row[5])
      h.adj_close = int(row[6])
      h.save(force_insert=True)
      #print "saved data for: "+ h
      
      count = count + 1