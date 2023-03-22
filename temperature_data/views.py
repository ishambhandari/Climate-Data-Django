from django.shortcuts import render
from .models import Country_data,State_data,City_data

# Create your views here.
def index(request):
    countries = Country_data.objects.all()[:5]          # loads only first five entries for country
    states = State_data.objects.all()[:5]
    cities = City_data.objects.all()[:5]
    context = {
        'countries':countries,
        'states': states,
        'cities': cities,
    }
    return render(request, 'temperature_data/index.html',context)

def load_countrydata(request):
    countries = Country_data.objects.all()          # loads complete entries for country
    return render(request, 'temperature_data/load_countrydata.html',{'countries':countries})

def load_statedata(request):
    states = State_data.objects.all()
    return render(request,'temperature_data/load_statedata.html',{'states':states})

def load_citiesdata(request):
    cities = City_data.objects.all()
    return render(request,'temperature_data/load_citiesdata.html',{'cities':cities})
    
