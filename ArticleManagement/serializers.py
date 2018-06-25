from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, BaseSerializer, Serializer

from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['article_id', 'edit_time', 'title', 'author', 'editor', 'content', 'creator']


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['name', 'superior']


class ArchivalArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivalArticles
        fields = ['article', 'column']


class ArticleStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleStat
        fields = ['article', 'stat']


class ArticlePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticlePermission
        fields = ['duty', 'column', 'permission']