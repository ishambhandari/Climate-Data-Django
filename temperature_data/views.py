from django.shortcuts import render
from .models import Country_data

# Create your views here.
def index(request):
    countries = Country_data.objects.all()[:5]
    return render(request, 'temperature_data/index.html',{'countries':countries})

def load_countrydata(request):
    countries = Country_data.objects.all()
    return render(request, 'temperature_data/load_countrydata.html',{'countries':countries})
