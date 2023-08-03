from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('heatmap', views.heatmap, name = 'heatmap'),
    # path('compare_graph', views.places, name = 'graph'),
    path('average_data', views.average_data, name = 'average'),
    path('specific_data/', views.full_data, name = 'specific'),
    path('compare_data', views.compare_graph, name = 'compare')
]
