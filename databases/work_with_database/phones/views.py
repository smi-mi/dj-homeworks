from django.shortcuts import render
from operator import attrgetter
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects

    sort_type = request.GET.get('sort')
    if sort_type == 'name':
        phones = phones.order_by('name')
    elif sort_type == 'min_price':
        phones = phones.order_by('price')
    elif sort_type == 'max_price':
        phones = phones.order_by('-price')

    context = {'phones': phones.all()}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
