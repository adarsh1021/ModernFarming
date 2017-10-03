from django.conf.urls import url
from django.contrib import admin
from . views import *

app_name = 'soil'

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^analyze/$', analyze, name="analyze"),
    url(r'^analyze-sample/(?P<port>[\w\-]+)$', analyze_sample, name="analyze_sample"),
]
