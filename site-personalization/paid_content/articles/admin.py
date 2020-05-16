from django.contrib import admin
from .models import Article, ArticleUser


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(ArticleUser)
class UserAdmin(admin.ModelAdmin):
    pass
