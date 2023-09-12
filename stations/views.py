import csv

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        stations = list(reader) 
    stations_paginator = Paginator(stations, 10)
    cur_page = request.GET.get('page', 1)
    page = stations_paginator.get_page(cur_page)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
