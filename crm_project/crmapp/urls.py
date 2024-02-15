# crmapp/urls.py
from django.urls import path
from .views import home

urlpatterns = [
    #path('countries/', country_list, name='country_list'),
    path('', home, name='home'),
]
