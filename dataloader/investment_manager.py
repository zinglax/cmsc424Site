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
  
  print port_indi
  #psrint act.amount
  #print act.act_type
  #print act.port_indi1
  
  
  
def buy(row):
  ''' buying into a portfolio or company '''
  
  # Activity
  act = Activity()
  act.amount = row[3]
  act.act_type = "buy"
  act.port_indi1 = Port_Indi.objects.get(name=row[1])
  act.date = row[4].replace('-', '')
  
  ports =  list(Port_Indi.objects.filter(name=row[2]))
  
  if ports != []:
    act.port_indi2 = Port_Indi.objects.get(name=row[2])
  else:
    act.company = Company.objects.get(ticker=row[2])
  act.save()
  
  # Stakehold
  stakehold = StakeHold()
  stakehold.last_modified = row[4].replace('-', '')
  stakehold.fund = Port_Indi.objects.get(name=row[1])
  
  if ports != []:
    stakehold.fund2 = Port_Indi.objects.get(name=row[2])
  else:
    stakehold.company = Company.objects.get(ticker=row[2])
  
  
  
  
def sell(row):
  ''' selling investment in a portfolio or company '''
  
  
  
def sellbuy(row):
  ''' selling of an investment in one company or portfolio and investing in another '''
  
  
  