from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Country, City, State, Country_data, City_data, State_data, Country_average, City_average, State_average

# Create your views here.
def index(request):
    return render(request, 'temperature_data/index.html')

def heatmap(request):
    average_city_data = City_average.objects.all()
    for i in average_city_data:
        i.latitude = i.latitude[:-1]
        i.longitude = i.longitude[:-1]
        i.average_temperature = int(i.average_temperature)

    return render(request, 'temperature_data/Heatmap.html', {'data':average_city_data})

def places(request, category, item, date = None):
    if request.method == 'GET':
        city = City.objects.all()
        state  = State.objects.all()
        country = Country.objects.all()
        return render(request,'temperature_data/compare_graph.html', {'city':city, 'state':state, 'country':country} )
    



def average_data(request):
    parameter = request.POST.get('selected_value')
    page_number = request.GET.get('page', 1)
    state = request.GET.get("state") if request.GET.get('state') else parameter
    page_size = 10 # number of items per page
    if state == 'city':
        data = City_average.objects.all()
        paginator = Paginator(data, page_size)
        page_obj = paginator.get_page(page_number)

    elif state == 'state':
        data = State_average.objects.all()
        paginator = Paginator(data, page_size)
        page_obj = paginator.get_page(page_number)
    else:
        data =Country_average.objects.all()
        # Use Django's Paginator to paginate the data
        paginator = Paginator(data, page_size)
        page_obj = paginator.get_page(page_number)

    return render(request, 'temperature_data/average_temperature.html', {'data': page_obj, 'param': state})

def full_data(request):
    table_name = request.GET.get('table')
    row_id = request.GET.get('row')
    row_id = row_id.split(',')[0]

    graph = request.GET.get('graph') if request.GET.get('graph') else None
    page_number = request.GET.get('page', 1)
    page_size = 10
    if table_name == 'city':
        cid = City.objects.filter(city_id = int(row_id)).first()
        data =  City_data.objects.filter(city_id = cid)
        param = 'city'
        paginator = Paginator(data, page_size)
        page_obj = paginator.get_page(page_number)
        name = cid.city

    elif table_name == 'state':
        sid = State.objects.filter(state_id = int(row_id)).first()
        data = State_data.objects.filter(state_id= sid)
        param  = 'state'
        paginator = Paginator(data, page_size)
        page_obj = paginator.get_page(page_number)
        name = sid.state
    else:
        cid = Country.objects.filter(country_id = int(row_id)).first()
        data = Country_data.objects.filter(country_id= cid)
        param = 'country'
        paginator = Paginator(data, page_size)
        page_obj = paginator.get_page(page_number)
        name = cid.country

    if graph != None:
        temp_data = []
        labels = []
        for x in data:
            if x.average_temperature.strip():
                temp_data.append(float(x.average_temperature))
                labels.append(x.date.strftime("%Y-%m-%d"))
        
        return render(request, 'temperature_data/graph.html', {'data':temp_data, 'param':param, 'row_id':row_id, 'labels':labels, 'graph_name':name})
    return render(request,'temperature_data/temperature_detail.html', {'data':page_obj, 'param':param, 'row_id':row_id} )


    

