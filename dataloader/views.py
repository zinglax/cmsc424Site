# Views for Dataloader appication
from django.http import HttpResponse
from django.shortcuts import render_to_response
import dataloader as d
import yahooDataRetriever
import investment_manager

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import Document
from forms import DocumentForm
from forms import FileForm

from itertools import chain

from models import *
from django.conf import settings

ticker_file = "./dataloader/SandP500TickerSymbols.txt"


def dataloader(request):
  name = 'Dylan'
  html = '<html><body>Historical Data and companies are now objectified in a sqlite3 database</body></html>' 

  # Testing
  #d.input_company_hist_test()

  # Methods to load data
  d.input_companies()  
  d.input_company_hist()

    
  return HttpResponse(html)    

def home(request):
  
  results = yahooDataRetriever.get_top_500_tickers(ticker_file)
  results.sort()
  
  return render_to_response("nav/home.html", {'results':results})



def investing(request):
  # Handle file upload
  file_form = FileForm(request.POST)
  form = DocumentForm(request.POST, request.FILES)
  
  
  if request.method == 'POST' and "uploadFile" in request.POST:
    # Upload
    if form.is_valid():
      newdoc = Document(docfile = request.FILES['docfile'])
      newdoc.save()
  
      # Redirect to the document list after POST
      return HttpResponseRedirect(reverse('dataloader.views.investing'))
  elif request.method == 'POST' and "invest" in request.POST:  
    # Make Investments
    if file_form.is_valid():
      file_name = file_form.cleaned_data['file_input']
      print "### FILE FOR INVESTMENTS: " + file_name
      file_path = settings.MEDIA_ROOT + "/" + file_name
      print file_path
      
      cr = csv.reader(open(file_path))    
      # Starting from second row
      
      for row in cr:
        if row[0] == 'fund' or row[0] == 'individual':
          investment_manager.fund(row)
        elif row[0] == 'buy':
          investment_manager.buy(row)
        elif row[0] == 'sell':
          investment_manager.sell(row)
        elif row[0] == 'sellbuy':
          investment_manager.sellbuy(row)
                        
      
      
      return HttpResponseRedirect(reverse('dataloader.views.investing'))

  elif request.method == 'POST' and "clear" in request.POST:   
    # Clear Investments
    print "### This should clear everything"
    Activity.objects.all().delete()
    StakeHold.objects.all().delete()
    Port_Indi.objects.all().delete()
    print "### OK check porfolio page"
    
    
  else:
      form = DocumentForm() # A empty, unbound form
      file_form = FileForm()

  # Load documents for the list page
  documents = Document.objects.all()

  return render_to_response(
       'nav/investing.html',
       {'documents': documents, 'form': form, 'file_form':file_form},
       context_instance=RequestContext(request)
   )

def portfolios(request):
  ports = Port_Indi.objects.filter(is_individual=False)
  indies = Port_Indi.objects.filter(is_individual=True)
  
  return render_to_response("nav/portfolios.html", {'portfolios':ports,'individuals':indies})
  
def port_indi_page(request, port_indi):
  name = port_indi
  
  #ports = Port_Indi.objects.filter(name=port_indi)
  pi = Port_Indi.objects.get(name=port_indi)
  #pi = ports[0]
  
  #activities = Activity.objects.filter(port_indi1=pi).values('act_type','amount','company','port_indi1','port_indi2')
  #activities2 = Activity.objects.filter(port_indi2=pi).values('act_type','amount','company','port_indi1','port_indi2')

  activities = Activity.objects.filter(port_indi1=pi).values()
  activities2 = Activity.objects.filter(port_indi2=pi).values()
  
  stocks = StakeHold.objects.filter(fund=pi)
      
  results = list(chain(activities,activities2))
  
  
  

  
  return render_to_response("nav/portfolio.html", {'port':pi, 'activities':results, 'stocks':stocks})

def company(request, company):
  comp = Company.objects.get(ticker=company)
  hist = Historical_Data.objects.filter(company=comp)
  name = comp.name
  
  
  
  return render_to_response("nav/company.html", {'name':name,'hist':hist})
  

def queries(request):
  
  return render_to_response("nav/queries.html", {})


def misc(request):
  
  return render_to_response("nav/misc.html", {})


