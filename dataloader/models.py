from django.db import models

import yahooDataRetriever
import csv


# Database structures used to store financial data

class Company(models.Model):
  ''' A S&P500 Company '''
  name = models.CharField(max_length=200,null=True, blank=True)
  ticker = models.CharField(max_length=5,null=True, blank=True)
  
  def __unicode__(self):
    return self.name
  
  '''
  def __init__(self, _name, _ticker):
    self.name = _name
    self.ticker = _ticker
    '''

class Historical_Data(models.Model):
  ''' Historical Data recorded on a given day for a specific company '''
  company = models.ForeignKey('Company',null=True, blank=True)  
  date = models.CharField(max_length=8,null=True, blank=True)
  opening = models.FloatField(null=True, blank=True)
  closing = models.FloatField(null=True, blank=True)
  high =  models.FloatField(null=True, blank=True)
  low = models.FloatField(null=True, blank=True)
  volume = models.FloatField(null=True, blank=True)
  adj_close = models.FloatField(null=True, blank=True)
  
  def __unicode__(self):
    return self.name
  
  '''
  def __init__(self, _company, _date, _opening, _high,
                _low, _closing, _volume, _adj_close):
    #self.company = _company
    self.date = _date
    self.opening = _opening
    self.closing = _closing
    self.high = _high
    self.low = _low
    self.volume = _volume
    self.adj_close = _adj_close
'''

"""
class Quote(models.Model):
  ''' A share price of a company at a specific point in time '''
  # Date
  date = models.DateTimeField()
  
  # Company
  company = models.ForeignKey('Company')
  
  # Listed Price
  price = models.IntegerField()
  
  # Historical data record
  hist = models.ForeignKey('Historical_Data')  
  
  def __unicode__(self):
    return self.name
  
  
 
  def __init__(self, _date, _company, _price, _hist):
    self.date = _date
    self.company = _company
    self.price = _price
    self.hist = _hist
"""

class Port_Indi(models.Model):
  ''' Portfilio or Individual '''
  
  name = models.CharField(max_length=100,null=True, blank=True)
  
  cash = models.IntegerField(null=True, blank=True)
  
  #last_quote = models.ForeignKey('Quote')
  last_activity = models.ForeignKey('Activity',null=True, blank=True)
  
  networth = models.IntegerField(null=True, blank=True)
  
  
  
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
  
  '''
  def __init__(self, _cash, _last_quote, _last_activity,
               _networth, _is_individual):
    self.cash = _cash
    self.last_quote = _last_quote
    self.last_activity = _last_quote
    self.networth = _networth
    self.is_individual = _is_individual
    '''

class Activity(models.Model):
  ''' A buy, sell, or funding '''
  
  # Date
  date = models.CharField(max_length=8,null=True, blank=True)  
  
  # Buy, sell, or fund
  act_type = models.CharField(max_length=50,null=True, blank=True)
  
  # Cash value
  # used for a funding or buying of a specific portfolio or stock
  amount = models.IntegerField(null=True, blank=True)
  
  # Maker of transaction
  port_indi1 = models.ForeignKey('Port_Indi', related_name='port_indi1',null=True, blank=True)
  
  # Secondary fund or stock to purchaise/sell
  port_indi2 = models.ForeignKey('Port_Indi', related_name='port_indi2',null=True, blank=True)
  company = models.ForeignKey('Company',null=True, blank=True)
  
  def __unicode__(self):
    return self.name
  
  '''
  def __init__(self, _act_type, _amount, _fund, _fund2,
               _company):
    self.act_type = _act_type
    self.amount = _amount
    self.fund = _fund
    self.fund2 = _fund2
    self.company = _company
  '''
  



class StakeHold(models.Model):
  ''' Ownership of a Stock or another Fund '''
  
  # Date of last modified
  last_modified = models.CharField(max_length=8,null=True, blank=True)
  last_activity = models.ForeignKey('activity',null=True, blank=True) 
  
  # Owner
  fund = models.ForeignKey('Port_Indi',related_name='fund',null=True, blank=True)
  
  ''' StakeHold in a Stock '''
  company = models.ForeignKey('Company',null=True, blank=True)
  shares = models.FloatField(null=True, blank=True)
  #last_quote = models.ForeignKey('Quote')
  
  ''' StakeHold in a Fund '''
  fund2 = models.ForeignKey('Port_Indi',related_name='fund2',null=True, blank=True)  
  percentage = models.FloatField(null=True, blank=True)  
  

  def __unicode__(self):
    return self.name 
  
  
  '''
  def __init__(self, _last_modified, _fund, _company, _amount, _last_quote, _fund2, _percentage):
    self.last_modified = _last_modified
    self.fund = _fund
    self.company = _company
    self.amount = _amount
    self.last_quote = _last_quote
    self.fund2 = _fund2
    self.percentage =  _percentage
  '''
  

class Document(models.Model):
    docfile = models.FileField(upload_to='.')


