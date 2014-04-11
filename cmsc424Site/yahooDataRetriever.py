import ystockquote
import requests

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


def historical_url_generator(company_ticker, from_date, to_date):
  ''' Creates a URL for the historical data of a given company, dates formatted
  as mmddyyyy
  '''
  
  # Parsing date strings
  from_month = int(from_date[0:2])
  from_day = int(from_date[2:4])
  from_year = int(from_date[4:8])
  
  to_month = int(to_date[0:2])
  to_day = int(to_date[2:4])
  to_year = int(to_date[4:8])
  
  # Decrementing the month to work with url
  from_month = from_month - 1
  to_month = to_month - 1

  # Formatting URL
  url = "http://ichart.yahoo.com/table.csv?s=" + company_ticker + "&a=" +\
    str(from_month) + "&b=" + str(from_day) + "&c=" + str(from_year) + "&d=" +\
    str(to_month) + "&e=" + str(to_day) +"&f=" + str(to_year)
  
  return url
  
  
def retrieve_csv_file(url, company_ticker, to_date, from_date):
  " Retrieves the csv file for a given company over a period of time "
  # Generates Filename
  filename = company_ticker + "~" + to_date + "~" + from_date
  
  r = requests.get(url, stream=True)
  
  # Writes data to file from requests stream
  with open("./Data/"+filename, 'wb') as fd:
      for chunk in r.iter_content(chunk_size=1024):
          fd.write(chunk)
  
def get_S_and_P_500_data():
  
  tickers = get_top_500_tickers(ticker_file)

  for t in tickers:
    url = historical_url_generator(t, "01012005", "12312013")
    retrieve_csv_file(url, t, "01012008", "12312013")
    
if __name__ == "__main__":
  get_S_and_P_500_data()