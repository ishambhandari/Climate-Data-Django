from django.shortcuts import render
from django.core.paginator import Paginator
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
    page_number = request.GET.get('page', 1)
    print('this is page', page_number)
    state = request.GET.get("state") if request.GET.get('state') else parameter

    print('this is statae', state)
    page_size = 10 # number of items per page
    if state == 'city':
        data = City_average.objects.all()
        paginator = Paginator(data, page_size)
        page_obj = paginator.get_page(page_number)

        return render(request,'temperature_data/average_temperature.html', {'data':page_obj, 'param':state} )

    elif state == 'state':
        data = State_average.objects.all()
        paginator = Paginator(data, page_size)
        page_obj = paginator.get_page(page_number)
        return render(request,'temperature_data/average_temperature.html', {'data':page_obj, 'param':state} )



    data =Country_average.objects.all()
    # Use Django's Paginator to paginate the data
    paginator = Paginator(data, page_size)
    page_obj = paginator.get_page(page_number)

    return render(request, 'temperature_data/average_temperature.html', {'data': page_obj, 'param': state})

def full_data(request, table_name, row_id ):
    print('this is table name', table_name)
    row_id = row_id.split(',')[0]
    print('this is row id', row_id)
    page_number = request.GET.get('page', 1)
    page_size = 10
    if table_name == 'city':
        print('here')
        cid = City.objects.filter(city_id = int(row_id)).first()
        print('this is cid', cid)
        data =  City_data.objects.filter(city_id = cid)
        param = 'city'
        paginator = Paginator(data, page_size)
        page_obj = paginator.get_page(page_number)

    elif table_name == 'state':
        print('state here')
        sid = State.objects.filter(state_id = int(row_id)).first()
        data = State_data.objects.filter(state_id= sid)
        param  = 'state'
        paginator = Paginator(data, page_size)
        page_obj = paginator.get_page(page_number)
        # print('country here')
    else:
        cid = Country.objects.filter(country_id = int(row_id)).first()
        data = Country_data.objects.filter(country_id= cid)
        param = 'country'
        paginator = Paginator(data, page_size)
        page_obj = paginator.get_page(page_number)
    return render(request,'temperature_data/temperature_detail.html', {'data':page_obj, 'param':param} )
    

