from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('countries',views.load_countrydata, name='load_countrydata'),
    path('states',views.load_statedata, name='load_statedata'),
    path('cities',views.load_citiesdata, name='load_citiesdata'),
]
