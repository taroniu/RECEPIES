from django.shortcuts import render
import csv
from django.http import HttpResponse
from Recepies.settings import BUS_STATION_CSV
# Create your views here.
def bus_stations(request):

    a = {}
    with open(BUS_STATION_CSV, newline='') as filer:
        reader = csv.DictReader(filer)
    return HttpResponse(f'{reader}')
