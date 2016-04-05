#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from Company import views


urlpatterns = [
    url(r'^send/$', views.showReq),
    url(r'^$', views.registrate),
    #url(r'^$', views.SumSb),
    url(r'^del/(P?[0-9]*)$', views.deleteCompany),
    url(r'^edit/(P?[0-9]*)$', views.editCompany),
    url(r'^add/(P?[0-9]*)$', views.registrate),
  	url(r'^tree/(P?[0-9]*)$', views.tree_page),
]
