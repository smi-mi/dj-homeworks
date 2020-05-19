from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', default='')
    path = models.CharField(verbose_name='Путь к csv-файлу', max_length=50)

    @staticmethod
    def get_path():
        return Table.objects.first().path

    @staticmethod
    def set_path(path):
        table = Table.objects.first()
        table.path = path
        table.save()


class Column(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    order_num = models.PositiveIntegerField(verbose_name='Порядковый номер')
    width = models.PositiveIntegerField(verbose_name='Ширина')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='columns')
