from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"

    form = CalcForm(request.GET)
    if form.is_valid():
        initial_fee = int(form.data['initial_fee'])
        rate = int(form.data['rate'])
        months_count = int(form.data['months_count'])

        common_result = initial_fee + initial_fee * rate // 100
        result = common_result // months_count

        context = {'form': form,
                   'common_result': common_result,
                   'result': result,
                   }
    else:
        context = {'form': form}

    return render(request, template, context)
