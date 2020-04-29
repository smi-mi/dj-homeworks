from datetime import datetime
from django.shortcuts import render
from .models import Book


def books_view(request, date: datetime = None):
    template = 'books/books_list.html'
    context = {}
    if date:
        prev_date_book = Book.objects.filter(pub_date__lt=date).order_by("-pub_date").first()
        if prev_date_book:
            prev_date = prev_date_book.pub_date
            context['prev_date'] = prev_date
        next_date_book = Book.objects.filter(pub_date__gt=date).order_by("pub_date").first()
        if next_date_book:
            next_date = next_date_book.pub_date
            context['next_date'] = next_date
        books = Book.objects.filter(pub_date=date).all()
    else:
        books = Book.objects.all()
    context['books'] = books
    return render(request, template, context)
