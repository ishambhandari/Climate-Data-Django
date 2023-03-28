from django.shortcuts import render
from .models import Country, City, State, Country_data, City_data, State_data, Country_average, City_average, State_average

# Create your views here.
def index(request):
    return render(request, 'temperature_data/index.html')

def place_names(request, parameter = 'country'):
    if parameter == 'city':
        data = City.objects.all()
        return render(request,'temperature_data/places.html', {'data':data} )

    elif parameter == 'state':
        data  = State.objects.all()
        return render(request,'temperature_data/places.html', {'data':data} )
    
    data = Country.objects.all()
    return render(request,'temperature_data/places.html', {'data':data} )



def average_data(request):
    parameter = request.POST.get('selected_value')
    print("this is parameter", parameter)
    if parameter == 'city':
        data = {
                "data" : City_average.objects.all(),
                "param" : 'city' 
                }

        return render(request,'temperature_data/average_temperature.html', {'data':data} )

    elif parameter == 'state':
        data = {
                "data" : State_average.objects.all(),
                "param" : 'state', 
                }
        return render(request,'temperature_data/average_temperature.html', {'data':data} )

    data = {
            "data" :Country_average.objects.all(),
            "param" : 'country',
            }
    # print(data)
    return render(request,'temperature_data/average_temperature.html', {'data':data} )

def full_data(request, table_name, row_id ):
    row_id = row_id.split(',')[0]
    if table_name == 'city':
        cid = City.objects.filter(city_id = int(row_id)).first()
        print('this is cid', cid)
        data = {
                "data": City_data.objects.filter(city_id = cid),
                "param" : 'city'
                }
        return render(request,'temperature_data/temperature_detail.html', {'data':data} )

    elif table_name == 'state':
        sid = State.objects.filter(state_id = int(row_id)).first()
        data  = {
                "data":State_data.objects.filter(state_id= sid),
                "param" : 'state'
                }
        return render(request,'temperature_data/temperature_detail.html', {'data':data} )
    cid = Country.objects.filter(country_id = int(row_id)).first()
    data = {
            "data" : Country_data.objects.filter(country_id= row_id),
            "param" : 'country'
            }

    return render(request,'temperature_data/temperature_detail.html', {'data':data} )
    

