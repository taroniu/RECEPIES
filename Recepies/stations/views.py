import csv
from Recepies.settings import BUS_STATION_CSV
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render


# Create your views here.
def bus_stations(request):

    names_list = []
    streets_list = []
    district_list = []
    with open(BUS_STATION_CSV, newline='') as filer:
        reader = csv.DictReader(filer, delimiter=';')
        for row in reader:
            names_list.append(row['Name'])
            streets_list.append(row['PlaceDescription'])
            district_list.append(row['District'])

    CONTENT = list(zip(names_list, streets_list, district_list))

    page_number = int(request.GET.get('page', 1))
    p = Paginator(CONTENT, 10)
    page = p.get_page(page_number)

    context = {
        'page': page
    }

    return render(request, 'stations/stations.html', context)

