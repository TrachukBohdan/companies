#!/usr/bin/python
# -*- coding: utf-8 -*-
#from django.core.management.base import BaseCommand
import pprint

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
 
# Это наша форма, которую мы определим в forms.py
from .forms import Main_Company_Form
from .models import Main_Company

def registrate(request, id=0):#функция принимает id

    form= Main_Company_Form(request.POST)# вызываем форму заполнения с forms.py
    
    if request.POST: 
        company = Main_Company(
            name_company=request.POST['name_company'], 
            established_company=request.POST['established_company'], 
            parent_id = id,
    

        );
        #print(id, company.name_company);
        print(company.parent_id)
        print(id)
        print(company.established_company)
        if company.parent_id == 0:
            for company.parent_id in Main_Company.objects.get():
                print(company.name_company)
        elif(id ==company.parent_id) and (company.parent_id == company.parent_id):
            print()
        company.save(); # сохранили в базу данных




    
            
          




        return redirect('/'); # обновили страницу
      
    

    return render(
        request, r'Company/Company.html', # подключили html - форму
        {
            'form': form, 
            'data': Main_Company.objects.all(), # список категори 
            'cat_id': id, # когди изменяли данные 
        }
    )



def showReq(request):
    return HttpResponse("Company is %s." % request.POST['name_company']);	

def deleteCompany(request,id):
    company = Main_Company.objects.get(id = id).delete();# по переданому іd удаляем компанию
    return redirect('/')

def tree(parent_id=0):

    companyList = [];
    
    # list of cat with parent_id
    companies = Main_Company.objects.filter(parent_id = parent_id); 
  
    # if cat have childrens
    for company in companies.iterator():
        
        # count children of company
        subCompany = Main_Company.objects.filter(parent_id = company.id)
        print(subCompany.count());
        print('- ' + company.name_company);
            
        # subCompany have children
        if(subCompany.count() != 0):
            companyList.append({
                'name': company.name_company,
                'companies': tree(company.id),
                'id': company.id
            });
        else:
            companyList.append({
                'name': company.name_company,
                'companies': [],
                'id': company.id
            });

    return companyList;

def tree_page(request, id):
    companyList = tree();
    print('-------------------------');

    for company in companyList :
        print()

    return HttpResponse('tree');

def editCompany(request,id):

    company = Main_Company.objects.get(id = id); # вызываем форму по id
    
    if request.POST: # 
        
        company.name_company = request.POST['name_company'];
        company.established_company = request.POST['established_company'];
        company.save();
        return redirect('/')

    form = Main_Company_Form({# копировали форму с заполнеными параметрами
        'name_company': company.name_company,
        'established_company': company.established_company
    });

    return render(
        request, 
        r'Company/Company.html', 
        {
            'form': form, 
            'data': Main_Company.objects.all(),
        }
    );

            
        


    
    


