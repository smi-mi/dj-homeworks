from django import template
from datetime import datetime


register = template.Library()


@register.filter
def format_date(value):
    date = datetime.fromtimestamp(value)
    seconds = (datetime.utcnow() - date).seconds
    minutes = seconds // 60
    hours = minutes // 60
    if minutes < 10:
        return 'только что'
    if hours < 24:
        return str(hours) + ' часов назад'
    return date.strftime('%Y-%m-%d')


@register.filter
def format_score(value, default=''):
    if value is None:
        return default
    if value < -5:
        return 'все плохо'
    if value <= 5:
        return 'нейтрально'
    return 'хорошо'


@register.filter
def format_num_comments(value):
    if value == 0:
        return 'Оставьте комментарий'
    if value <= 50:
        return value
    return '50+'


@register.filter
def format_selftext(value, count):
    if len(value) < 2 * count:
        return value
    str_array = value.split()
    first = str_array[:count]
    last = str_array[-count:]
    return " ".join(first + ['...'] + last)
