#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Main_Company(models.Model): # создание моделей
	name_company = models.CharField(max_length = 100)
	established_company = models.CharField(max_length = 100)
	parent_id = models.CharField(max_length = 100)

