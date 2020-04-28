from django.shortcuts import render
from .models import Iphone, Samsung, Mi


def show_catalog(request):
    template = 'catalog.html'
    context = {'iphone': Iphone.objects.first(),
               'samsung': Samsung.objects.first(),
               'mi': Mi.objects.first(),
               }
    return render(
        request,
        template,
        context
    )
