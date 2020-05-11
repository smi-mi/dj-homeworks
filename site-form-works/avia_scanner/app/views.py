import time
import random

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    term = request.GET.get('term', '')
    results = cache.get(term)
    if not results:
        results = list(City.objects.filter(name__startswith=term).values_list('name', flat=True))
        cache.set(term, results)
    return JsonResponse(results, safe=False)
