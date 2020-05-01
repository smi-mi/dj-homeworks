from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'

    ordering = '-published_at'
    object_list = Article.objects.only('image', 'title', 'text', 'genre').\
        order_by(ordering).select_related('genre').all()
    context = {'object_list': object_list}

    return render(request, template_name, context)
