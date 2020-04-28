from django.contrib import admin
from .models import Phone, Iphone, Samsung, Mi


@admin.register(Iphone)
class IphoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Samsung)
class SamsungAdmin(admin.ModelAdmin):
    pass


@admin.register(Mi)
class MiAdmin(admin.ModelAdmin):
    pass
