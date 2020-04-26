from django.shortcuts import render
from operator import attrgetter
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = list(Phone.objects.all())

    sort_type = request.GET.get('sort')
    if sort_type == 'name':
        phones = sorted(phones, key=attrgetter('name'))
    elif sort_type == 'min_price':
        phones = sorted(phones, key=attrgetter('price'))
    elif sort_type == 'max_price':
        phones = sorted(phones, key=attrgetter('price'), reverse=True)

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
