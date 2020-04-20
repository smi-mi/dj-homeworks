from datetime import datetime
from django.urls import path, register_converter
from app.views import file_list, file_content


class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value) -> datetime:
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value: datetime) -> str:
        return value.strftime('%Y-%m-%d')

register_converter(DateConverter, 'date')

urlpatterns = [
    path('file-list/', file_list, name='file_list'),
    path('file-list/<date:date>/', file_list, name='file_list'),
    path('file-content/<name>/', file_content, name='file_content'),
]
