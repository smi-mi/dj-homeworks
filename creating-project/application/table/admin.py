from django.contrib import admin
from .models import Table, Column


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    pass


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    pass
