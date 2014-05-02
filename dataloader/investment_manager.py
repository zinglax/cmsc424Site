# Managing investments
from models import Historical_Data, Company, Port_Indi, StakeHold, Activity




def fund(row):
  ''' A funding of a new individual '''
  port_indi = Port_Indi()
  act = Activity()
  
  # Creating the new portfolio/individual    
  port_indi.cash = row[2]
  port_indi.networth = row[2]
  port_indi.name = row[1]
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
  
  print port_indi
  #psrint act.amount
  #print act.act_type
  #print act.port_indi1
  
  
  
def buy(row):
  ''' buying into a portfolio or company '''
  
  
  
def sell(row):
  ''' selling investment in a portfolio or company '''
  
  
  
def sellbuy(row):
  ''' selling of an investment in one company or portfolio and investing in another '''
  
  
  