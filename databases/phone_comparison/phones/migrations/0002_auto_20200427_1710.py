# Generated by Django 2.2.10 on 2020-04-27 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='processor',
            field=models.CharField(max_length=50),
        ),
    ]