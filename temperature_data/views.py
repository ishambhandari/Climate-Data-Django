from django.shortcuts import render,get_object_or_404
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

def search_country(request):
    country_search = request.GET.get('search')
    countries = Country.objects.all()   
    if country_search:
        countries = countries.filter(country__icontains=country_search)
    else:
        countries = None
    return render(request, 'temperature_data/search_country.html',{'countries':countries,'country_search':country_search})

def country_details(request,country_name):
    country_name = Country.objects.filter(country=country_name).first()
    print('this is country name', country_name)
    country_list = Country_data.objects.all()
    context = {
        'country_name' : country_name,
        'country_list' : country_list,
    }
    return render(request,'temperature_data/country_details.html',context) 

def visualize(request):
    if requested.method == 'POST':
        selected_option = request.POST.get('dropdown')
        if selected_option == 'option1':
            return render(request,'temperature_data/country_chart.html')
        elif selected_option == 'option2':
            return render(request,'temperature_data/state_chart.html')
        elif selected_option == 'option3':
            return render(request,'temperature_data/city_chart.html')
        else:
    return render(request,'temperature_data/visualize.html')

def country_chart(request):
    countries = Country_data.objects.all()
    date = [c.date for c in countries]
    average_temperature = [c.average_temperature for c in countries]
    data = {'labels':date, 'data':average_temperature}
    chart = json.dumps(data)
    return render(request,'temperature_data/country_chart.html',{'chart':chart})

def state_chart(request):
    states = State_data.objects.all()
    date = [s.date for s in states]
    average_temperature = [s.average_temperature for s in states]
    data = {'labels':date, 'data':average_temperature}
    chart = json.dumps(data)
    return render(request,'temperature_data/state_chart.html',{'chart':chart})

def city_chart(request):
    cities = City_data.objects.all()
    date = [ci.date for ci in cities]
    average_temperature = [ci.average_temperature for ci in cities]
    data = {'labels':date, 'data':average_temperature}
    chart = json.dumps(data)
    return render(request,'temperature_data/city_chart.html',{'chart':chart})

def load_statedata(request):
    states = State.objects.all()
    return render(request,'temperature_data/load_statedata.html',{'states':states})

def load_citiesdata(request):
    cities = City.objects.all()
    return render(request,'temperature_data/load_citiesdata.html',{'cities':cities})
    
