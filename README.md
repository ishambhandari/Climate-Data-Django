# Climate Data Application using Django
This application shows the global temperature trend collected from the historical data of the 1750s across the different countries, states, and cities in the world. This application is made using Django, a python web application framework and deployed in AWS.

The data used for the application can be found here https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data . We have made use of only three csv files : country, state and city for our application.

#### Creating Django application
We will set up the virtual environment and download Django for our application using these commands:

    pyenv local 3.10.7          # sets the local version for python
    python3 -m venv .venv       # creates virtual evironment 
    source .venv/bin/activate   # activates the virtual environment
    pip install --upgrade pip   # installs pip if update is required
    pip install django          # installs django
Now we will start creating the site using django admin tools also creating the application respectively, using this command:

    django-admin startproject mysite .
    
We need to specify some settings for the site, for that open the settings.py file and add import os in the first line, provide the url in ALLOWED_HOSTS to run beyond localhost. Also specify the app name in the INSTALLED_APPS ['temperature_data',].

    python3 manage.py startapp temperature_data
A new folder temperature_data will be created with relevant files for database mapping and server side interactions.

#### Creating Models
We will first parse the csv files, for that we create parse_data1.py in the /temperature_data/management/commands folder and create database tables for our application using SQLite3. Open the models.py file and start adding the tables here.

We have three tables country, state and city with their associated primary keys and foreign keys in the Country_data, State_data and City_data tables. There are also separate tables showing the average temperature for every country, city and state.

Now we need to create migration file for Django which loads the models into the database using this command:

    python3 manage.py makemigrations temperature_data
    python3 manage.py migrate temperature_data

#### Creating Views and Templates

Create the views for the application in the views.py file, which has different methods and the logic added to view every HTML page. Create the HTML pages in the templates/temperature_data folder. 

    from django.shortcuts import render
    from django.core.paginator import Paginator
    from .models import Country, City, State, Country_data, City_data, State_data, Country_average, City_average, State_average

    # Create your views here.
    def index(request):
    return render(request, 'temperature_data/index.html')

Provide the path for the associated view and HTML page in the urls.py file like this:

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


Open mysite/urls.py and add the application name url to be included

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('temperature_data.urls'))
    ]

Check everything is running fine on server, type this command in terminal to run the server: 

    python3 manage.py runserver 0.0.0.0:8000

#### Creating visuals for data

#### Deployment