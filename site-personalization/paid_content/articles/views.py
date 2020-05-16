from django.shortcuts import render, get_object_or_404
from .models import Article


def show_articles(request):
    return render(
        request,
        'articles.html',
        context={
            'articles': Article.objects.all()
        }
    )


def show_article(request, id):
    article = get_object_or_404(Article, id=id)
    return render(
        request,
        'article.html',
        context={
            'article': article
        }
    )


def pay_view(request):
    if request.method == 'POST':
        request.user.did_pay = True
        request.user.save()
    return render(request, 'pay.html')
