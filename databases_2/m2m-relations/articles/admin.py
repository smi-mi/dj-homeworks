from django.contrib import admin

from .models import Article, Scope, Relationship


class RelationshipInline(admin.TabularInline):

    model = Relationship
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        RelationshipInline,
    ]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = [
        RelationshipInline,
    ]
