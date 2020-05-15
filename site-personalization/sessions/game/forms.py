from django import forms


class AttemptForm(forms.Form):
    number = forms.IntegerField(label='Введите число')
