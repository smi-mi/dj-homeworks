import csv
from django.shortcuts import render


def inflation_view(request):
    template_name = 'inflation.html'

    context = {'data': []}
    with open('inflation_russia.csv', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for i, row in enumerate(reader):
            if i > 0:
                row = [float(e) if e and j > 0 else e for j, e in enumerate(row)]
                context['data'].append(row)
    return render(request, template_name,
                  context)
