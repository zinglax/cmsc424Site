from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cmsc424Site.views.home', name='home'),
    # url(r'^cmsc424Site/', include('cmsc424Site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    # dataloader
    url(r'^dataloader/', 'dataloader.views.dataloader', name='resume'),
    
    # home
    url(r'^$', 'dataloader.views.home', name='home'),
    #url(r'^investing/', 'dataloader.views.investing', name='investing'),    
    
    url(r'^portfolios/', 'dataloader.views.portfolios', name='portfolios'),
    #url(r'^portfolio/', 'dataloader.views.port_indi_page', name='port_indi_page'), 
    url(r'^portfolio/(?P<port_indi>\w+)/$', 'dataloader.views.port_indi_page', name='port_indi_page'),     
    url(r'^queries/', 'dataloader.views.queries', name='queries'),    
    url(r'^misc/', 'dataloader.views.misc', name='misc'),    
    
    url(r'^company/(?P<company>\w+)/$', 'dataloader.views.company', name='company'),  
    #url(r'^company/', 'dataloader.views.company', name='company'),  

    (r'^', include('dataloader.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    

