from django.conf.urls import url
from django.contrib import admin
from . views import *

app_name = 'soil'

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^analyze/$', analyze, name="analyze"),
    url(r'^analysis-history/$', analysis_history, name="analysis_history"),
    url(r'^analyze-sample/(?P<port>[\w\-]+)$', analyze_sample, name="analyze_sample"),
    url(r'^calibrate/$', calibrate, name="calibrate"),
    url(r'^calibrate-sample/(?P<port>[\w\-]+)$', calibrate_sample, name="calibrate_sample"),
    url(r'^calibrate-save/(?P<result>.*)$', calibrate_save, name="calibrate_save"),
    url(r'^analysis-save/(?P<result>.*)$', analysis_save, name="analysis_save"),
]
