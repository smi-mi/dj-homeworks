from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Relationship


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_mains = 0
        for form in self.forms:
            is_main = form.cleaned_data.get('is_main')
            if is_main:
                count_mains += 1

        if count_mains == 0:
            raise ValidationError('Укажите основной раздел')
        if count_mains > 1:
            raise ValidationError('Укажите только один основной раздел')
        return super().clean()


class RelationshipInline(admin.TabularInline):

    model = Relationship
    extra = 1
    formset = RelationshipInlineFormset


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
