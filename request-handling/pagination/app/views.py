from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
from csv import DictReader
from urllib import parse


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding='cp1251') as data:
        stations_all = list(DictReader(data))
    paginator = Paginator(stations_all, 10)
    current_page = request.GET.get('page', 1)
    stations = paginator.get_page(current_page)

    next_page_url, prev_page_url = None, None
    if stations.has_next():
        next_page_url = reverse(bus_stations) + '?' + parse.urlencode({'page': stations.next_page_number()})
    if stations.has_previous():
        prev_page_url = reverse(bus_stations) + '?' + parse.urlencode({'page': stations.previous_page_number()})

    return render_to_response('index.html', context={
        'bus_stations': stations,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

