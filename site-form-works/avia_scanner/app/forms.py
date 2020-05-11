from django import forms
from datetime import date

from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    city_from = forms.CharField(max_length=50, label='Город отправления', widget=AjaxInputWidget('/api/city_ajax'))
    city_to = forms.CharField(max_length=50, label='Город прибытия')
    date = forms.DateField(initial=date.today, label='Дата', widget=forms.SelectDateWidget)
