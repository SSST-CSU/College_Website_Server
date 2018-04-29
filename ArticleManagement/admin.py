from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['creation_time', 'title', 'author', 'editor', 'content']


class ColumnAdmin(admin.ModelAdmin):
    list_display = ['name']


class ArchivalArticlesAdmin(admin.ModelAdmin):
    list_display = ['article', 'column']


class ArticleStatAdmin(admin.ModelAdmin):
    list_display = ['article', 'stat']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(ArchivalArticles, ArchivalArticlesAdmin)
admin.site.register(ArticleStat, ArticleStatAdmin)
