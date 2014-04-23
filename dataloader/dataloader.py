import yahooDataRetriever
import csv
import datetime

from models import Historical_Data, Company

name_file = "./dataloader/SandP500CompanyNames.txt"

def input_companies():
  ''' Creates the company models for each S&P 500 company'''
  
  yahoo_data = yahooDataRetriever.get_dict_500_companies(name_file)
  
  for i in yahoo_data.keys():
    c = Company()
    c.name = yahoo_data.get(i)
    c.ticker = i
    c.save()
  
  

def input_company_hist():
  ''' Returns a dictionary of S&P 500 company historical data'''
  
  # Gets all of the historical data
  #yahooDataRetriever.get_S_and_P_500_data()
  
  yahoo_data = yahooDataRetriever.get_dict_500_companies(name_file)
  
  print "Company Ticker and Names:"
  print yahoo_data
  
  for e in Company.objects.all():
      print(e.name)  
  
  # Loops over every csv file in the Data folder
  for i in yahoo_data.keys():
    cr = csv.reader(open( "./dataloader/Data/" + i + ".csv", "rb"))
    
    # Starting from second row
    cr.next()
    for row in cr:

      # Date,Open,High,Low,Close,Volume,Adj Close

      h = Historical_Data()
      date = row[0].split('-')
      companies = Company.objects.filter(name = i)
      h.company = companies[0]
      h.date = date[0]+date[1]+date[2]
      h.opening = row[1]
      h.high = float(row[2])
      h.low = float(row[3])
      h.closing = float(row[4])
      h.volume = float(row[5])
      h.adj_close = float(row[6])
      h.save(force_insert=True)
      print "saved data for: "+ i

