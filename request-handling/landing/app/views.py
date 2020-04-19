from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    from_landing = request.GET.get('from-landing')
    if from_landing is not None:
        counter_click[from_landing] += 1
    return render_to_response('index.html')


def landing(request):
    landing_type = request.GET.get('ab-test-arg', 'original')
    counter_show[landing_type] += 1
    if landing_type == 'test':
        return render_to_response('landing_alternate.html')
    return render_to_response('landing.html')


def stats(request):
    test = counter_click['test'] / counter_show['test'] if counter_show['test'] != 0 else 0.0
    original = counter_click['original'] / counter_show['original'] if counter_show['original'] != 0 else 0.0
    return render_to_response('stats.html', context={
        'test_conversion': test,
        'original_conversion': original,
    })
