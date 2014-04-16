# Views for Dataloader appication
from django.http import HttpResponse
import dataloader as d

def dataloader(request):
    name = 'Dylan'
    html = '<html><body background="http://colourlovers.com.s3.amazonaws.com/images/patterns/1202/1202172.png">Hi %s. this is your resume!</body></html>' % name
    
    d.input_company_hist()
    
    return HttpResponse(html)    

