# crmapp/views.py
from django.shortcuts import render
from .models import Country

#def country_list(request):
#    countries = Country.objects.all()
#    return render(request, 'country_list.html', {'countries': countries})

def home(request):
    countries = Country.objects.all()
    return render(request, 'home.html', {'countries': countries})