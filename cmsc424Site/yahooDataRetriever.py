import ystockquote

ticker_file = "./SandP500TickerSymbols.txt"


def get_top_500_tickers(f):
  ''' Generates a list of S&P 500 tickers and returns them '''
  # gets lines of file
  f = open("./SandP500TickerSymbols.txt")
  lines = f.readlines()
  f.close()
  
  j = []
  
  # Strips white space from each entry in list
  for i in lines:
    i = i.strip()
    j.append(i)
  
  return j



def get_historical_csv(company_ticker, from_date, to_date):
  ''' Gets historical csv file for a company in a certain time span. 
  date formated as mmddyyyy
  '''
  
  from_month = int(from_date[0:2])
  from_day = int(from_date[2:4])
  from_year = int(from_date[4:8])
  
  to_month = int(to_date[0:2])
  to_day = int(to_date[2:4])
  to_year = int(to_date[4:8])
  


  ## Stripping the leading 0's if their are any
  #if from_month[0] == "0":
    #from_month = from_month[1]
  
  #if from_day[0] == "0":
    #from_day = from_day[1]
    
  #if to_month[0] == "0":
    #to_month = to_month[1]
  
  #if to_day[0] == "0":
    #to_day = to_day[1]  
  
  # Decrementing the month to work with url
  from_month = from_month - 1
  to_month = to_month - 1
  
  print from_month
  print from_day
  print from_year
  print "hello"
  print to_date
  print to_month
  print to_year

  url = "http://ichart.yahoo.com/table.csv?s="
  
  
  
  
get_historical_csv("GOOG", "01012008", "12312013")