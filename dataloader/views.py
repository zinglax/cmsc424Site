# Views for Dataloader appication
from django.http import HttpResponse
from django.shortcuts import render_to_response
import dataloader as d
import yahooDataRetriever

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import Document
from forms import DocumentForm



from models import *

ticker_file = "./dataloader/SandP500TickerSymbols.txt"


def dataloader(request):
  name = 'Dylan'
  html = '<html><body background="http://colourlovers.com.s3.amazonaws.com/images/patterns/1202/1202172.png">Historical Data and companies are now objectified in a sqlite3 database</body></html>' 

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
  if request.method == 'POST':
      form = DocumentForm(request.POST, request.FILES)
      if form.is_valid():
          newdoc = Document(docfile = request.FILES['docfile'])
          newdoc.save()

          # Redirect to the document list after POST
          return HttpResponseRedirect(reverse('dataloader.views.investing'))
  else:
      form = DocumentForm() # A empty, unbound form

  # Load documents for the list page
  documents = Document.objects.all()

  return render_to_response(
       'nav/investing.html',
       {'documents': documents, 'form': form},
       context_instance=RequestContext(request)
   )


def queries(request):
  
  return render_to_response("nav/queries.html", {})


def misc(request):
  
  return render_to_response("nav/misc.html", {})


