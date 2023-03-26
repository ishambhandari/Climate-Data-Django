from django.shortcuts import render
from .models import Country, City, State, Country_data, City_data, State_data

# Create your views here.
def index(request):
    return render(request, 'temperature_data/index.html')

