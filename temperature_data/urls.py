from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('heatmap', views.heatmap, name = 'heatmap'),
    path('average_data', views.average_data, name = 'average'),
    path('specific_data/<str:table_name>/<str:row_id>', views.full_data, name = 'specific'),
]
