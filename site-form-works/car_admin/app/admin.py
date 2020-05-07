from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    readonly_fields = ['review_count']
    Car.review_count.short_description = 'Количество статей'
    search_fields = ['brand', 'model']
    list_display = ['brand', 'model', 'review_count']
    list_filter = ['brand']
    ordering = ['-id']


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    search_fields = ['title', 'car__brand', 'car__model']
    list_display = ['car', 'title']
    list_filter = ['car', 'car__brand']
    ordering = ['-id']


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
