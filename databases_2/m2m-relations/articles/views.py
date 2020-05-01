from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Relationship


def articles_list(request):
    template = 'articles/news.html'
    context = {'object_list': []}

    ordering = '-published_at'
    object_list = Article.objects.order_by(ordering).prefetch_related('scopes').all()
    for article in object_list:
        context['object_list'].append(
            (article,
             Relationship.objects.filter(article__id=article.id).order_by('-is_main', 'scope__name').all(),
             )
        )

    return render(request, template, context)
