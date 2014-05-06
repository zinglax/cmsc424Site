# Managing investments
from models import Historical_Data, Company, Port_Indi, StakeHold, Activity
from models import *
import yahooDataRetriever

ticker_file = "./dataloader/SandP500TickerSymbols.txt"


def fund(row):
  ''' A funding of a new individual Takes in a list of a row in CSV.'''
  port_indi = Port_Indi()
  act = Activity()
  
  # Creating the new portfolio/individual    
  port_indi.cash = row[2]
  port_indi.networth = row[2]
  port_indi.name = row[1]
  
  # Check to see if its an Individual or a Porfolio
  if row[0] == 'fund':
    port_indi.is_individual = False
  else:
    port_indi.is_individual = True
  #port_indi.last_quote = Quote()
  port_indi.last_activity = act
  port_indi.save()
  
  # Activity
  act = Activity()
  act.amount = row[2]
  act.act_type = "fund"
  act.port_indi1 = port_indi
  act.date = row[3].replace('-', '')
  act.save()
  
  # Referencing activity
  port_indi.last_activity = act
  port_indi.save()
  print str(port_indi) + ' HAS BEEN FUNDED'
   
def buy(row):
  ''' buying into a portfolio or company. Takes in a list of a row in CSV. 
  buy,fund_1,MMM,233780,2005-01-20
  buy,ind_2,fund_2,6671,2005-01-18
  '''
  buying_port = Port_Indi.objects.get(name=row[1])
  
  # Activity
  act = Activity()
  act.amount = row[3]
  act.act_type = "buy"
  act.port_indi1 = buying_port
  act.date = row[4].replace('-', '')
  
  # Stakehold
  stake = StakeHold()
  stake.last_modified = row[4].replace('-', '')
  stake.fund = buying_port  
  tickers = yahooDataRetriever.get_top_500_tickers(ticker_file)

  # check whether buying company or portfolio  
  if row[2] not in tickers: # Buying Portfolio
    purchase_port = Port_Indi.objects.get(name=row[2])
    act.port_indi2 = purchase_port
    stake.fund2 = purchase_port

    # Check cash amount    
    #if cash >= float(act.amount):
      #purchase_port.c
    
    # Calculate Percentage
    
    # Update other investors percenages
    
    # Calculate networths
    
  else: # Buying Company
    act.company = Company.objects.get(ticker=row[2])
    stake.company = Company.objects.get(ticker=row[2])
    stakes = list(StakeHold.objects.filter(fund=buying_port,company=stake.company))
    print len(stakes)
    cash = act.port_indi1.cash
    
    print row[4].replace('-', '')
    print stake.company
    
    
    hist_data = list(Historical_Data.objects.filter(date=row[4].replace('-', ''), company=Company.objects.get(ticker=row[2])))
    hist_data_record = hist_data[0]
    
    # check if stakehold exists already
    if stakes == []:
      #stake.save()
      #stake.shares = float(row[3])
      stake.shares = float(row[3]) / hist_data_record.closing
    else:
      stake = StakeHold.objects.get(fund=buying_port,company=stake.company)
      #stake.shares = float(row[3])
      stake.shares += float(row[3]) / hist_data_record.closing
    
    # Checking funds
    if cash >= float(act.amount):
      stake.save()
      act.save()
      buying_port.cash = cash - int(act.amount)
      buying_port.save()
      print "## BUY TRANSACTION COMPLETED"
    else:
      print "### INSUFFICIENT FUNDS: TRANSACTION NOT COMPLETED"
  
def sell(row):
  ''' selling investment in a portfolio or company. Takes in a list of a row in CSV.'''
  
def sellbuy(row):
  ''' selling of an investment in one company or portfolio and investing in another. Takes in a list of a row in CSV. '''
  
def calculate_networth(port_indi):
  ''' calculates the networth of a specific company, must do it recusively'''
  