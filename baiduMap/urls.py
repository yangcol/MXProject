#encoding:utf-8
from django.conf.urls import patterns, include, url
from views import home
__author__ = 'yangq'
urlpatterns = patterns('',
     url(r'^/$', home),
)
