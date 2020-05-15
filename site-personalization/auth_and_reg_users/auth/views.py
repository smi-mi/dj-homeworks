from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(
        request,
        'home.html'
    )


def signup(request):
    context = {
        'form': UserCreationForm
    }
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'success': True
            }
    return render(
        request,
        'signup.html',
        context=context
    )
