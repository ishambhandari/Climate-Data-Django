from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Country, City, State, Country_data, City_data, State_data, Country_average, City_average, State_average

# Create your views here.
def index(request):
    return render(request, 'temperature_data/index.html')

def compare_graph(request):
    if request.method == 'GET':
        return render(request, 'temperature_data/compare_graph.html')

    #Getting the parameters from post request
    table1 = request.POST.get('table1')
    table2= request.POST.get('table2')
    name1 = request.POST.get('name1')
    name2= request.POST.get('name2')
    print('table', table2)
    print('name', name2)
    data_list = []
    data_list2 = []
    label1 = []
    label2 = []
    if table1 == 'country':
        cid = Country.objects.filter(country = name1).first()
        data = Country_data.objects.filter(country_id = cid)
        for i in data:
            data_list.append(i.average_temperature)
            label1.append(i.date.strftime("%Y-%m-%d"))
    elif table1 == 'city':
        cid = City.objects.filter(city = name1).first()
        data = City_data.objects.filter(city_id = cid)
        for i in data:
            data_list.append(i.average_temperature)
            label1.append(i.date.strftime("%Y-%m-%d"))
    elif table1 == 'state':
        sid = State.objects.filter(state = name1).first()
        data = State_data.objects.filter(state_id = sid)
        for i in data:
            data_list.append(i.average_temperature)
            label1.append(i.date.strftime("%Y-%m-%d"))
    if table2 == 'country':
        cid = Country.objects.filter(country = name2).first()
        data = Country_data.objects.filter(country_id = cid)
        for i in data:
            data_list2.append(i.average_temperature)
            label2.append(i.date.strftime("%Y-%m-%d"))

    elif table2 == 'city':
        cid = City.objects.filter(city = name2).first()
        data = City_data.objects.filter(city_id = cid)
        for i in data:
            data_list2.append(i.average_temperature)
            label2.append(i.date.strftime("%Y-%m-%d"))
    elif table2 == 'state':
        cid = State.objects.filter(state = name2).first()
        data = State_data.objects.filter(state_id = cid)
        for i in data:
            data_list2.append(i.average_temperature)
            label2.append(i.date.strftime("%Y-%m-%d"))
    return render(request, 'temperature_data/compare_graph.html', {'data1':data_list,'label1':label1, 'param1':table1, 'name1' : name1, 'data2':data_list2, 'label2': label2,  'param2':table2, 'name2':name2})

def heatmap(request):
    average_city_data = City_average.objects.all()
    for i in average_city_data:
        i.latitude = i.latitude[:-1]
        i.longitude = i.longitude[:-1]
        i.average_temperature = int(i.average_temperature)

    return render(request, 'temperature_data/Heatmap.html', {'data':average_city_data})

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




    

