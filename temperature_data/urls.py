from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name ='home'),
    path('display_data', views.display_data, name ='display_data'),
    path('countries',views.load_countrydata, name='load_countrydata'),
    path('country_list/<country_name>',views.country_details, name='country_details'),
    path('states',views.load_statedata, name='load_statedata'),
    path('cities',views.load_citiesdata, name='load_citiesdata'),
    path('visualize/',views.visualize, name='visualize'),
    path('countrychart/',views.country_chart, name='country_chart'),
    path('statechart/',views.state_chart, name='state_chart'),
    path('citychart/',views.city_chart, name='city_chart'),
]
