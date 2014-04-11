from django.db import models

# Database structures used to store financial data

class Company(models.Model):
  ''' A S&P500 Company '''
  name = models.CharField(max_length=200)
  ticker = models.CharField(max_length=4)
  
  def __unicode__(self):
    return self.name
  
  
class Quote(models.Model):
  ''' A share price of a company at a specific point in time '''
  # Date
  date = models.DateTimeField
  
  # Company
  company = models.ForeignKey(Company)
  
  # Listed Price
  price = models.IntegerField()
  
  # Historical data record
  hist = models.ForeignKey(Historical_Data)  
  
  def __unicode__(self):
    return self.name
  

class StakeHold():
  ''' Ownership of a Stock or another Fund '''
  
  # Date of last modified
  last_modified = models.DateTimeField()
  
  # Owner
  fund = models.ForeignKey(Port_Indi)
  
  ''' StakeHold in a Stock '''
  company = models.ForeignKey(Company)
  amount = models.IntegerField()
  last_quote = models.ForeignKey(Quote)
  
  ''' StakeHold in a Fund '''
  fund2 = models.ForeignKey(Port_Indi)  
  percentage = models.IntegerField()  
  

  def __unicode__(self):
    return self.name  
  
  
class Activity(models.Model):
  ''' A buy, sell, or funding '''
  
  # Buy, sell, or fund
  act_type = models.CharField(max_length=50)
  
  # Cash value
  # used for a funding or buying of a specific portfolio or stock
  amount = models.IntegerField()
  
  # Maker of transaction
  fund = models.ForeignKey(Port_Indi)
  
  # Secondary fund or stock to purchaise/sell
  fund2 = models.ForeignKey(Port_Indi)
  company = models.ForeignKey(Company)
  
  def __unicode__(self):
    return self.name
  
  
class Port_Indi(models.Model):
  ''' Portfilio or Individual '''
  
  cash = models.IntegerField()
  
  last_quote = models.ForeignKey(Quote)
  last_activity = models.ForeignKey(Activity)
  
  networth = models.IntegerField()
  
  ''' Individual
  - Can invest in Porfolio 
  - Can invest in Stock
  - Cannot invest in another Individual
  '''
  is_individual = models.BooleanField()
  
  ''' Portfolio
  - Can invest in Stock
  - Cannot invest in Porfolio or Individual
  '''
  
  def __unicode__(self):
    return self.name


class Historical_Data(models.Model):
  ''' Historical Data recorded on a given day for a specific company '''
  company = models.ForeignKey(Company)  
  date = models.DateTimeField
  opening = models.IntegerField()
  closing = models.IntegerField()
  high =  models.IntegerField()
  low = models.IntegerField()
  volume = models.IntegerField()
  adj_close = models.IntegerField()
  
  def __unicode__(self):
    return self.name
  

