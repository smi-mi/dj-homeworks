# Generated by Django 2.2.10 on 2020-05-18 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_auto_20200517_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='path',
            field=models.CharField(max_length=50, verbose_name='Путь к csv-файлу'),
        ),
    ]