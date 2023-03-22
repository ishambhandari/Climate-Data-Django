from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('load_countrydata/',views.load_countrydata, name='countrylist'),
    path('load_statedata/',views.load_statedata, name='statelist'),
    path('load_citiesdata/',views.load_citiesdata, name='citieslist'),
]
