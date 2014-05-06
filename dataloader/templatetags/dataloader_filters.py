from django import template
from dataloader.models import *

register = template.Library()

@register.filter(name='replace')
def replace(value):
  return value.replace(".","_")

@register.filter(name='get_port_indi')
def get_port_indi(value):
  print value
  if value == '':
    return ''
  else:
    print value
    port = Port_Indi.objects.get(pk=value)
  
  print 'HELLO' + port.name
  return port.name