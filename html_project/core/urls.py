from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'profit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<project>\w+)/(?P<template>\w+).html/$', 'core.views.template', name='template'),
    # url(r'^admin/', include(admin.site.urls)),
]

# rest api
#
#urlpatterns += [    
#]
