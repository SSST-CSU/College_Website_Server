from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'article_id', 'edit_time', 'title', 'author', 'editor', 'creator']


admin.site.register(Article, ArticleAdmin)


class ColumnAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'superior']


admin.site.register(Column, ColumnAdmin)


class ArchivalArticlesAdmin(admin.ModelAdmin):
    list_display = ['article', 'column']


admin.site.register(ArchivalArticles, ArchivalArticlesAdmin)


class ArticleStatAdmin(admin.ModelAdmin):
    list_display = ['article', 'stat']


admin.site.register(ArticleStat, ArticleStatAdmin)


class ArticlePermissionAdmin(admin.ModelAdmin):
    list_display = ['duty', 'column', 'permission']


admin.site.register(ArticlePermission, ArticlePermissionAdmin)
