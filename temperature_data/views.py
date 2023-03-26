from django.shortcuts import render
from .models import Country,State,City,Country_data,State_data,City_data

# Create your views here.
def index(request):
    return render(request, 'temperature_data/index.html')

def display_data(request):
    countries = Country.objects.all()[:5]          # loads only first five entries for country
    states = State.objects.all()[:5]
    cities = City.objects.all()[:5]
    context = {
        'countries':countries,
        'states': states,
        'cities': cities,
    }
    return render(request, 'temperature_data/display_data.html',context)

def load_countrydata(request):
    countries = Country.objects.all()          # loads complete entries for country
    return render(request, 'temperature_data/load_countrydata.html',{'countries':countries})

def load_statedata(request):
    states = State.objects.all()
    return render(request,'temperature_data/load_statedata.html',{'states':states})

def load_citiesdata(request):
    cities = City.objects.all()
    return render(request,'temperature_data/load_citiesdata.html',{'cities':cities})
    
