from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    context = {}

    ordering = '-published_at'
    object_list = Article.objects.order_by(ordering).all()
    context['object_list'] = object_list

    return render(request, template, context)
