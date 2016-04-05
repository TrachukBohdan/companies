# -*- coding:utf-8 -*-
 
from django.forms import CharField, Form
from django import forms
 
class Main_Company_Form(Form):
    name_company = CharField(
        label='Name company', 
        max_length=100, 
        error_messages={'required': 'Input name company'})
    established_company = CharField(
        label='Company Estimated Earnings', 
        max_length = 100,
        error_messages={'required':'Input company estimated earnings'})