from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('load_countrydata/',views.load_countrydata, name='load_countrydata'),
]
