# Managing investments
from models import Historical_Data, Company, Port_Indi, StakeHold, Activity
from models import *



def fund(row):
  ''' A funding of a new individual Takes in a list of a row in CSV.'''
  port_indi = Port_Indi()
  act = Activity()
  
  
  
  # Creating the new portfolio/individual    
  port_indi.cash = row[2]
  port_indi.networth = row[2]
  port_indi.name = row[1]
  
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
  
  # Referencing 
  port_indi.last_activity = act
  port_indi.save()
  
  print str(port_indi) + ' HAS BEEN FUNDED'
  #psrint act.amount
  #print act.act_type
  #print act.port_indi1
  

  
def buy(row):
  ''' buying into a portfolio or company. Takes in a list of a row in CSV. '''
  
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
  
  ports =  list(Port_Indi.objects.filter(name=row[2]))
  
  # check whether buying company or portfolio
  if ports != []:
    act.port_indi2 = Port_Indi.objects.get(name=row[2])
    stake.fund2 = Port_Indi.objects.get(name=row[2])
    
  else: # buying company
    act.company = Company.objects.get(ticker=row[2])
    stake.company = Company.objects.get(ticker=row[2])

    stakes = list(StakeHold.objects.filter(fund=buying_port,company=stake.company))
    
    print len(stakes)
    
    cash = act.port_indi1.cash
    
    
    # check if stakehold exists already
    if stakes ==[]:
      stake.amount = row[3]
    else:
      stakes = StakeHold.objects.get(fund=buying_port,company=stake.company)
      stake.amount = stake.amount + act.amount
    
    
    
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
  
  
  