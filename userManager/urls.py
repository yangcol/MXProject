__author__ = 'yangq'
#encoding:utf-8
from django.conf.urls import patterns, include, url
from views import show, debug
urlpatterns = patterns(
    '',
    url(r'^/$', show),
    url(r'init/$', debug),
)