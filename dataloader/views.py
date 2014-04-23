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
  
  results = yahooDataRetriever.get_top_500_tickers(ticker_file)
  results.sort()
  
  return render_to_response("nav/home.html", {'results':results})

def investing(request):

  return render_to_response("nav/investing.html", {})


def queries(request):
  
  return render_to_response("nav/queries.html", {})


def misc(request):
  
  return render_to_response("nav/misc.html", {})


