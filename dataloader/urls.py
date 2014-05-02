# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('dataloader.views',
    url(r'^investing/$', 'investing', name='investing'),
)